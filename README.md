![](https://github.com/wss1029681084/ScrpitManage/blob/master/screenshots/%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE.png?raw=true)
![](https://github.com/wss1029681084/ScrpitManage/blob/master/screenshots/%E8%84%9A%E6%9C%AC%E6%89%A7%E8%A1%8C.png?raw=true)
![](https://github.com/wss1029681084/ScrpitManage/blob/master/screenshots/%E8%84%9A%E6%9C%AC%E9%85%8D%E7%BD%AE.png?raw=true)
![](https://github.com/wss1029681084/ScrpitManage/blob/master/screenshots/%E8%B4%A6%E5%8F%B7%E9%85%8D%E7%BD%AE.png?raw=true)

# 目的

  日常项目测试中，总是在不停的敲linux命令，切换目录，执行脚本。比如获取短信验证码，为了某个场景去执行某个脚本，甚至于测试环境的更新部署。这些都需要不停的敲打linux命令，有时候忘记路径和脚本，还要专门去找资料。非常浪费时间。 如果有个平台可以把这些管理起来就好了。但是一般的中小型团队是没有测试开发的，所以这个想法无从实施。
# 用法
   账号配置：配置了连接的服务器的ip，账号，密码，端口（在这个服务器里执行脚本）<br>
   环境配置;比如公司有3套环境，发送push的脚本在3套环境都有，执行的路径分别是<br>
   /home/app/multiple/100/go_src/src/cfds<br>
   /home/app/multiple/200/go_src/src/cfds<br>
   /home/app/multiple/300/go_src/src/cfds<br>
   我们把/home/app/multiple/100/；/home/app/multiple/200/；/home/app/multiple/300/提取出来作为环境的路径，剩下的所有环境下相同的路径部分作为脚本<br>
   脚本配置：把环境配置里截取的剩下的放到脚本里，这样就可以只需配置一个脚本，在不同环境里运行时，运用下拉框的形式选择，组合拼接后执行。<br>
###   原理就是在界面上配置好要执行脚本各个部分，传递到后端拼接成一个完整的要执行的脚本，然后paramiko远程连接服务器去执行脚本，返回结果再显示在网页上。
# 例子
  通过在脚本配置里配置脚本的名称，要执行的脚本，传的参数等，配置成功后显示在对应的页面。<br>
如：./gettoekn --mobile=18656560106,需要写成./gettoekn --mobile=CMD；然后执行时在页面上输入的手机号，传到后端，执行命令时自动替换掉CMD<br>
对于这种类似于多个传参的：./cli_push -clientid=1 -uid=10086 -type=3 ,（根据ios/Android，用户uid，push的类型），就写成./cli_push CMD，页面上的传的参数是-clientid=1 -uid=10086 -type=3。如果脚本不需要传递参数，也可以直接./cli_push CMD，界面上不填写，这样就是一个“”替换了CMD,对所有类型所有用户发送push.

![](https://testerhome.com/uploads/photo/2019/7128d47c-5a3f-4a95-8e8f-4a41101bea54.png!large)
其他如服务部署功能，监控功能类似以上
![](https://testerhome.com/uploads/photo/2019/736bdcfe-9396-4e87-a74d-521bfda04f98.png!large)
# 部署安装：
基于python3，Django2，xadmin2<br>
1.进入项目根目录：pip install -r requirements（xadmin2会pip失败，请参考https://blog.csdn.net/yuhan963/article/details/79091248）<br>
2.python manage.py makemigrations <br>
3.python manage.py migrate<br>
4.python manage.py createsuperuser<br>
5.python manage.py runserver 0.0.0.0:8000<br>
因为上传的github里包含我之前使用的sqlite3，所以也可以跳过2,3,4步骤。<br>