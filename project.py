'''
每一行以；（中文分号）结尾
文末为断言，以。（中文句号）结尾
比如：标题应该为：软件测试_百度搜索。
定位与操作之间以，（中文分号）分开
比如：在id为：kw，文本框执行清空；
关键字
【基本】
进入网站：url路径
强制等待
【定位】
name为：name
classname为：classname
id为：id
tarname为：tarname
链接文字为：链接文字
链接部分文字为：链接部分文字
cssselector为：cssselector
xpath为：xpath
【操作】
点击；
清空；
提交；
输入：
【断言】
标题应该为：

'''


#!/usr/bin/env python
#coding:utf-8
import re
import codecs

#获取对象
def getElenument(line):
    mystr =""
    #如果存在“进入网站：url”产生语句“self.driver.get(url)”
    if ("进入网站：" in line):
        url = str(re.findall(r"进入网站：(.+?)；",line))[2:-2]
        mystr = "self.driver.get(\""+url+"\")"
    #如果存在“name为：XXX,”产生语句“self.find_element_by_id(XXX)”
    if ("name为：" in line):
        name = str(re.findall(r"name为：(.+?)，",line))[2:-2]
        mystr = "self.find_element_by_id(\""+name+"\")"
    #如果存在“classname为：XXX,”产生语句“self.driver.find_element_by_class_name(XXX)”
    if ("classname为：" in line):
        name = str(re.findall(r"name为：(.+?)，",line))[2:-2]
        mystr = "self.driver.find_element_by_class_name(\""+name+"\")"
    #如果存在“id为：XXX,”产生语句“self.driver.find_element_by_id(XXX)”
    if ("id为：" in line):
        name = str(re.findall(r"id为：(.+?)，",line))[2:-2]
        mystr = "self.driver.find_element_by_id(\""+name+"\")"
    #如果存在“tarname为：XXX,”产生语句“self.driver.find_element_by_tag_name(XXX)”
    if ("tarname为：" in line):
        name = str(re.findall(r"tarname为：(.+?)，",line))[2:-2]
        mystr = "self.driver.find_element_by_tag_name(\""+name+"\")"
    #如果存在“链接文字为：XXX,”产生语句“self.driver.find_element_by_link_text(XXX)”
    if ("链接文字为：" in line):
        name = str(re.findall(r"链接文字为：(.+?)，",line))[2:-2]
        mystr = "self.driver.find_element_by_link_text(\""+name+"\")"
    #如果存在“链接部分文字为：XXX,”产生语句“self.driver.find_element_by_partial_link_text(XXX)”
    if ("链接部分文字为：" in line):
        name = str(re.findall(r"链接部分文字为：(.+?)，",line))[2:-2]
        mystr = "self.driver.find_element_by_partial_link_text(\""+name+"\")"
    #如果存在“cssselector为：XXX,”产生语句“self.driver.find_element_by_css_selector(XXX)”
    if ("cssselector为：" in line):
        name = str(re.findall(r"cssselector为：(.+?)，",line))[2:-2]
        mystr = "self.driver.find_element_by_css_selector(\""+name+"\")"
    #如果存在“cssselector为：XXX,”产生语句“self.driver.find_element_by_xpath(XXX)”
    if ("xpath为：" in line):
        name = str(re.findall(r"xpath为(.+?)，",line))[2:-2]
        mystr = "self.driver.find_element_by_xpath(\""+name+"\")"
    #如果存在“强制等待X秒；”产生语句“time.sleep(X)”
    if ("强制等待" in line):
        sec = str(re.findall(r"强制等待(.+?)秒；",line))[2:-2]
        mystr = "time.sleep("+sec+")"    
    return action(line,mystr)

#进行操作
def action(line,mystr):
    #如果存在“点击；”产生语句“.click()”
    if("点击；" in line):
        mystr = mystr+".click()"
    #如果存在“清空；”产生语句“.clear()”
    if("清空；" in line):
        mystr = mystr+".clear()"
    #如果存在“提交；”产生语句“.submit()”
    if("提交；" in line):
        mystr = mystr+".submit()"
    #如果存在“输入：XXX；”产生语句“.send_keys("XXX")”
    if("输入：" in line):
        word = str(re.findall(r"输入：(.+?)；",line))[2:-2]
        mystr = mystr+".send_keys(\""+word+"\")"
    return mystr

#进行断言
def myassert(line):
    #如果存在“标题应该为：”产生语句“.click()”
    mystr =""
    if("标题应该为：" in line):
        word = str(re.findall(r"标题应该为：(.+?)。",line))[2:-2]
        mystr = "self.assertEqual(self.driver.title,\""+word+"\")"
    return mystr

#读模板文件
def readfile(file,line):
    f2 = open(file,"r")
    line=f2.read()
    f2.close()
    line = line.replace('+++1',txt)
    return line

#写入文件
def writefile(file,mystr):
    f3=codecs.open(file,"w",encoding='utf8')
    f3.write(mystr)
    f3.close()
            
if __name__=='__main__':
    #从文本中读入缺陷报告，存在bugReport字段中
    f1=codecs.open("bugReport.txt",encoding='utf8') 
    txt=""
    for line in f1:
        #进行匹配
        txt=txt+"\t\t"+getElenument(line)+"\n"
        ast = myassert(line)
        if not (ast) =="":
            txt = txt[:-1]
            txt = txt+myassert(line)         
    f1.close()
    #读入unittest的测试文件模板
    line = readfile("model.py",line)
    #写入py文件
    writefile("test.py",line)
    
    


