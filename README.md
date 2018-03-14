# xidian_ids
抓取西电教务系统个人成绩并保存到本地

## 文件说明：
1. jw_xd.py  教务系统登录、个人成绩抓取、保存成绩到本地的操作
2. info.py 保存用户的用户名（学号）和密码
3. resources.py 保存教务系统站点中的几个主要的url

## 代码运行环境和使用到的第三方库

- 运行环境    
     本机测试环境 python 3.6.1（py2可能需要手动修改一些代码）

- 程序用到的库
     **re**  正则表达式库，py自带
     **os** 执行操作系统命令，py自带
     **requests** 做HTTP请求，在cmd目录下手动pip安装  `pip install requests`
     **xlwt** xls格式文件的读和写操作，同上pip安装 `pip install xlws`
     **lxml** 解析html标签， `pip install lxml`

## 后期打算
原本打算再加一个抢课功能，结果发现选课功能只在特定时间开放，等以后有机会再继续完善
