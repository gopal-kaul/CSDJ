import PySimpleGUI as sg
from youtube_search import YoutubeSearch
import json
import pafy
import os
import subprocess
import shutil
import platform


def search(name):
    # To get all the video links
    results = YoutubeSearch(name, max_results=5).to_json()
    best = json.loads(results)  # The top video
    # Complete Download Link
    download_link = f'https://youtube.com{best["videos"][0]["url_suffix"]}'
    print(download_link)  # Printing for debuggind
    return download_link  # Returning it to the download functon


def download(name):
    link = search(name)  # Searching the song on YT
    song = pafy.new(link)  # Finding the song using PAFY
    dl = song.getbestaudio()  # Getting the best song and audio quality
    path = os.path.join(os.getcwd(), "cache", f"{name}.webm")
    # Downloading it with output to console
    dl.download(quiet=False, filepath=path)
    # os.rename(title, name)
    if platform.system() == 'Windows':
        ffmpeg_cmd = f"'{os.path.join(os.getcwd(), 'utils', 'ffmpegw.exe')}'" + " -i " + f"'{os.path.join(os.getcwd(),'cache',f'{name}.webm')}'" +  \
            " -acodec pcm_s16le -ar 22050 -ac 1 -fflags +bitexact -flags:v +bitexact -flags:a +bitexact " + \
            f'"{os.path.join(os.getcwd(),"cache","voice_input.wav")}"' + " -y"
        print(ffmpeg_cmd)
        subprocess.call(ffmpeg_cmd, shell=True)
    # Call to ffmpeg to run the conversion
    elif platform.system() == "Linux":
        ffmpeg_cmd = f'"{os.path.join(os.getcwd(), "utils","ffmpeglinux")}"' + " -i " + f"'{os.path.join(os.getcwd(),'cache',f'{name}.webm')}'" +  \
            " -acodec pcm_s16le -ar 22050 -ac 1 -fflags +bitexact -flags:v +bitexact -flags:a +bitexact " + \
            f'"{os.path.join(os.getcwd(),"cache","voice_input.wav")}"' + " -y"
        print(ffmpeg_cmd)
        subprocess.call(ffmpeg_cmd, shell=True)


def movetodir():
    try:
        cfg = open('csdir.cfg')
        dest = str(cfg.read())
        path = os.path.join(os.getcwd(), 'cache' 'voice_input.wav')
        if platform.system() == 'Windows':
            shutil.copy(path, f"{dest}\\")
        elif platform.system() == "Linux":
            shutil.copy(path, f"{dest}")
        print("Copied!")
        if os.path.exists(os.path.join(dest, 'csgo', 'cfg', 'csdj.cfg')) == False:
            shutil.copy(f'{os.path.join(os.getcwd(),"csdj.cfg")}',
                        f"{os.path.join(dest,'csgo','cfg')}")
        cfg.close()
    except FileNotFoundError:  # File does not exist!
        dest = ''
        # Adding(Trying to add default path):
        if platform.system() == "Windows":
            if os.path.isdir(os.path.join("C:", "Program Files (x86)", "Steam", "steamapps", "common", "Counter-Strike Global Offensive")) == True:
                dest = os.path.join("C:", "Program Files (x86)", "Steam",
                                    "steamapps", "common", "Counter-Strike Global Offensive")
            elif os.path.isdir(os.path.join("C:", "Program Files", "Steam", "steamapps", "common", "Counter-Strike Global Offensive")) == True:
                dest = os.path.join("C:", "Program Files", "Steam",
                                    "steamapps", "common", "Counter-Strike Global Offensive")
        elif platform.system() == "Linux":
            if os.path.isdir(os.path.join(os.path.expanduser("~"), ".steam", "steam", "steamapps", "common", "Counter-Strike Global Offensive")) == True:
                dest = os.path.join(os.path.expanduser(
                    "~"), ".steam", "steam", "steamapps", "common", "Counter-Strike Global Offensive")
        if dest == '':
            dest = input("Enter your CSGO install dir : ")
        cfg = open('csdir.cfg', 'w')
        cfg.write(dest)
        path = os.path.join(os.getcwd(), 'cache', 'voice_input.wav')
        if platform.system() == 'Windows':
            shutil.copy(path, f"{dest}\\")
        elif platform.system() == "Linux":
            shutil.copy(path, f"{dest}")
        print("Copied!")
        if os.path.exists(os.path.join(dest, 'csgo', 'cfg', 'csdj.cfg')) == False:
            shutil.copy(f'{os.path.join(os.getcwd(),"csdj.cfg")}',
                        f"{os.path.join(dest,'csgo','cfg')}")
        cfg.close()


sg.theme('Dark Blue 3')
layout = [
    [sg.Text("Enter a song name : ")],
    [sg.Input()],
    [sg.Ok()]
]
window = sg.Window('CSDJ', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Ok':
        download(values[0])
        movetodir()
        sg.popup_ok(f"{values[0]} successfully downloaded and copied!")
window.close()
