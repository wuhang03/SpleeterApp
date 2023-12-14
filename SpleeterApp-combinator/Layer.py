# coding=gb2312
from pydub import AudioSegment
import os
from PyQt5.QtCore import QThread, pyqtSignal
import shutil

class SaveCombinationThread(QThread):
  finished = pyqtSignal()

  def __init__(self, output_dir, music_play):
    super().__init__()
    self.output_dir = output_dir
    self.music_play = music_play

  def run(self):
    source_file = self.music_play
    destination_folder = self.output_dir

    shutil.move(source_file, destination_folder)

    print("Save completed.")
    self.finished.emit()

def lay_audio(audio_name, input_folder, output_folder):
    audio_files = [f for f in os.listdir(input_folder) if f.endswith('.wav')]
    output = None
    # 循环处理每个音频文件
    for audio_file in audio_files:
        audio_path = os.path.join(input_folder, audio_file)
        print(audio_path)
        sound = AudioSegment.from_wav(audio_path)
        if output is None:
            output = sound
        else:
            output = output.overlay(sound)

    output_file_name = audio_name + '.wav'
    output_path = os.path.join(output_folder, output_file_name)
    print(output_path)
    output.export(output_path, format="wav")