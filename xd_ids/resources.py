# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 16:48:39 2017

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓     ┏┓
            ┏┛┻━━━━━┛┻━┓
            ┃    ☃    ┃
            ┃ ┳┛   ┗┳  ┃
            ┃    ┻     ┃
            ┗━┓      ┏━┛
              ┃      ┗━━┓
              ┃ 神兽保佑 ┣┓
              ┃ 永无BUG！┏┛
              ┗┓┓┏━━┳┓┏━┛
               ┃┫┫  ┃┫┫
               ┗┻┛  ┗┻┛
@author: wen
"""
base_url = 'http://jwxt.xidian.edu.cn/'

#登录页面
login_url = 'http://ids.xidian.edu.cn/authserver/login?service=http%3A%2F%2Fjwxt.xidian.edu.cn%2Fcaslogin.jsp'

#欢迎网页
home_url = base_url+'caslogin.jsp'

#选课管理
select_class = base_url+"../xkAction.do"
result_of_select = base_url+'../xkAction.do?actionType=6'
drop_class = base_url+'../xkAction.do?actionType=7'
invaild_result = base_url+'../xkAction.do?actionType=16'
course_timetable = base_url+'../xkAction.do?actionType=6'

#教学评估
teaching_evaluation = base_url+'../jxpgXsAction.do?oper=listWj'

#班级课表
class_timetable = base_url+'../bjkbcxAction.do?oper=bjkb_lb'

#成绩查询
grade_url = base_url+'gradeLnAllAction.do?type=ln&oper=qbinfo&lnxndm=2015-2016学年第一学期(两学期)#2015-2016学年第一学期(两学期)'

header_post={
            "Host": "ids.xidian.edu.cn",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "http://ids.xidian.edu.cn/authserver/login?service=http%3A%2F%2Fjwxt.xidian.edu.cn%2Fcaslogin.jsp"
            }

