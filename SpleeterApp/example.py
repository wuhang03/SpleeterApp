import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl, QPropertyAnimation, QEasingCurve
from PyQt5.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QStyle

from audio_player import AudioPlayer


class MainWindowUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self._setup_ui()

        self.setWindowTitle('sound fading')
        self.setGeometry(100, 100, 100, 100)

    def _setup_ui(self):
        self.central_widget = QWidget(self)
        self.central_widget_layout = QVBoxLayout(self.central_widget)
        self.setCentralWidget(self.central_widget)

        self.player = AudioPlayer()
        self.user_action = -1  # 0 - stopped, 1 - playing, 2 - paused
        self.play_button = QPushButton()
        self.play_button.clicked.connect(self.play_pause_button_clicked)

        self.play_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay)
        self.pause_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause)
        self.play_button.setIcon(self.play_icon)

        self.central_widget_layout.addWidget(self.play_button)

    def play(self):
        print("Play")
        self.play_button.setIcon(self.pause_icon)
        self.user_action = 1
        self.player.setSource(QUrl("some audio file path"))
        self.player.play()

    def pause(self):
        print("Pause")
        self.play_button.setIcon(self.play_icon)
        self.user_action = 2
        self.player.pause()

    def unpause(self):
        print("Unpause")
        self.play_button.setIcon(self.pause_icon)
        self.user_action = 1
        self.player.play()

    def play_pause_button_clicked(self):
        if self.user_action <= 0:
            self.play()
        elif self.user_action == 1:
            self.pause()
        elif self.user_action == 2:
            self.unpause()


class AudioPlayer(QMediaPlayer):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.audio_output = QAudioOutput()
        self.audio_output.volumeChanged.connect(lambda: print(self.audio_output.volume()))
        self.setAudioOutput(self.audio_output)
        self.audioOutput().setVolume(.5)
        self.current_volume = self.audio_output.volume()

        self.fade_in_anim = QPropertyAnimation(self.audio_output, b"volume")
        self.fade_in_anim.setDuration(1400)
        self.fade_in_anim.setStartValue(0.01)
        self.fade_in_anim.setEndValue(self.current_volume)
        self.fade_in_anim.setEasingCurve(QEasingCurve.Type.Linear)
        self.fade_in_anim.setKeyValueAt(0.01, 0.01)

        self.fade_out_anim = QPropertyAnimation(self.audio_output, b"volume")
        self.fade_out_anim.setDuration(600)
        self.fade_out_anim.setStartValue(self.current_volume)
        self.fade_out_anim.setEndValue(0)
        self.fade_out_anim.setEasingCurve(QEasingCurve.Type.Linear)
        self.fade_out_anim.setKeyValueAt(0.01, self.current_volume)
        self.fade_out_anim.finished.connect(super().pause)

    def play(self):
        self.audio_output.setVolume(0.01)
        self.fade_in_anim.setEndValue(self.current_volume)
        super().play()
        self.fade_in_anim.start()

    def pause(self):
        self.current_volume = self.audio_output.volume()
        self.fade_out_anim.setStartValue(self.current_volume)
        self.fade_out_anim.start()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindowUi()
    mainWindow.show()

    sys.exit(app.exec())