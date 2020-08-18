import re
import sys
import codecs
import binascii
import os
import pyperclip
import json

## Pattern section
initPattern = b'\x48\x8D\x41\x1F\xC7\x45\xD8'
junkPattern = ["c745d4", "488d411fc745d8", "c745dc",
    "c745e0", "c745e4", "c745e8", "c745ec"]
##

## Array section
offsetArray = []
dumpKeySectionList = []
##

## Error section
errorFile = "[!] Please provide a filename to proceed."
errorData = "[!] File specified doesn't exist, please proceed a valid file."
errorOffset = "[!] Something went wrong, no offset value has been set."
errorDumpKey = "[!] Something went wrong, can't dump bytes to array."
errorGenKey = "[!] Something went wrong, can't generate key."
errorCryptoData = "[!] Something went wrong, can't create Crypto.json file."
errorB64toBytes = "[!] Something went wrong, can't convert string to bytes."
##

## Function section


def incrementOffset(offset, jumpBytes):
    for i in range(0, jumpBytes):
        i = int(offset, 16)
        i += 1
        offset = hex(i)
        offsetArray.append(offset)


def decrementOffset(offset, jumpBytes):
    for i in range(0, jumpBytes):
        i = int(offset, 16)
        i -= 1
        offset = hex(i)
        offsetArray.append(offset)


def DumpKeyBlock():
    for offset in offsetArray:
        offset = int(offset, 16)
        f.seek(offset, 0)
        keyData = f.read(1)
        keyData = binascii.hexlify(keyData)
        dumpKeySectionList.append(keyData.decode('utf-8'))


def cleanGenKey(junkHex, hexBlock):
    cleanHex = hexBlock
    for trash in junkHex:
        cleanHex = re.sub(trash, '', cleanHex)

    print("[i] Pure [hex] key extracted: " + cleanHex)

    b64 = codecs.encode(codecs.decode(cleanHex, 'hex'), 'base64').decode()

    return b64

##


## argv contains data?!
if len(sys.argv) > 1:

    fileName = sys.argv[1]
    filePath = os.path.exists(fileName)

    ## Checking if file in argv exists, exec.
    if filePath:

        f = open(fileName, "rb")
        data = f.read()
        regex = re.compile(initPattern)
        for match_obj in regex.finditer(data):
            offset = match_obj.start()

            print("[i] Pattern match found, our initial offset is: " + hex(offset))

            offset = hex(offset)
            ## Add manualy initial offset to array
            offsetArray.append(offset)

            ## Getting offset section (where are key stored), up and down from initial match
            incrementOffset(offset, 45)
            decrementOffset(offset, 11)

            ## Sortnig your offsets by increase (dafault sort option)
            offsetArray.sort()

            print("[i] Retreaving key offset section.")
            print(*offsetArray)

        if offsetArray:
            DumpKeyBlock()
            f.close()

            print("[i] Retreaving key block section.")
            print(*dumpKeySectionList)
        else:

            print(errorDumpKey)

        if dumpKeySectionList:
            ## Generating base64 key from sorted HEX block
            hex = ''.join(dumpKeySectionList)
            ## Filtering junk from key block and Gen key
            b64 = cleanGenKey(junkPattern, hex).rstrip()

            print("[i] Base64 Decription *.pak key: " + b64)
        else:
            print(errorGenKey)
        ## Json pattern generation
        data = {}
        types = {}
        EncryptionKey = {}

        data['$types'] = types
        types['UnrealBuildTool.EncryptionAndSigning+CryptoSettings, UnrealBuildTool, Version=4.0.0.0, Culture=neutral, PublicKeyToken=null'] = "1"
        types['UnrealBuildTool.EncryptionAndSigning+EncryptionKey, UnrealBuildTool, Version=4.0.0.0, Culture=neutral, PublicKeyToken=null'] = "2"
        types['UnrealBuildTool.EncryptionAndSigning+SigningKeyPair, UnrealBuildTool, Version=4.0.0.0, Culture=neutral, PublicKeyToken=null'] = "3"
        types['UnrealBuildTool.EncryptionAndSigning+SigningKey, UnrealBuildTool, Version=4.0.0.0, Culture=neutral, PublicKeyToken=null'] = "4"
        data['$type'] = "1"
        data['EncryptionKey'] = EncryptionKey
        EncryptionKey['$type'] = "2"
        EncryptionKey['Name'] = "null"
        EncryptionKey['Guid'] = "null"
        EncryptionKey['Key'] = b64
        data['SigningKey'] = "null"
        data['bEnablePakSigning'] = "true"
        data['bEnablePakIndexEncryption'] = "true"
        data['bEnablePakIniEncryption'] = "true"
        data['bEnablePakUAssetEncryption'] = "true"
        data['bEnablePakFullAssetEncryption'] = "false"
        data['bDataCryptoRequired'] = "true"
        data['PakEncryptionRequired'] = "true"
        data['PakSigningRequired'] = "true"
        data['SecondaryEncryptionKeys'] = "[ ]"
        ##
        if b64:
                Crypto = open('Crypto.json', 'w', encoding='utf-8')
                json.dump(data, Crypto, ensure_ascii=False,
                          indent=4, sort_keys=True)
                Crypto.close()
                print(
                    "[i] Crypto.json was successfuly created with your dumped (Base64) key in it.")
                b64likebytes = str.encode(b64)
                if b64likebytes:
                    hexToClipboard = codecs.encode(codecs.decode(b64likebytes, 'base64'), 'hex').decode()
                    pyperclip.copy("0x" + hexToClipboard.upper())
                    print("[i] Raw [hex] key was added to your clipboard aka (Ctrl+V) where you want.")
                else:
                    print(errorB64toBytes)
        else:
            print(errorCryptoData)
    else:
        print(errorData)        
else:
    print(errorFile)
