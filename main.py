from setup import *
import os

ed = ED()
print("code by Mubashir Ali")
while True:
    menu  = input("\nSelect option : \n[1] Encrypter \n[2] Decrypter \n[3] Exit\nSelect : ")
    if menu == "1" :
       
        user = str(input("\n[+] Enter text to encrypt : "))
        os.system("cls")
        print(f"text:{user}")
        ed.encrypter(user)
        
        continue
    elif menu == "2":
        user = str(input("\n[+] Enter text to decrypt : "))
        os.system("cls")
        print(f"encoded:{user}")
        ed.decrypter(user)
        continue
    elif menu == "3":
        break
    else:
        print("select valid option!")
        continue
