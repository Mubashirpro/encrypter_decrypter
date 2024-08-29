try:
    from colorama import Fore
    import base64
    import os
    import requests
    mods = ["colorama","base64"]
    if ImportError:
       if not requests.ConnectionError:
        for i in mods:
            os.system(f"pip install {i}")  
       else:
           print("Connection failed!")
    os.system("cls") 

            

except:
    print(":(")
red,green,cyan,lime,yellow = Fore.RED,Fore.GREEN,Fore.CYAN,Fore.LIGHTGREEN_EX,Fore.YELLOW
#J5VQ====
class ED:

    
    def __init__(self):
       
        title = """ << CODE BY MUBASHIR >> """
        print(yellow,title)
    def encrypter(self,string):
        string = string.encode()
        enc = base64.b32encode(string)
        print(cyan,f"\nEncrypted : {enc.decode()}")
    def decrypter(self,encrypted):
        decrypted = base64.b32decode(encrypted)
        print(lime,f"\nDecrypted : {decrypted.decode()}")
    
if __name__ == "__main__":
    ed = ED()
   
