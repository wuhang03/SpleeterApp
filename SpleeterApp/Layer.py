# coding=gb2312
from pydub import AudioSegment
import os


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

audio_name = input("请输入要合成的音频名称：")
input_folder = input("请输入音源文件夹路径：")
output_folder = input("请输入输出文件夹路径：")
print("叠加中")
lay_audio(audio_name, input_folder,output_folder)
print("叠加完成")