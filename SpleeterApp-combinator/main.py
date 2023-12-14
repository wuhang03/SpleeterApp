# coding=gb2312
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog
import os
from untitled import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QAudioProbe
from Player import MusicPlayerThread
from Spleeter import SpleeterThread

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QFont, QFontMetrics
import Layer

class AudioOverlayApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(AudioOverlayApp, self).__init__()
        self.input_file = ""
        self.output_dir = ""
        self.music_name = ""
        self.music_play = ""
        self.input_folder = ""

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_dur = False
        self.ui.pushButton_play.setDisabled(1)

        # Connect button events
        self.ui.pushButton_input1.clicked.connect(self.select_music)
        self.ui.pushButton_output1.clicked.connect(self.spleeter)
        self.ui.pushButton_play.clicked.connect(self.play_music)

        self.ui.pushButton_vocal.clicked.connect(self.play_vocal)
        self.ui.pushButton_original.clicked.connect(self.play_original)
        self.ui.pushButton_drum.clicked.connect(self.play_drum)
        self.ui.pushButton_piano.clicked.connect(self.play_piano)

        self.ui.pushButton_12.clicked.connect(self.load_input_folder)
        self.ui.pushButton_play_2.clicked.connect(self.play_music)
        self.ui.pushButton_10.clicked.connect(self.save_combination)

        self.media_player = QMediaPlayer()
        app.aboutToQuit.connect(self.media_player.deleteLater)

    def play_vocal(self):
        self.music_play = self.output_dir + '/' + self.music_name + '/vocals.wav'
        self.play_music()
        print(self.music_play)

    def play_original(self):
        self.music_play = self.input_file
        self.play_music()
        print(self.music_play)

    def play_drum(self):
        self.music_play = self.output_dir + '/' + self.music_name + '/drums.wav'
        self.play_music()
        print(self.music_play)

    def play_piano(self):
        self.music_play = self.output_dir + '/' + self.music_name + '/piano.wav'
        self.play_music()
        print(self.music_play)

    def select_music(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, 'Select Music File', '',
                                                   'Music Files (*.mp3 *.wav);;All Files (*)', options=options)
        if file_name:
            media_content = QMediaContent(QUrl.fromLocalFile(file_name))
            self.media_player.setMedia(media_content)

            last_slash_index = file_name.rfind('/')
            file_name_with_extension = file_name[last_slash_index + 1:]
            last_dot_index = file_name_with_extension.rfind('.')
            file_name_without_extension = file_name_with_extension[:last_dot_index]

            self.ui.label_songname.setText(file_name_without_extension)
            self.adjust_font_size(self.ui.label_songname)
            self.ui.pushButton_play.setDisabled(False)

            self.input_file = file_name
            self.music_play = file_name
            self.music_name = file_name_without_extension
            print(self.music_name)

    def spleeter(self):
        os.chdir("..")
        self.output_dir = QFileDialog.getExistingDirectory(self.ui, 'Select Output Folder')
        print(self.input_file)
        print(self.output_dir)
        print(self.music_name)
        print("Processing...")
        self.spleeter_thread = SpleeterThread(self.input_file, self.output_dir)
        self.spleeter_thread.start()

    def adjust_font_size(self, label):
        text = label.text()
        print('text:', text)
        font = label.font()
        fm = QFontMetrics(font)
        text_width = fm.width(text)
        font_size = font.pointSize()
        label_width = label.width()

        while text_width > label_width:
            font_size -= 1
            font.setPointSize(font_size)
            label.setFont(font)
            fm = QFontMetrics(font)
            text_width = fm.width(text)

    def play_music(self):
        self.music_player_thread = MusicPlayerThread(self.ui)
        self.music_player_thread.play_music(self.music_play)

    def update_position(self, position):
        self.ui.horizontalSlider.setValue(position)
        if position > 0 and self.set_dur is False:
            self.set_dur = True
            self.ui.horizontalSlider.setRange(0, self.media_player.duration())
            minutes, seconds = divmod(self.media_player.duration() / 1000, 60)
            self.ui.label_time_total.setText(f"{int(minutes):02d}:{int(seconds):02d}")
        minutes, seconds = divmod(position / 1000, 60)
        self.ui.label_time.setText(f"{int(minutes):02d}:{int(seconds):02d}")

    def load_input_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Select Input Folder', '')
        if folder_path:
            print(f"Input folder loaded: {folder_path}")
            self.input_folder = folder_path
            self.ui.label_5.setText(folder_path)
            self.music_name = "combined_music"
            self.output_dir = folder_path
            Layer.lay_audio(self.music_name, self.input_folder, self.output_dir)
            self.music_play = self.output_dir + '/' + self.music_name + '.wav'


    def save_combination(self):
        os.chdir("..")
        self.output_dir = QFileDialog.getExistingDirectory(self, 'Select Output Folder')
        print("Processing...")
        self.save_thread = Layer.SaveCombinationThread(self.output_dir, self.music_play)
        self.save_thread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AudioOverlayApp()
    ex.show()
    sys.exit(app.exec_())
