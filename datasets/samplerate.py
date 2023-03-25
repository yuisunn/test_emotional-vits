import os
import subprocess

def reform_fre(input_path, output_path):
    i = 1
    for file in os.listdir(input_path):

        file1 = input_path + '\\' + file

       # file2 = output_path + '\\' + ''+str("%04d" % (int(os.path.splitext(file)	[0])+1)) + '.wav'
        file2 = output_path + '\\' + file

       # cmd = "ffmpeg -y -i " + file1 + " -ac 1 -ar 22050 -f wav " + file2 + " -y"

        cmd = "ffmpeg -y -i " + file1 + " -ar 16000 -f wav " + file2
        # 对mp3视频进行采样率 格式 声道
        subprocess.call(cmd, shell=True)
        cmd = "sox " + file2 + " -b 16 " + file2
        subprocess.call(cmd, shell=True)
        i = i + 1

"""此工程用于对mp3文件进行转换"""

if __name__ == '__main__':

    your_pathdir_origin = r"D:\_AI\vits_emotional\datasets\redrabbit"
    your_pathdir_output = your_pathdir_origin+"wav"
    if not os.path.isdir(your_pathdir_output):
        # 创建文件夹
        os.mkdir(your_pathdir_output)
    reform_fre(your_pathdir_origin,your_pathdir_output)