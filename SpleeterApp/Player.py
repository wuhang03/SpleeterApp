from PyQt5.QtCore import QThread
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl


class MusicPlayerThread(QThread):
    def __init__(self, ui, media_player):
        QThread.__init__(self)
        self.ui = ui
        self.media_player = media_player
        self.is_playing = False

    def run(self, music_file):
        print("run")
        if self.is_playing:
            self.media_player.stop()
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(music_file)))
        self.media_player.play()
        self.is_playing = True
        # self.media_player.stateChanged.connect(self.state_changed)

        self.exec_()

    def play_music(self, music_file):
        if self.is_playing:
            self.media_player.stop()
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(music_file)))
        self.media_player.play()
        self.is_playing = True

    def state_changed(self, state):
        print("state changed")
        if state == QMediaPlayer.PlayingState:
            self.ui.pushButton_play.setIcon(QIcon("picture/pause_5072281.png"))
        else:
            self.ui.pushButton_play.setIcon(QIcon("picture/play_13004132.png"))
            self.is_playing = False