#!/usr/bin/python3
# -*- coding:utf-8 -*-
from demo import models


def gethostname():
    name=models.Server.objects.all().values("server_name")

    len(name)
    host=[[]]*len(name)
    n=1
    host.append(["test0","初始值"])
    for i in name:
        host.append(["test"+str(n),i])
        n=n+1
    return host

