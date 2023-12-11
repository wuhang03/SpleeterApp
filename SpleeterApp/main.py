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
    # ������ť�ͱ�ǩ
    self.select_folder_button = QPushButton('ѡ����Ƶ�ļ���', self)
    self.select_folder_button.clicked.connect(self.select_folder)

    self.overlay_button = QPushButton('������Ƶ', self)
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
    self.input_file = ""  # ������Ƶ��·��
    self.output_dir = ""  # �����Ƶ��·��
    self.music_name = ""  # ��Ƶ������
    self.music_play = ""  # ���ڲ��ŵ�����·��

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

    # �������ֹ�����
    vbox = QVBoxLayout()
    vbox.addWidget(self.select_folder_button)
    vbox.addWidget(self.overlay_button)
    vbox.addWidget(self.info_label)

    # ����������
    self.setLayout(vbox)

    # ���ô��ڱ���ʹ�С
    self.setWindowTitle('��Ƶ����Ӧ��')
    self.setGeometry(300, 300, 300, 200)

  def select_folder(self):
    # ���ļ���ѡ��Ի���
    folder_path = QFileDialog.getExistingDirectory(self, 'ѡ����Ƶ�ļ���')
    self.selected_folder = folder_path
    self.info_label.setText(f'��ѡ����Ƶ�ļ��У�{folder_path}')

  def overlay_audio(self):
    if hasattr(self, 'selected_folder'):
      # ��ȡ�ļ��������е���Ƶ�ļ�
      audio_files = [f for f in os.listdir(self.selected_folder) if f.endswith('.wav')]

<<<<<<< Updated upstream
      # ��ʼ�������Ƶ
      output = None

      # ѭ������ÿ����Ƶ�ļ�
      for audio_file in audio_files:
        # ������Ƶ�ļ�������·��
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
    print("������")
    self.spleeter_thread = SpleeterThread(self.input_file, self.output_dir)
    self.spleeter_thread.start()

>>>>>>> Stashed changes

        # ��ȡ��Ƶ�ļ�
        sound = AudioSegment.from_wav(audio_path)

        # ����ǵ�һ����Ƶ�ļ���ֱ�Ӹ�ֵ��output��������ӵ�output��
        if output is None:
          output = sound
        else:
          output = output.overlay(sound)

      # ��������ļ�������·�������浽�����ļ�����
      output_file_name = 'output.wav'
      output_path = os.path.join(self.selected_folder, output_file_name)

      # ��������ļ���ָ��λ��
      output.export(output_path, format="wav")

<<<<<<< Updated upstream
      self.info_label.setText(f'��Ƶ������ɣ�����ļ���{output_path}')
    else:
      self.info_label.setText('����ѡ����Ƶ�ļ���')
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
