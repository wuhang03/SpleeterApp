# coding=gb2312
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog
<<<<<<< Updated upstream
from pydub import AudioSegment
=======
>>>>>>> Stashed changes
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
=======
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QFont, QFontMetrics
import Layer
from PyQt5.QtGui import QMovie


class AudioOverlayApp(QtWidgets.QMainWindow):
  def __init__(self):
    super(AudioOverlayApp, self).__init__()
    self.input_file = ""  # ������Ƶ��·��
    self.output_dir = ""  # �����Ƶ��·��
    self.music_name = ""  # ��Ƶ������
    self.music_play = ""  # ���ڲ��ŵ�����·��
    self.input_folder = ""  # �������Ҫ�ϲ����������ڵ��ļ���

    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.set_dur=False
    self.set_dur2=False
    self.ui.pushButton_play.setDisabled(1)
    self.gif2 = QMovie("picture/music-7683_512.gif")
    self.ui.label_gif_2.setMovie(self.gif2)
    self.gif2.start()
    self.gif2.stop()
    # self.gif = QMovie("picture/music-9262_512.gif")
    # self.ui.label_gif.setMovie(self.gif)
    # self.gif.start()
    # self.gif.stop()
    self.ui.pushButton_input1.clicked.connect(self.select_music)
    self.ui.pushButton_output1.clicked.connect(self.spleeter)
    self.ui.pushButton_play.clicked.connect(self.play_music)
    self.ui.pushButton_play.clicked.connect(lambda x:self.ui.gif.stop())
>>>>>>> Stashed changes

    self.overlay_button = QPushButton('������Ƶ', self)
    self.overlay_button.clicked.connect(self.overlay_audio)

<<<<<<< Updated upstream
    self.info_label = QLabel(self)
=======
    # choose the folder of audio
    self.ui.pushButton_12.clicked.connect(self.load_input_folder)
    self.ui.pushButton_play_2.clicked.connect(self.play_music_comb)
    self.ui.pushButton_10.clicked.connect(self.save_combination)

    self.media_player = QMediaPlayer()
    self.media_player.positionChanged.connect(lambda x: self.update_position(x))

    self.media_player_comb = QMediaPlayer()
    self.media_player_comb.positionChanged.connect(lambda x: self.update_position_comb(x))
>>>>>>> Stashed changes

    # �������ֹ�����
    vbox = QVBoxLayout()
    vbox.addWidget(self.select_folder_button)
    vbox.addWidget(self.overlay_button)
    vbox.addWidget(self.info_label)

<<<<<<< Updated upstream
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
=======
    app.aboutToQuit.connect(self.media_player.deleteLater)
    app.aboutToQuit.connect(self.media_player_comb.deleteLater)

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
      media_content = QMediaContent(QUrl.fromLocalFile(self.music_play))
      self.media_player_comb.setMedia(media_content)

  def save_combination(self):
    os.chdir("..")
    self.output_dir = QFileDialog.getExistingDirectory(self, 'Select Output Folder')
    print("Processing...")
    self.save_thread = Layer.SaveCombinationThread(self.output_dir, self.music_play)
    self.save_thread.start()

  def play_vocal(self):
    self.music_play = self.output_dir + '/' + self.music_name + '/vocals.wav'
    media_content = QMediaContent(QUrl.fromLocalFile(self.music_play))
    self.media_player.setMedia(media_content)
    self.play_music()
    print(self.music_play)
>>>>>>> Stashed changes

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

        # ��ȡ��Ƶ�ļ�
        sound = AudioSegment.from_wav(audio_path)
=======
  def play_original(self):
    self.music_play = self.input_file
    media_content = QMediaContent(QUrl.fromLocalFile(self.music_play))
    self.media_player.setMedia(media_content)
    self.play_music()
    print(self.music_play)

  def play_drum(self):
    self.music_play = self.output_dir + '/' + self.music_name + '/drums.wav'
    media_content = QMediaContent(QUrl.fromLocalFile(self.music_play))
    self.media_player.setMedia(media_content)
    self.play_music()
    print(self.music_play)

  def play_piano(self):
    self.music_playfile = self.output_dir + '/' + self.music_name + '/piano.wav'
    media_content = QMediaContent(QUrl.fromLocalFile(self.music_play))
    self.media_player.setMedia(media_content)
    self.play_music()
    print(self.music_play)
>>>>>>> Stashed changes

        # ����ǵ�һ����Ƶ�ļ���ֱ�Ӹ�ֵ��output��������ӵ�output��
        if output is None:
          output = sound
        else:
          output = output.overlay(sound)

      # ��������ļ�������·�������浽�����ļ�����
      output_file_name = 'output.wav'
      output_path = os.path.join(self.selected_folder, output_file_name)

<<<<<<< Updated upstream
      # ��������ļ���ָ��λ��
      output.export(output_path, format="wav")

      self.info_label.setText(f'��Ƶ������ɣ�����ļ���{output_path}')
    else:
      self.info_label.setText('����ѡ����Ƶ�ļ���')
