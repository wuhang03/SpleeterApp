# coding=gb2312
import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog
from pydub import AudioSegment
import os
<<<<<<< Updated upstream

class AudioOverlayApp(QWidget):
  def __init__(self):
    super().__init__()

    self.init_ui()

  def init_ui(self):
    # 创建按钮和标签
    self.select_folder_button = QPushButton('选择音频文件夹', self)
    self.select_folder_button.clicked.connect(self.select_folder)

    self.overlay_button = QPushButton('叠加音频', self)
    self.overlay_button.clicked.connect(self.overlay_audio)

    self.info_label = QLabel(self)
=======
from untitled import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QAudioProbe
from Player import MusicPlayerThread
from Spleeter import SpleeterThread

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QFont, QFontMetrics



class AudioOverlayApp(QtWidgets.QMainWindow):
  def __init__(self):
    super(AudioOverlayApp, self).__init__()
    self.input_file = ""  # 输入音频的路径
    self.output_dir = ""  # 输出音频的路径
    self.music_name = ""  # 音频的名称
    self.music_play = ""  # 正在播放的音乐路径

    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.set_dur=False
    self.ui.pushButton_play.setDisabled(1)

    self.ui.pushButton_input1.clicked.connect(self.select_music)
    self.ui.pushButton_output1.clicked.connect(self.spleeter)
    self.ui.pushButton_play.clicked.connect(self.play_music)

    # choose the kind of audio
    self.ui.pushButton_vocal.clicked.connect(self.play_vocal)
    self.ui.pushButton_original.clicked.connect(self.play_original)
    self.ui.pushButton_drum.clicked.connect(self.play_drum)
    self.ui.pushButton_piano.clicked.connect(self.play_piano)

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
    self.music_playfile = self.output_dir + '/' + self.music_name + '/piano.wav'
    self.play_music()
    print(self.music_play)

>>>>>>> Stashed changes

    # 创建布局管理器
    vbox = QVBoxLayout()
    vbox.addWidget(self.select_folder_button)
    vbox.addWidget(self.overlay_button)
    vbox.addWidget(self.info_label)

    # 设置主布局
    self.setLayout(vbox)

    # 设置窗口标题和大小
    self.setWindowTitle('音频叠加应用')
    self.setGeometry(300, 300, 300, 200)

  def select_folder(self):
    # 打开文件夹选择对话框
    folder_path = QFileDialog.getExistingDirectory(self, '选择音频文件夹')
    self.selected_folder = folder_path
    self.info_label.setText(f'已选择音频文件夹：{folder_path}')

  def overlay_audio(self):
    if hasattr(self, 'selected_folder'):
      # 获取文件夹中所有的音频文件
      audio_files = [f for f in os.listdir(self.selected_folder) if f.endswith('.wav')]

<<<<<<< Updated upstream
      # 初始化输出音频
      output = None

      # 循环处理每个音频文件
      for audio_file in audio_files:
        # 构建音频文件的完整路径
        audio_path = os.path.join(self.selected_folder, audio_file)
=======

      self.ui.label_songname.setText(file_name_without_extension)
      self.adjust_font_size(self.ui.label_songname)
      self.ui.pushButton_play.setDisabled(False)

      self.input_file = file_name
      self.music_play = file_name
      self.music_name = file_name_without_extension
      print(self.music_name)


  def spleeter(self):
    os.chdir("..")
    self.output_dir = QFileDialog.getExistingDirectory(self, 'Select Output Folder')
    print(self.input_file)
    print(self.output_dir)
    print(self.music_name)
    print("进行中")
    self.spleeter_thread = SpleeterThread(self.input_file, self.output_dir)
    self.spleeter_thread.start()

>>>>>>> Stashed changes

        # 读取音频文件
        sound = AudioSegment.from_wav(audio_path)

        # 如果是第一个音频文件，直接赋值给output；否则叠加到output上
        if output is None:
          output = sound
        else:
          output = output.overlay(sound)

      # 构建输出文件的完整路径，保存到输入文件夹中
      output_file_name = 'output.wav'
      output_path = os.path.join(self.selected_folder, output_file_name)

      # 保存输出文件到指定位置
      output.export(output_path, format="wav")

<<<<<<< Updated upstream
      self.info_label.setText(f'音频叠加完成，输出文件：{output_path}')
    else:
      self.info_label.setText('请先选择音频文件夹')
=======

  def play_music(self):
    self.music_player_thread = MusicPlayerThread(self.ui)
    self.music_player_thread.play_music(self.music_play)

  def update_position(self, position):
    self.ui.horizontalSlider.setValue(position)
    if position>0 and self.set_dur is False:
      self.set_dur=True
      self.ui.horizontalSlider.setRange(0, self.media_player.duration())
      minutes, seconds = divmod(self.media_player.duration() / 1000, 60)
      self.ui.label_time_total.setText(f"{int(minutes):02d}:{int(seconds):02d}")
      # print( self.media_player.duration())
    minutes, seconds = divmod(position / 1000, 60)
    self.ui.label_time.setText(f"{int(minutes):02d}:{int(seconds):02d}")
>>>>>>> Stashed changes


if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = AudioOverlayApp()
  ex.show()
  sys.exit(app.exec_())
