# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 20:42:26 2017

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

import re
import requests
import xlwt
import os

from resources import *
from info import *

def get_hidden(html):
    p_lt = r'<input type="hidden" name="lt" value="(.*?)"'
    lt = re.findall(p_lt,html)
    p_exec = r' <input type="hidden" name="execution" value="(.*?)"'
    execution = re.findall(p_exec,html)
    #print(lt,'\n',execution)
    return (lt[0], execution[0])

#此处只能传入一个 str 类型
def simplify_string(item):
    #print(item)
    try:
        tmp = item
        string = re.sub('\xa0',' ',item)
        string = re.sub('[\r\n\t：:]','',string).strip()
        return string
    except:
        print('[****]error ',tmp)
    #print(string)
    
#只能传入一个含有多个字符串的 list（只能有一层嵌套）
def simplify_list(item):
    if type(item) == list:
        for i in range(len(item)):
            item[i] = simplify_string(item[i])
        return item
    else:
        print('not a list, please try again!')

def write_line(table, row_index, column_index, item):
    assert type(item) == list
    for i in item:
        table.write(row_index,column_index,i)
        column_index += 1

def get_type(s):
    s = str(s)
    try:
        x = eval(s)
        return type(x)
    except:
        return type(s)
          
class xd_ids:
    
    def __init__(self, Sno, passwd):
        self.username = Sno
        self.password = passwd
        self.session = requests.session()
        
    def login(self):
        html = self.session.get(login_url).content.decode('utf-8')
        (lt,execution) = get_hidden(html)
        payload = {
                "username":self.username,
                "password":self.password,
                "submit":"",
                "lt":lt,
                "execution":execution,
                "_eventId":"submit",
                "rmShown":"1"
                    }
        s = self.session.post(login_url, data=payload, headers=header_post)
        s = self.session.get(home_url)
        if "学分制综合教务" in s.text:
            print('successfully login!')
            return True
        else:
            print('login failed, try again!')
            print(s.content.decode('gbk'))
            return False
    
    def parse_info(self, grade_page):
        from lxml import etree
        
        assert "成绩" in grade_page
        root = etree.HTML(grade_page)
        item_list = root.xpath('//a/@name')  #获取学期信息
        #print(item_list)
        grade_list = []
        title_list = []
        tail_list = []
        for i in range(len(item_list)):
            title = root.xpath('/html/body/table[4*(%d)]//thead/tr/th/text()' % (i+1))
            #print(title)
            title_list.append(title)
            num_of_courses = len(root.xpath('/html/body/table[4*(%d)]//table[1]/tr' % (i+1)))
            course_list = []
            for j in range(num_of_courses):
                course = root.xpath('/html/body/table[4*(%d)]//table[1]/tr[%d]//*/text()' % (i+1, j+1))
                del(course[6])
                del(course[-1])
                #print(course)
                course_list.append(course)
            grade_list.append(course_list)
            tail = root.xpath('/html/body/table[4*(%d)]//table[2]/tr/*/text()' % (i+1))
            #print(tail)
            tail_list.append(tail)
        return (item_list, title_list, grade_list,tail_list)

    def save_grade(self):
        grade_page = self.session.get(grade_url).text
        #print(grade_page)
        (item_list, title_list, grade_list, tail_list) = self.parse_info(grade_page)
        '''
        print(item_list)
        print(title_list[0])
        print(grade_list[0][0])
        print(tail_list[0])
        '''
        file = xlwt.Workbook()
        table = file.add_sheet('grade')
        row_index = 0
        column_index = 0
        
        table.col(0).width = 256*30
        for i in range(1,12):
            table.col(i).width = 256*10
        
        total_grades = 0
        total_credit = 0
        
        for i in range(len(item_list)):
            table.write(row_index,column_index,item_list[i])
            row_index += 1
            
            title_list[i] = simplify_list(title_list[i])
            write_line(table, row_index, 1, title_list[i])
            row_index += 1
            
            sum_grades = 0
            sum_credit = 0
        
            for j in range(len(grade_list[i])):
                grade_list[i][j] = simplify_list(grade_list[i][j])
                if get_type(grade_list[i][j][-1])==float and\
                (grade_list[i][j][5]=='必修' or grade_list[i][j][5]=='学院选修') and\
                '国家英语' not in grade_list[i][j][2]:
                    credit = float(grade_list[i][j][4])
                    grade = float(grade_list[i][j][-1])
                    sum_credit += credit
                    sum_grades += grade*credit
                write_line(table, row_index, 1, grade_list[i][j])
                row_index+=1
                
            tail_list[i] = simplify_list(tail_list[i])
            write_line(table, row_index, 0, tail_list[i])
            row_index += 1
            
            total_credit += sum_credit
            total_grades += sum_grades
            
            weight_ave = sum_grades / sum_credit
            table.write(row_index, 0, '加权平均')
            table.write(row_index,1,weight_ave)
            row_index += 2
            
        
        table.write(row_index, 0, '加权平均')
        table.write(row_index,1,total_grades/total_credit)
        row_index += 1
        
        file.save('./grade.xls')
        path = os.getcwd()+'\\grade.xls'
        print('file has been saved in ',path)
        '''
        print(item_list)
        print(title_list)
        print(grade_list)
        print(tail_list)
        '''
       # print(grade_list[1][1])
        
        
        return (item_list, title_list, grade_list, tail_list)
        #print(grade_page)
        
        
if __name__ == '__main__':
    #test = xd_ids("15030188006", "101515")
    test = xd_ids(username,password)
    if test.login():
        #page = test.save_grade()
        '''
        f = open('./page.html','w')
        f.write(page)
        f.close()
        '''
        (item_list, title_list, grade_list, tail_list) = test.save_grade()
        
        