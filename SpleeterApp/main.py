# coding=gb2312
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog
from pydub import AudioSegment
import os

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

      # ��ʼ�������Ƶ
      output = None

      # ѭ������ÿ����Ƶ�ļ�
      for audio_file in audio_files:
        # ������Ƶ�ļ�������·��
        audio_path = os.path.join(self.selected_folder, audio_file)

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

      self.info_label.setText(f'��Ƶ������ɣ�����ļ���{output_path}')
    else:
      self.info_label.setText('����ѡ����Ƶ�ļ���')

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = AudioOverlayApp()
  ex.show()
  sys.exit(app.exec_())
