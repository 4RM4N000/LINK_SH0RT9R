import sys
import time
import pyshorteners
username = "Arman"
password = "Arman098"

def end():
  arman = input()
  sys.exit()
  
  
def animated(logo):
  for x in logo:
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.05)
 

given_username = input("\u001b[34;1mEnter Your Username: ")
if given_username == username:
  print("\u001b[32;1mCorrect Username")
  given_password = input("\u001b[34;1mEnter Your Password: ")
  if given_password == password:
    print("\u001b[32;1mWelcome To This Tool")
  else:
    print("\u001b[31;1mWrong Password")
    time.sleep(1)
    print("Press enter to exit")
    end()
    
    
else:
  print("\u001b[31;1mWrong User")
  time.sleep(1)
  print("Press enter to exit")
  end()
logo = '''
\u001b[34;1m____  ____  _      ____  _     
/  _ \/  __\/ \__/|/  _ \/ \  /|
| / \||  \/|| |\/||| / \|| |\ ||
| |-|||    /| |  ||| |-||| | \||
\_/ \|\_/\_\\_/  \|\_/ \|\_/  \|
                                
'''
logo2 = " \u001b[32;1m________________________________"
animated(logo2)
animated(logo)
animated(logo2)




link = input("\u001b[33;1mEnter Your Link Here: ")
s = pyshorteners.Shortener()
provide = s.tinyurl.short(link)


print(f"Your sort link is : {provide}")