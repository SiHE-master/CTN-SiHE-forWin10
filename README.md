# CTN-SiHE-forWin10
Windows/autostart/DHU cable network

部署步骤：
1.下载整个程序文件夹后，把文件夹放到一个目录，如：D:\CTN-SiHE-forWin10。
2.安装Firefox浏览器。
3.在setting.txt文件中填上自己的上网账号，分别替换掉usrname和password即可。
4.运行ctn_forWin10.exe，测试是否能自动上网认证。如果已经连上了校园网，可以进入自助服务系统把当前设备下线（可以根据本机IP来判断下线哪一台，查看IP方法：cmd中输入ipconfig回车）。

开机自启服务设置：
1.以管理员权限启动cmd，cd到程序文件夹目录，nssm install <服务名称>，名称自定义，如nssm install ctn，回车，在弹出菜单的path里选择ctn_forWin10.exe的路径，然后点击install service即可。
2.完成上述步骤注册完服务后，win+R打开运行框，输入services.msc回车，打开本地服务列表，找到刚刚注册的服务名称，右键属性，启动类型为自动即可。

2021/1/16更新： 最近服务器搬迁，遇到Firefox无法跳转到认证界面的情况，把URL更改为 http://1.2.3.4/ 即可。
