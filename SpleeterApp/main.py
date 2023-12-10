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
    # 创建按钮和标签
    self.select_folder_button = QPushButton('选择音频文件夹', self)
    self.select_folder_button.clicked.connect(self.select_folder)

    self.overlay_button = QPushButton('叠加音频', self)
    self.overlay_button.clicked.connect(self.overlay_audio)

    self.info_label = QLabel(self)

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

      # 初始化输出音频
      output = None

      # 循环处理每个音频文件
      for audio_file in audio_files:
        # 构建音频文件的完整路径
        audio_path = os.path.join(self.selected_folder, audio_file)

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

      self.info_label.setText(f'音频叠加完成，输出文件：{output_path}')
    else:
      self.info_label.setText('请先选择音频文件夹')

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = AudioOverlayApp()
  ex.show()
  sys.exit(app.exec_())
