# Bitcoin-Virus
Bitcoin wallet address swapper (Python3)  
This script waits for any text to be copied to clipboards victim, validates and returns wether the copied text is a valid bitcoin address or not, and if valid, swaps the copied bitcoin address by any custom address (replace on line 31 in virus.py -> pyperclip.copy('{your btc address}')).  

##### WARNING  
This script ouhgt to be used for educational purpose only, I'm not responsible for any misuse.


## Modules used  
* pyperclip==1.8.0  
* base58==2.0.0  
* Module installation:
```
pip3 install -r requirements.txt
```

