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
**[ i ]** copy your created key (Ctrl+C)

**[ i ]** then paste (Ctrl+V) your copied key to your [Crypto.json](https://raw.githubusercontent.com/somethingcoolmustbehere/UnrealPakTool/master/Crypto.json).

open/edit your [Crypto.json](https://raw.githubusercontent.com/somethingcoolmustbehere/UnrealPakTool/master/Crypto.json).

in EncryptionKey section of your [Crypto.json](https://raw.githubusercontent.com/somethingcoolmustbehere/UnrealPakTool/master/Crypto.json) file:
```json
"EncryptionKey":
  {
      "$type":"2",
      "Name":"null",
      "Guid":"null",
      "Key":"Your Base64 key here"
  },
```
"Your Base64 key here" paste your generated key (in the middle of " "), save file.

then in cmd run:
```
UnrealPak.exe name_of_your_game-WindowsNoEditor.pak -cryptokeys=Crypto.json
```
Have fun!)
![dumpPakKey](https://i.imgur.com/EzIsUQk.png)
###### builded *.exe is here -> [dumpPakKey.exe](https://github.com/somethingcoolmustbehere/dumpPakKey/releases)

**NOTICE:** It was successfully tested in created (Shipping mode) projects in UE4 4.25.3

**NOTICE:** It was created "for science purposes only" in order to dump real life projects, you need to be shure they arent obfuscated by their loaders witch most of games have

**NOTICE:** Pattern used to find key section may change in other unreal engine build's, and you will need to manually change pattern, and rebuild *.py to *.exe
