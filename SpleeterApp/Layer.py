# coding=gb2312
from pydub import AudioSegment
import os


def lay_audio(audio_name, input_folder, output_folder):
    audio_files = [f for f in os.listdir(input_folder) if f.endswith('.wav')]
    output = None
    # ѭ������ÿ����Ƶ�ļ�
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

audio_name = input("������Ҫ�ϳɵ���Ƶ���ƣ�")
input_folder = input("��������Դ�ļ���·����")
output_folder = input("����������ļ���·����")
print("������")
lay_audio(audio_name, input_folder,output_folder)
print("�������")