=======
  def select_music(self):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    file_name, _ = QFileDialog.getOpenFileName(self, 'Select Music File', '',
                                               'Music Files (*.mp3 *.wav);;All Files (*)', options=options)
    if file_name:
      media_content = QMediaContent(QUrl.fromLocalFile(file_name))
      self.media_player.setMedia(media_content)

      #ͨ���Ӻ���ǰ������һ����͵�һ����б�ܣ�ȷ���ļ�·��
      last_slash_index = file_name.rfind('/')

      # ��ȡ�ļ�����������չ����
      file_name_with_extension = file_name[last_slash_index + 1:]

      # ȥ����չ��
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
    self.output_dir = QFileDialog.getExistingDirectory(self, 'Select Output Folder')
    self.ui.label_output_path.setText(self.output_dir)
    print(self.input_file)
    print(self.output_dir)
    print(self.music_name)
    print("������")
    self.spleeter_thread = SpleeterThread(self.input_file, self.output_dir)
    self.spleeter_thread.start()


  def adjust_font_size(self,label):
    text = label.text()
    print('text:', text)
    font = label.font()
    # �����ı��Ŀ��
    fm = QFontMetrics(font)
    text_width = fm.width(text)
    font_size=font.pointSize()
    # ��ȡ��ǩ�Ŀ��
    label_width = label.width()

    # ����ı���ȳ�����ǩ��ȣ����������С
    while text_width > label_width:
      font_size -= 1
      font.setPointSize(font_size)
      label.setFont(font)

      fm = QFontMetrics(font)
      text_width = fm.width(text)



  def play_music(self):
    # print('clicked' + str(self.media_player.state()))
    # if self.media_player.state() == QMediaPlayer.PlayingState:
    #   self.ui.gif = QMovie("picture/music-9262_512.gif")
    #   self.ui.label_gif.setMovie(self.ui.gif)
    #   self.ui.gif.start()
    #   self.ui.gif.stop()
    #   self.ui.pushButton_play.setIcon(QtGui.QIcon("picture/play_13004132.png"))
    #   self.media_player.pause()
    #
    # else:
    #   self.ui.gif = QMovie("picture/music-9262_512.gif")
    #   self.ui.label_gif.setMovie(self.ui.gif)
    #   self.ui.gif.start()
    #   print("set icon")
    #   self.ui.pushButton_play.setIcon(QtGui.QIcon("picture/pause_5072281.png"))
    #   self.media_player.play()
    print('clicked' + str(self.media_player.state()))
    if self.media_player.state() == QMediaPlayer.PlayingState:
      self.media_player.pause()
      self.ui.gif.stop()
      self.ui.pushButton_play.setIcon(QtGui.QIcon("picture/play_13004132.png"))
    else:
      print('play')
      self.media_player.play()
      print("Media player error:", self.media_player.errorString(), 'Position:', self.media_player.position())
      self.ui.gif.start()
      self.ui.pushButton_play.setIcon(QtGui.QIcon("picture/pause_5072281.png"))


  def play_music_comb(self):
    print('clicked' + str(self.media_player_comb.state()))
    if self.media_player_comb.state() == QMediaPlayer.PlayingState:
      self.ui.gif2 = QMovie("picture/music-7683_512.gif")
      self.ui.label_gif_2.setMovie(self.ui.gif2)
      self.ui.gif2.start()
      self.ui.gif2.stop()
      self.ui.pushButton_play_2.setIcon(QtGui.QIcon("picture/play_13004132.png"))
      self.media_player_comb.pause()

    else:
      self.ui.gif2 = QMovie("picture/music-7683_512.gif")
      self.ui.label_gif_2.setMovie(self.ui.gif2)
      self.ui.gif2.start()
      print("set icon")
      self.ui.pushButton_play_2.setIcon(QtGui.QIcon("picture/pause_5072281.png"))
      self.media_player_comb.play()
      print("Media player error:", self.media_player_comb.errorString(), 'Position:', self.media_player_comb.position())

  def update_position(self, position):
    self.ui.horizontalSlider.setValue(position)
    if position>0 and self.set_dur is False:
      self.set_dur=True
      self.ui.horizontalSlider.setRange(0, self.media_player.duration())
      minutes, seconds = divmod(self.media_player.duration() / 1000, 60)
      self.ui.label_time_total.setText(f"{int(minutes):02d}:{int(seconds):02d}")
    minutes, seconds = divmod(position / 1000, 60)
    self.ui.label_time.setText(f"{int(minutes):02d}:{int(seconds):02d}")

  def update_position_comb(self, position):
    self.ui.horizontalSlider_2.setValue(position)
    if position>0 and self.set_dur2 is False:
      self.set_dur2=True
      self.ui.horizontalSlider_2.setRange(0, self.media_player_comb.duration())
      minutes, seconds = divmod(self.media_player_comb.duration() / 1000, 60)
      self.ui.label_time_end2.setText(f"{int(minutes):02d}:{int(seconds):02d}")
    minutes, seconds = divmod(position / 1000, 60)
    self.ui.label_time_2.setText(f"{int(minutes):02d}:{int(seconds):02d}")



>>>>>>> Stashed changes

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = AudioOverlayApp()
  ex.show()
  sys.exit(app.exec_())
