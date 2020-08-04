## dumpPakKey [tool] [win64] for dumping *.pak base64 key for Unreal Engine 4

> Windows python pyinstaller to make an *.py exe 

- 1st you need to download fresh python for Windows

- https://www.python.org/downloads/release

- install it, dont forget to check (include to PATH) option in checkbox
- then open cmd and type:
- pip install pyinstaller
- after successful install

- type:
- pyinstaller dumpPakKey.py -F ## make sure you are at the same directory where dumpPakKey.py is... switch directory via cd (your_script_directory) in cmd.
- after complition, check dist directory for your created exe

- to run our baked *.exe open cmd , cd to path where your baked *.exe is
- then type dumpPakKey.exe name_of_your_game-Shipping.exe and copy key
- then add copied key to your Crypto.json
- open/edit Crypto.json
- in
```json
"EncryptionKey":
  {
      "$type":"2",
      "Name":"null",
      "Guid":"null",
      "Key":"Your Base64 key here"
  },
```
- "Your Base64 key here" paste your generated key (in the middle of " "), save file

- then in cmd run:

- UnrealPak.exe name_of_your_game-WindowsNoEditor.pak -cryptokeys=Crypto.json

- Have fun!)

## builded *.exe is here -> https://github.com/somethingcoolmustbehere/dumpPakKey/releases
> - NOTICE: It was successfully tested in created (Shipping mode) projects in UE4 4.25.3
> - NOTICE: It was created "for science purposes only" in order to dump real life projects, you need to be shure they arent obfuscated by their loaders witch most of games have
> - NOTICE: Pattern used to find key section may change in other unreal engine build's, and you will need to manually change pattern, and rebuild *.py to exe
