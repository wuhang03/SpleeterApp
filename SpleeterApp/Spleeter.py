<<<<<<< Updated upstream
import os
=======

from PyQt5.QtCore import QThread
>>>>>>> Stashed changes
import subprocess
import os

class SpleeterThread(QThread):
    def __init__(self, input_file, output_dir):
        QThread.__init__(self)
        self.input_file = input_file
        self.output_dir = output_dir

    def run(self):
        print("spleeter running")
        os.chdir("./SpleeterApp")
        num_stems = 5
        command = f'spleeter separate -p spleeter:{num_stems}stems -o {self.output_dir} {self.input_file}'
        subprocess.run(command, shell=True, encoding='utf-8')
