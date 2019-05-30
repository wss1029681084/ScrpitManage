#!/usr/bin/python3
# -*- coding:utf-8 -*-

import xadmin
from demo import models
from xadmin.views.base import filter_hook

from django.apps import apps

from django.utils.encoding import  smart_text

from django.utils.text import capfirst

from collections import OrderedDict
from xadmin.util import  sortkeypicker

from xadmin import views


class GlobalSetting(object):
    # 设置后台顶部标题
    site_title = '诺亚易捷管理平台'
    # 设置后台底部标题
    site_footer = "COPYRIGHT © 2010 - 2018 ALL RIGHTS RESERVED"
    menu_style = "accordion"
    apps_icons = {"home": "fa fa-home", "products": "", "companyintroduction": "",
                  "certifications": "fa fa-certificate",
                  "contactus": "fa fa-phone", "forum": "", "logisticinformation": "",
                  "sourcedownload": "fa fa-download", "trade": "fa fa-shopping-cart", "users": "fa fa-user",
                  "wechatuser": "fa fa-user", "knowledgebase": "fa fa-book", "questionanswer": "fa fa-question-circle"}
    #以下方法重写，自定义菜单排序
    @filter_hook
    def get_nav_menu(self):
        site_menu = list(self.get_site_menu() or [])
        had_urls = []

        def get_url(menu, had_urls):
            if 'url' in menu:
                had_urls.append(menu['url'])
            if 'menus' in menu:
                for m in menu['menus']:
                    get_url(m, had_urls)

        get_url({'menus': site_menu}, had_urls)

        nav_menu = OrderedDict()

        menus_ = self.admin_site._registry.items()
        for model, model_admin in menus_:
            if getattr(model_admin, 'hidden_menu', False):
                continue
            app_label = model._meta.app_label
            app_icon = None
            model_dict = {
                'title': smart_text(capfirst(model._meta.verbose_name_plural)),
                'url': self.get_model_url(model, "changelist"),
                'icon': self.get_model_icon(model),
                'perm': self.get_model_perm(model, 'view'),
                'order': model_admin.order,
            }
            if model_dict['url'] in had_urls:
                continue

            app_key = "app:%s" % app_label
            if app_key in nav_menu:
                nav_menu[app_key]['menus'].append(model_dict)
            else:
                # Find app title
                app_title = smart_text(app_label.title())
                if app_label.lower() in self.apps_label_title:
                    app_title = self.apps_label_title[app_label.lower()]
                else:
                    appL = apps.get_app_config(app_label)
                    app_title = smart_text(apps.get_app_config(app_label).verbose_name)
                    # added by Fiona for menu ordering
                    if app_label == "auth":
                        app_index = len(menus_) - 1
                    elif app_label == "xadmin":
                        app_index = len(menus_) - 2
                    else:
                        app_index = appL.orderIndex_
                # find app icon
                if app_label.lower() in self.apps_icons:
                    app_icon = self.apps_icons[app_label.lower()]
                nav_menu[app_key] = {
                    "orderIndex": app_index,
                    'title': app_title,
                    'menus': [model_dict],
                }
            app_menu = nav_menu[app_key]
            if app_icon:
                app_menu['first_icon'] = app_icon
            elif ('first_icon' not in app_menu or
                          app_menu['first_icon'] == self.default_model_icon) and model_dict.get('icon'):
                app_menu['first_icon'] = model_dict['icon']

            if 'first_url' not in app_menu and model_dict.get('url'):
                app_menu['first_url'] = model_dict['url']

        for menu in nav_menu.values():
            menu['menus'].sort(key=sortkeypicker(['order', 'title']))

        nav_menu = list(nav_menu.values())
        # nav_menu.sort(key=lambda x: x['title'])
        # 左侧菜单自定义排序新增
        nav_menu.sort(key=sortkeypicker(['orderIndex']))
        site_menu.extend(nav_menu)
        return site_menu
    def get_site_menu(self):  # 名称不能改
        return [
            {
                'title': '平台运行',
                'icon': 'fa fa-bar-chart-o',
                'menus': (
                    {'title': '脚本执行',
                     'icon': 'fa fa-bar-chart-o',
                     'url': '/admin/Runscrpit'

                     },
                    {'title': '代码部署',
                     'icon': 'fa fa-bar-chart-o',
                     'url': '/admin/Publish'

                     },
                    {'title': '服务监控',
                     'icon': 'fa fa-bar-chart-o',
                     'url': '/admin/Monitor'

                     },

                )
            }

            ]


class BaseSetting(object):# 启用主题管理器   
    enable_themes =True# 使用主题   
    use_bootswatch =True# 注册主题设置
class Serveradmin(object):
    list_display =('server_name','hostname','username','passwd','port')
    list_editable =('server_name','hostname','username','passwd','port')


class Publishadmin(object):
    list_display =('Publish_name','script','host','param','type')
    #list_editable =('Publish_name','script')
class Envadmin(object):
    list_display = ('name', 'path', 'remarks', 'createTime')



xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)

xadmin.site.register(models.Publish,Publishadmin)
xadmin.site.register(models.Server,Serveradmin)
xadmin.site.register(models.Env,Envadmin)
from .views import ScriptView,MonitorView,PublishView
xadmin.site.register_view(r'Publish/$', PublishView, name='for_test')
xadmin.site.register_view(r'Runscrpit/$', ScriptView ,name='for_test1')
xadmin.site.register_view(r'Monitor/$', MonitorView ,name='for_test1')



