# dumpPakKey [tool] [win64] for dumping *.pak base64 key for Unreal Engine 4

**1st** you need to download fresh python for Windows -> [Python/Releases](https://www.python.org/downloads/release) and install it

**[ ! ]** don't forget to check (include to PATH) option in checkbox, then open cmd (Win+R type cmd, Enter) and type:
```
pip install pyinstaller
```
after successful install, in your cmd type:
```
pyinstaller dumpPakKey.py -F 
```
**[ ! ]** make sure you are at the same directory where [dumpPakKey.py](https://raw.githubusercontent.com/somethingcoolmustbehere/dumpPakKey/master/dumpPakKey.py) is... 

**[ i ]** switch directory  in cmd.
```
cd \DirectoryName\dumpPakKey.py
```
after complition, check \Dist\ directory for your created *.exe
to run your (created with PyInstaller) *.exe open cmd , cd to path where your *.exe is and type the following: 
```
dumpPakKey.exe name_of_your_game-Shipping.exe
```

or just drag and drop your *.exe file on [dumpPakKey.exe](https://github.com/somethingcoolmustbehere/dumpPakKey/releases/download/unreal-engine-utilities/dumpPakKey.exe) it will automatically create Crypto.json for you.

then in cmd run:
```
UnrealPak.exe name_of_your_game-WindowsNoEditor.pak -cryptokeys=Crypto.json
```
or use [*.bat file](https://github.com/somethingcoolmustbehere/UnrealPakTool/blob/master/UnrealPakExtractCrypto.bat)

[UnrealPakTool](https://github.com/somethingcoolmustbehere/UnrealPakTool/releases/download/unreal-engine-utilities/UnrealPakTool.7z)

Have fun!)
![dumpPakKey](https://i.imgur.com/3db3AD3.png?1)
###### builded *.exe is here -> [dumpPakKey.exe](https://github.com/somethingcoolmustbehere/dumpPakKey/releases)

**NOTICE:** It was successfully tested in created (Shipping mode) projects in UE4 4.25.3

**NOTICE:** It was created "for science purposes only" in order to dump real life projects, you need to be shure they arent obfuscated by their loaders witch most of games have

**NOTICE:** Pattern used to find key section may change in other unreal engine build's, and you will need to manually change pattern, and rebuild *.py to *.exe
