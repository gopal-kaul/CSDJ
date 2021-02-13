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
    dl.download(quiet=True, filepath=path)
    # os.rename(title, name)


def movetodir(name):
    if platform.system() == 'Windows':
        basedir = os.getcwd().replace(' ', r'\ ')
        ffmpeg_cmd = f"{os.path.join(basedir,'utils', 'ffmpegw.exe')}" + " -i " + f"{os.path.join(basedir,'cache',f'{name}.webm')}" + \
            " -acodec pcm_s16le -ar 22050 -ac 1 -fflags +bitexact -flags:v +bitexact -flags:a +bitexact " + \
            f"{os.path.join(basedir,'cache','voice_input.wav')}" + " -y"
        subprocess.call(ffmpeg_cmd, shell=True)
    # Call to ffmpeg to run the conversion
    elif platform.system() == "Linux":
        ffmpeg_cmd = f'"{os.path.join(os.getcwd(), "utils/","ffmpeglinux")}"' + " -i " + f"'{os.path.join(os.getcwd(),'cache/',f'{name}.webm')}'" +  \
            " -acodec pcm_s16le -ar 22050 -ac 1 -fflags +bitexact -flags:v +bitexact -flags:a +bitexact " + \
            f'"{os.path.join(os.getcwd(),"cache/","voice_input.wav")}"' + " -y"
        subprocess.call(ffmpeg_cmd, shell=True)

    try:
        cfg = open('csdir.cfg')
        dest = str(cfg.read())
        if platform.system() == 'Windows':
            path = os.path.join(os.getcwd(), 'cache\\', 'voice_input.wav')
            shutil.copy(path, f"{dest}\\")
        elif platform.system() == "Linux":
            path = os.path.join(os.getcwd(), 'cache/', 'voice_input.wav')
            shutil.copy(path, f"{dest}")
        sg.PopupQuick("Copied!")
        if os.path.exists(os.path.join(dest, 'csgo', 'cfg', 'csdj.cfg')) == False:
            shutil.copy(f'{os.path.join(os.getcwd(),"csdj.cfg")}',
                        f"{os.path.join(dest,'csgo','cfg')}")
        cfg.close()
    except FileNotFoundError:  # File does not exist!
        dest = ''
        # Adding(Trying to add default path):
        if platform.system() == "Windows":
            if os.path.isdir(os.path.join("C:\\", "Program Files (x86)", "Steam", "steamapps", "common", "Counter-Strike Global Offensive")) == True:
                dest = os.path.join("C:\\", "Program Files (x86)", "Steam",
                                    "steamapps", "common", "Counter-Strike Global Offensive")
            elif os.path.isdir(os.path.join("C:\\", "Program Files", "Steam", "steamapps", "common", "Counter-Strike Global Offensive")) == True:
                dest = os.path.join("C:\\", "Program Files", "Steam",
                                    "steamapps", "common", "Counter-Strike Global Offensive")
        elif platform.system() == "Linux":
            if os.path.isdir(os.path.join(os.path.expanduser("~"), ".steam", "steam", "steamapps", "common", "Counter-Strike Global Offensive")) == True:
                dest = os.path.join(os.path.expanduser(
                    "~"), ".steam", "steam", "steamapps", "common", "Counter-Strike Global Offensive")
        if dest == '':
            dest = sg.popup_get_text("Enter your CSGO install dir : ")
        cfg = open('csdir.cfg', 'w')
        cfg.write(dest)
        if platform.system() == 'Windows':
            path = os.path.join(os.getcwd(), 'cache\\', 'voice_input.wav')
            shutil.copy(path, f"{dest}\\")
        elif platform.system() == "Linux":
            path = os.path.join(os.getcwd(), 'cache/', 'voice_input.wav')
            shutil.copy(path, f"{dest}")
        sg.PopupQuick("Copied!")
        if os.path.exists(os.path.join(dest, 'csgo', 'cfg', 'csdj.cfg')) == False:
            shutil.copy(f'{os.path.join(os.getcwd(),"csdj.cfg")}',
                        f"{os.path.join(dest,'csgo','cfg')}")
        cfg.close()


def layoutbuild():
    layout = []
    for i in os.listdir(os.path.join(os.getcwd(), 'cache')):
        name = i.replace(".webm", '')
        if i not in ['.gitkeep', 'voice_input.wav']:
            layout.append(name)
    return layout


layout = [[sg.Text("Select from available songs or add from YouTube : ")], [sg.Listbox(
    values=layoutbuild(), size=(40, 2*len(layoutbuild())), enable_events=True, key="-FILES-")]]
sg.theme('Dark Blue 14')
layout.append([sg.HSeparator()])
layout.append([sg.Button("Add from YouTube", key='yt')])
window = sg.Window('CSDJ', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == 'yt':
        song = sg.popup_get_text("Enter the song name : ")
        download(song)
        movetodir(song)
        sg.popup_ok(f"{song} successfully downloaded and copied!")
        window['-FILES-'].update(layoutbuild())
    elif event == '-FILES-':
        movetodir(values['-FILES-'][0])
window.close()
