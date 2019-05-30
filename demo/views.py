#!/usr/bin/python3
# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.template import Context
import os
from django.contrib.auth.decorators import login_required
from xadmin.views import CommAdminView
from demo import models
from Utils import shell
import re
from django.http import HttpResponse
from dwebsocket.decorators import accept_websocket

# Create your views here.
class ScriptView(CommAdminView):
    def get(self, request):


        title = "脚本执行"
        context = super().get_context()
        context["title"] = title
        context["breadcrumbs"].append({'url': '/admin/', 'title': title})
        context["content"]=models.Publish.objects.filter(type="RunScrpit").values()
        context["env"]=models.Env.objects.values()
        return render(request, "Runscrpit.html", context)


class PublishView(CommAdminView):
    def get(self, request):
        context = super().get_context()
        title = "代码部署"
        context["title"] = title
        context["breadcrumbs"].append({'url': '/admin/', 'title': title})
        context["content"] = models.Publish.objects.filter(type="CodePublish").values()
        context["env"] = models.Env.objects.values()
        return render(request, "publish.html", context)


class MonitorView(CommAdminView):
    def get(self, request):
        context = super().get_context()
        title = "服务监控"
        context["title"] = title
        context["breadcrumbs"].append({'url': '/admin/', 'title': title})
        context["content"] = models.Publish.objects.filter(type="Monitor").values()
        context["env"] = models.Env.objects.values()
        return render(request, "Monitor.html", context)
def runscript(request):
            key=request.GET['a']
            value=request.GET['b']
            print("-------"+value)
            id = re.findall("\d+", value)[0]
            hostid=models.Publish.objects.filter(id=id).values("host_id")[0]["host_id"]
            env=request.GET['c']
            path=models.Env.objects.filter(name=env).values()[0]["path"]
            script = models.Publish.objects.filter(id=id).values("script")[0]["script"]
            newscrpit =path+ str(script).replace("CMD", str(key))

            result=shell.xshell(hostid,newscrpit)
            if result !=[]:
                print(result)
                return HttpResponse(result)
            else:
                return HttpResponse("无记录，请检查脚本或参数是否正确")
@accept_websocket
def publish(request):
    print(1111)
    for messages in request.websocket:
        data = str(messages.decode().strip()).split(',')
        print(data)
        key=data[0]   #传的参数
        value=data[1]  #传的testid
        id = re.findall("\d+", value)[0]
        hostid = models.Publish.objects.filter(id=id).values("host_id")[0]["host_id"]
        env = data[2]
        path = models.Env.objects.filter(name=env).values()[0]["path"]
        script = models.Publish.objects.filter(id=id).values("script")[0]["script"]
        newscrpit = path+str(script).replace("CMD", str(key))
        print(newscrpit)
        shell.xshelllong(request, newscrpit,hostid)


def monitor(request):
    value = request.GET['b']
    print("-------" + value)
    id = re.findall("\d+", value)[0]
    hostid = models.Publish.objects.filter(id=id).values("host_id")[0]["host_id"]
    env = request.GET['c']
    path = models.Env.objects.filter(name=env).values()[0]["path"]
    script = models.Publish.objects.filter(id=id).values("script")[0]["script"]
    newscrpit = path + str(script)
    result = shell.xshell(hostid, newscrpit)
    if result != []:
        print(result)
        return HttpResponse(result)
    else:
        return HttpResponse("无记录，请检查脚本配置是否正确")