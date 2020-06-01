import paramiko
import pymongo

ip = '172.17.0.2'
username = 'sp'
password = 'sp123#'
port = '22'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(ip,port,username,password)
stdin,stdout,stderr=ssh.exec_command("ifconfig")
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)
print('hii')