# ScrpitManage<br>
为中小测试团队，尤其是服务端测试较多的同学专门设计~~<br>
初衷：<br>
日常项目测试中，总是在不停的敲linux命令，切换目录，执行脚本。比如获取短信验证码，为了某个场景去执行某个脚本，甚至于测试环境的更新部署。这些都需要不停的敲打linux命令，有时候忘记路径和脚本，还要专门去找资料。非常浪费时间。 如果有个平台可以把这些管理起来就好了。但是一般的中小型团队是没有测试开发的，所以这个想法无从实施。<br>





通过在脚本配置里配置脚本的名称，要执行的脚本，传的参数等，配置成功后显示在对应的页面。<br>
如：./gettoekn --mobile=18656560106,需要写成./gettoekn --mobile=CMD；然后执行时在页面上输入的手机号，传到后端，执行命令时自动替换掉CMD
对于这种类似于多个传参的：./cli_push -clientid=1 -uid=10086 -type=3 ,（根据ios/Android，用户uid，push的类型），就写成./cli_push CMD，页面上的传的参数是-clientid=1 -uid=10086 -type=3。如果脚本不需要传递参数，也可以直接./cli_push CMD，界面上不填写，这样就是一个“”替换了CMD,对所有类型所有用户发送push.<br>


另外：<br>
该平台还支持在发布菜单页里，配置服务监控和代码部署。其中代码部署运用websocket，实时显示服务端部署日志。当然，现在很多公司都有自己的代码部署平台，或者如jenkins上持续集成完成部署。这个功能稍微多余，但适用于没有自己的部署平台的团队。<br>




部署安装：<br>
基于python3，Django2，xadmin2<br>
1.进入项目根目录：pip install -r requirements（xadmin2会pip失败，请参考https://blog.csdn.net/yuhan963/article/details/79091248）<br>
2.python manage.py makemigrations <br>
3.python manage.py migrate<br>
4.python manage.py createsuperuser<br>
5.python manage.py runserver 0.0.0.0:8000<br>
因为上传的github里包含我之前使用的sqlite3，所以也可以跳过2,3,4步骤。<br>
