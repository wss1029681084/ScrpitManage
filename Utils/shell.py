#!/usr/bin/python
#-*- coding: UTF-8 -*-
# 定义一个类，表示一台远端linux主机

import paramiko,time,requests,json
from dwebsocket.decorators import accept_websocket, require_websocket
from demo import models

def xshell(host_id,cmd):
    data=models.Server.objects.filter(id=host_id).values()[0]
    hostname =data["hostname"]
    username = data["username"]
    password =data["passwd"]
    port = data["port"]

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, port=port, username=username, password=password,timeout=180)
    stdin, stdout, stderr = ssh.exec_command( cmd)


    return stdout.readlines()
    ssh.close()

def xshelllong(req,cmd,host_id):
    data = models.Server.objects.filter(id=host_id).values()[0]
    hostname = data["hostname"]
    username = data["username"]
    password = data["passwd"]
    port = data["port"]
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(cmd, get_pty=True)

    while stdout.readline():
        nextline = stdout.readline().strip()  # 读取脚本输出内容

        req.websocket.send(nextline.encode('utf-8'))  # 发送消息到客户端
        # 判断消息为空时,退出循环
    req.websocket.send('发布结束，部署成功！'.encode('utf-8'))






    ssh.close()  # 关闭ssh连接
def xshellapp(req,cmd):
    hostname = '10.21.62.170'
    username = 'app'
    password = 'app'
    port = 22
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(cmd, get_pty=True)

    while True:
        nextline = stdout.readline().strip()  # 读取脚本输出内容

        req.websocket.send(nextline.encode('utf-8'))  # 发送消息到客户端
        # 判断消息为空时,退出循环
        if  not nextline:
            req.websocket.send('发布结束，部署成功！'.encode('utf-8'))
            break

    ssh.close()  # 关闭ssh连接



def gettoken(mobile):

    cmd1= "| awk -F '\"' '{print $(NF-1) }'"
    #注意命令的空格
    date=time.strftime('%Y%m%d',time.localtime(time.time()))
    cmd="grep "+"'"+mobile[-4:]+"'"+" /home/app/multiple/200/logs/services_user_"+date+".log |grep 'token'| tail -1 "+cmd1
    print(cmd)
    a= xshell(cmd)
    '''
    d=list(a)
    print(d)
    print(type(d))
    print(d[0])
    dict=json.dump(d[0])

    token=dict.get("token",-1)
    '''
    return a[0]
def publish_rn(branch):
    #xshell("su app")

    cmd="bash /home/wss11416/test.sh "+str(branch)
    return xshelllong(cmd,)