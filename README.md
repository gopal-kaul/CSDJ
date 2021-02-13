# CSDJ - The Open Source Music Player for Source based Games!
![Github All Releases](https://img.shields.io/github/issues/gopal-kaul/CSDJ) ![Github All Releases](https://img.shields.io/github/forks/gopal-kaul/CSDJ) ![Github All Releases](https://img.shields.io/github/stars/gopal-kaul/CSDJ) ![Github All Releases](https://img.shields.io/github/downloads/gopal-kaul/CSDJ/total.svg)
### A Music Player for Source based games like CSGO, HL2 and others!

Head over to the releases page to grab it!
Pretty easy to use!

Features-
1. Direct Download Songs from YouTube by Name!
2. Songs get auto cached!
3. GUI(needs improvement!)

### Why did you make this?
Well, first of all, other projects like [SLAM](https://github.com/SilentSys/SLAM) and [csgoMP](https://github.com/stroopwafel1337/csgoMP) exist, but they are more or less dead. This will be supported for the forseeable future. This is nowhere as good as SLAM, as it still needs some features to be added!(Like selecting of songs using the console as in SLAM)

### How to Download?
Go to [CSDJ Releases](https://github.com/gopal-kaul/CSDJ/releases/latest) and download the appropriate version for your operating system. Or clone this repository and run the Python script.
To run the python script, do the following-
```
git clone https://github.com/gopal-kaul/CSDJ.git
cd CSDJ
pip install -r requirements.txt
python CSDJ.py
```

### How to use?
Just extract, run CSDJ.exe or ./csdj, and profit!
Enter the song name, it supports caching so you don't redownload it everytime.
I have added some automatic detection of default paths. If your path is not found, you may need to enter your CSGO install path.
It is usually the following-
 ```
 C:\Program Files(x86)\Steam\steamapps\common\Counter-Strike Global Offensive
 ```
 or
 ```
 /home/$USER/.steam/steamapps/common/Counter-Strike Global Offensive
 ```
 
 ### In Game
 Hit your console key. In console, type
 ```
 exec csdj
 ```
 to load CSDJ into CSGO.
 Next, while in-game, you can use '/' key to play music continuously or use ' key to push-to-play.
 ### Note-
 If the song ends, you need to press the '/' key again to use your microphone.
 
 ### Can I get a VAC Ban by using this?
 No. This does not run with CSGO nor does it interact with it, so you cannot get a VAC ban!
 
 ### My Anti Virus says your app might be a virus!
 It is a false positive. We are using system calls to copy files to your C: drive, thus some antivirus may detect it. We haven't obfuscated the code so that you can decompile the code to check out what happens under the hood!
 
 ### I have a feature request / a doubt / wanna meet the devs!
 [Join our Discord!](https://discord.gg/JZfhXuCw4J)
 
 ### Do you accept pull requests?
 Yes we do. Submit your pull request and we'll get back to it!
 
