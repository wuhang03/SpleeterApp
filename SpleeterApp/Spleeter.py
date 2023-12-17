import os
import subprocess

<<<<<<< Updated upstream
=======
class SpleeterThread(QThread):
    def __init__(self, input_file, output_dir,parent=None):
        super(SpleeterThread,self).__init__(parent)
        self.input_file = input_file
        self.output_dir = output_dir
>>>>>>> Stashed changes

def run_spleeter(num_stems, input_file, output_dir):
    command = f'spleeter separate -p spleeter:{num_stems}stems -o {output_dir} {input_file}'
    subprocess.run(command, shell=True, encoding='utf-8')


# 用户输入音轨数和路径
num_stems = input("请输入音轨数：")
input_file = input("请输入输入文件路径：")
output_dir = input("请输入输出目录路径：")
print("进行中")

# 调用函数执行Spleeter命令
run_spleeter(num_stems, input_file, output_dir)