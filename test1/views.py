from django.http import HttpResponse
from django.shortcuts import render
import paramiko


import os


def ssh(request):
    ip = request.GET.get("ip")
    usr = request.GET.get("usr")
    pas = request.GET.get("pass")
    print(ip)
    print(usr)
    print(pas)  
    port = '22'
    
    ip = '172.17.0.2'
    username = 'sp'
    password = 'sp123#'
    port = '22'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(ip,port,usr,pas)
    stdin,stdout,stderr=ssh.exec_command("ip a")
    outputlines=stdout.readlines()
    resp=''.join(outputlines)
    print(resp)



    data = {"ip_add1":ip , "user":usr, "password":pas, "op":resp}
    
    

    return render(request,'ssh.html',data)




def about(request):
    return HttpResponse("about")   

def homepage(request):
    # return HttpResponse("homepage")   
    return render(request,'homepage.html')

def temp1(request):
    return render(request,'index.html')

def page2(request):
    text = request.GET.get('text','default')
    chk = request.GET.get('ck1','off')
    print(text)
    print(chk)
    
    str1 = {'name':text,'chkbox':chk}
    if chk == 'off':
        return HttpResponse("Please select checkbox")
    else:
        return render(request,'page2.html',str1)