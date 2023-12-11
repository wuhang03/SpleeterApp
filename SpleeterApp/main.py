# coding=gb2312
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog
# from pydub import AudioSegment
import os
from untitled import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QAudioProbe
from PyQt5.QtCore import Qt, QTimer
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QFont, QFontMetrics

class AudioOverlayApp(QtWidgets.QMainWindow):
  def __init__(self):
    super(AudioOverlayApp, self).__init__()
    self.ui = Ui_MainWindow()
    #self.setFixedSize(860, 874)
    self.ui.setupUi(self)
    self.set_dur=False
    self.ui.pushButton_play.setDisabled(1)

    self.ui.pushButton_input1.clicked.connect(self.select_music)
    self.ui.pushButton_play.clicked.connect(self.play_music)

    self.media_player = QMediaPlayer()
    self.media_player.positionChanged.connect(lambda x:self.update_position(x))

    # # 连接 mediaStatusChanged 信号到处理函数
    # self.media_player.mediaStatusChanged.connect(lambda x: self.handle_media_status_changed(x))
    # 在程序退出前调用 deleteLater()
    app.aboutToQuit.connect(self.media_player.deleteLater)

    #self.ui.gridLayout_3.addWidget(self.ui.media_player,6,1,1,3)


  def select_music(self):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    file_name, _ = QFileDialog.getOpenFileName(self, 'Select Music File', '',
                                               'Music Files (*.mp3 *.wav);;All Files (*)', options=options)
    if file_name:
      media_content = QMediaContent(QUrl.fromLocalFile(file_name))
      self.media_player.setMedia(media_content)

      #通过从后向前搜索第一个点和第一个反斜杠，确定文件路径
      last_slash_index = file_name.rfind('/')

      # 提取文件名（包括扩展名）
      file_name_with_extension = file_name[last_slash_index + 1:]

      # 去掉扩展名
      last_dot_index = file_name_with_extension.rfind('.')
      file_name_without_extension = file_name_with_extension[:last_dot_index]

      self.ui.label_songname.setText(file_name_without_extension)
      self.adjust_font_size(self.ui.label_songname)
      self.ui.pushButton_play.setDisabled(False)


  def adjust_font_size(self,label):
    text = label.text()
    print('text:', text)
    font = label.font()
    # 测量文本的宽度
    fm = QFontMetrics(font)
    text_width = fm.width(text)
    font_size=font.pointSize()
    # 获取标签的宽度
    label_width = label.width()

    # 如果文本宽度超过标签宽度，调整字体大小
    while text_width > label_width:
      font_size -= 1
      font.setPointSize(font_size)
      label.setFont(font)

      fm = QFontMetrics(font)
      text_width = fm.width(text)



  def play_music(self):
    print('clicked'+str(self.media_player.state()))
    if self.media_player.state() == QMediaPlayer.PlayingState:
      self.media_player.pause()
      self.ui.gif.stop()
      self.ui.pushButton_play.setIcon(QtGui.QIcon("picture/play_13004132.png"))
    else:
      print('play')
      self.media_player.play()
      print("Media player error:", self.media_player.errorString(),'Position:',self.media_player.position())
      self.ui.gif.start()
      self.ui.pushButton_play.setIcon(QtGui.QIcon("picture/pause_5072281.png"))

  def update_position(self, position):
    #print('setvalue')
    self.ui.horizontalSlider.setValue(position)
    # print('position:',position)
    # print(self.media_player.duration(),' ',self.ui.horizontalSlider.maximum())
    if position>0 and self.set_dur is False:
      self.set_dur=True
      self.ui.horizontalSlider.setRange(0, self.media_player.duration())
      minutes, seconds = divmod(self.media_player.duration() / 1000, 60)
      self.ui.label_time_total.setText(f"{int(minutes):02d}:{int(seconds):02d}")
      # print( self.media_player.duration())
    minutes, seconds = divmod(position / 1000, 60)
    self.ui.label_time.setText(f"{int(minutes):02d}:{int(seconds):02d}")

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = AudioOverlayApp()
  ex.show()
  sys.exit(app.exec_())

