'''
(基本)
【进入网站“url路径”】
(定位)
【进入网站“url”】
【id为“XXX”】、【编号为“XXX”】
【name为“XXX”】、【名称为“XXX”】、【名为“XXX”】
【classname为“XXX”】、【class名为“XXX”】、【类名为“XXX”】
【tagname为“XXX”】、【tag名为“XXX”】、【标签名为“XXX”】
【tagname为“XXX”】、【tag名为“XXX”】、【标签名为“XXX”】
【链接文字为“XXX”】、【url文字为“XXX”】
【链接部分文字为“XXX”】、【url部分文字为“XXX”】、【URL部分文字为“XXX”】
【cssselector为“XXX”】、【css选择为“XXX”】
【xpath为“XXX”】
(操作)
【点击】
【清空】
【提交】
【输入“XXX”】
【强制等待X秒】
【切换表单到“XXX”】
【切换到默认表单】
【切换到新窗口并且关闭老窗口】
【切换到新窗口并且不关闭老窗口】
【执行js脚本“XXX”】
【确定弹出框】
【取消弹出框】
【获取弹窗框里面的文字】
【属性为“XXX”的文字】
【设置名为“XXX”的cookie，值为“YYY”】
【移动元素到...的位置】
【获取HTML5 Viedo】
【获取HTML5 Viedo url】
【执行HTML5 Viedo 播放操作】
【执行HTML5 Viedo 停止操作】
【执行HTML5 Viedo 暂停操作】
【存储变量为“XXX”】
【获取下拉条】
【选择可见文字为“XXX”下拉条】
【选择值为“XXX”的下拉条】
【选择序号为“XXX”的下拉条】
【如果“XXX”被选择】
【如果“XXX”没被选择】
【那么“XXX”】
【判断...被选中】
【判断...没有被选中】
(断言)
【标题应该为“XXX”】
【标题应该包含“XXX”】
【网页路径应该为“XXX”】、【网页url应该为“XXX”】
【返回值与“XXX”相同】
【返回值“XXX”在返回结果中存在】
【判断元素XXX是否被选中】
【判断元素XXX是否没有被选中】

'''


#!/usr/bin/env python
#coding:utf-8
import re
import codecs
#初始化
def init(line):
    line = line.replace("选取","选择")
    line = line.replace("url","URL")
    return line

#获取对象
def getElenument(line):
    mystr =""
    line = init(line)
    #如果存在【进入网站“url”】产生语句“self.driver.get(url)”
    if ("进入网站“") in line:
        url = str(re.findall(r"进入网站“(.+?)”",line))[2:-2]
        mystr = "self.driver.get(\""+url+"\")"
     #如果存在【id为“XXX”】或【编号为“XXX”】产生语句“self.driver.find_element_by_id(XXX)”
    if ("id为“" in line) or ("编号为“" in line):
        name = str(re.findall(r"id为“(.+?)”",line))[2:-2]
        if len(name)==0:
            name = str(re.findall(r"编号为“(.+?)”",line))[2:-2]
        mystr = "self.driver.find_element_by_id(\""+name+"\")"
    #如果存在【name为“XXX”】或【名称为“XXX”】或【名为“XXX”】产生语句“self.find_element_by_id(XXX)”
    if ("name为“" in line) or ("名称为“" in line) or ("名为“" in line):
        name = str(re.findall(r"name为“(.+?)”",line))[2:-2]
        if len(name)==0:
            name = str(re.findall(r"名称为“(.+?)”",line))[2:-2]
        if len(name)==0:
            name = str(re.findall(r"名为“(.+?)”",line))[2:-2]
        mystr = "self.driver.find_element_by_name(\""+name+"\")"
    #如果存在【classname为“XXX”】或【class名为“XXX”】或【类名为“XXX”】产生语句“self.driver.find_element_by_class_name(XXX)”
    if ("classname为“" in line) or ("class名为“" in line) or ("类名为“" in line):
        name = str(re.findall(r"classname为“(.+?)”",line))[2:-2]
        if len(name)==0:
            name = str(re.findall(r"class名为“(.+?)”",line))[2:-2]
        if len(name)==0:
            name = str(re.findall(r"类名为“(.+?)”",line))[2:-2]
        mystr = "self.driver.find_element_by_class_name(\""+name+"\")"
    #如果存在【tagname为“XXX”】或【tag名为“XXX”】或【标签名为“XXX”】产生语句“self.driver.find_element_by_tag_name(XXX)”
    if ("tagname为“" in line) or ("tag名为“" in line) or ("标签名为“" in line):
        name = str(re.findall(r"tagname为“(.+?)”",line))[2:-2]
        if len(name)==0:
            name = str(re.findall(r"tag名为“(.+?)”",line))[2:-2]
        if len(name)==0:
            name = str(re.findall(r"标签名为“(.+?)”",line))[2:-2]
        mystr = "self.driver.find_element_by_tag_name(\""+name+"\")"
    #如果存在【链接文字为“XXX”】或【url文字为“XXX”】或【URL文字为“XXX”】产生语句“self.driver.find_element_by_link_text(XXX)”
    if ("链接文字为“" in line) or ("url文字为“" in line) or ("URL文字为“" in line):
        name = str(re.findall(r"链接文字为“(.+?)”",line))[2:-2]
        if len(name)==0:
            name = str(re.findall(r"url文字为“(.+?)”",line))[2:-2]
        if len(name)==0:
            name = str(re.findall(r"URL文字为“(.+?)”",line))[2:-2]
        mystr = "self.driver.find_element_by_link_text(\""+name+"\")"
    #如果存在【链接部分文字为“XXX”】或【url部分文字为“XXX”】产生语句“self.driver.find_element_by_partial_link_text(XXX)”
    if ("链接部分文字为“" in line) or("链接部分文字为“" in line) or ("链接部分文字为“" in line):
        name = str(re.findall(r"链接部分文字为“(.+?)”",line))[2:-2]
        if len(name)==0:
            name = str(re.findall(r"url部分文字为“(.+?)”",line))[2:-2]
        mystr = "self.driver.find_element_by_partial_link_text(\""+name+"\")"
    #如果存在【cssselector为“XXX”】或【css选择为“XXX”】产生语句“self.driver.find_element_by_css_selector(XXX)”
    if ("cssselector为“" in line) or ("css选择为“" in line):
        name = str(re.findall(r"cssselector为“(.+?)”",line))[2:-2]
        if len(name)==0:
            name = str(re.findall(r"css选择为“(.+?)”",line))[2:-2]
        mystr = "self.driver.find_element_by_css_selector(\""+name+"\")"
    #如果存在【xpath为“XXX”】产生语句“self.driver.find_element_by_xpath(XXX)”
    if ("xpath为“" in line):
        name = str(re.findall(r"xpath为“(.+?)”",line))[2:-2]
        mystr = "self.driver.find_element_by_xpath(\""+name+"\")"
    return action(line,mystr)

#进行操作
def action(line,mystr):
    #如果存在【点击】产生语句“.click()”
    if("点击" in line):
        mystr = mystr+".click()"
    #如果存在【清空】产生语句“.clear()”
    if("清空" in line):
        mystr = mystr+".clear()"
    #如果存在【提交】产生语句“.submit()”
    if("提交" in line):
        mystr = mystr+".submit()"
     #如果存在【输入“XXX”】产生语句“.send_keys("XXX")”
    if("输入" in line):
        name = str(re.findall(r"输入“(.+?)”",line))[2:-2]
        mystr = mystr+".send_keys(\""+name+"\")"
    #如果存在【强制等待X秒】”产生语句“time.sleep(X)”
    if ("强制等待" in line):
        sec = str(re.findall(r"强制等待(.+?)秒",line))[2:-2]
        mystr = "time.sleep("+sec+")"
    #如果存在“【如果“XXX”被选择】”产生语句“if XXX.is_selected():”
    if ("如果“" in line) and ("”被选择" in line):
        name = str(re.findall(r"如果“(.+?)”被选择",line))[2:-2]
        mystr = "if "+name+".is_selected():"
    #如果存在“【如果“XXX”没被选择】”产生语句“if not XXX.is_selected():”
    if ("如果“" in line) and ("”没被选择" in line):
        name = str(re.findall(r"如果“(.+?)”没被选择",line))[2:-2]
        mystr = "if not "+name+".is_selected():"
    #如果存在“【那么“XXX”】”产生语句“\tXXX”
    if ("那么“" in line) :
        name = str(re.findall(r"那么“(.+?)”",line))[2:-2]
        mystr = "\t"+name+mystr
    #如果存在“【切换表单到“XXX”】”产生语句“self.driver.switch_to.frame(XXX)”
    if ("切换表单到" in line):
        name = str(re.findall(r"切换表单到“(.+?)”",line))[2:-2]
        mystr = "self.driver.switch_to.frame(\""+name+"\")"
    #如果存在【切换到默认表单】”产生语句“self.driver.switch_to.default_content()”
    if ("切换到默认表单" in line):
        mystr = "self.driver.switch_to.default_content()"
    #如果存在【切换到新窗口并且关闭老窗口】”产生语句“.....”
    if("切换到新窗口并且关闭老窗口" in line):
        mystr = mystr+"current_windows = self.driver.current_window_handle\n\t\tall_handles = self.driver.window_handles\n\t\t"
        mystr = mystr+"for handle in all_handles:\n\t\t\tif handle != current_windows:\n\t\t\t\tself.driver.switch_to.window(handle)\n\t\t\t\tbreak\n\t\t"
        mystr = mystr+"for handle in all_handles:\n\t\t\tif handle == current_windows:\n\t\t\t\tself.driver.switch_to.window(handle)\n\t\t\t\tself.driver.close()\n\t\t\t\tbreak\n\t\t"
        mystr = mystr+"for handle in all_handles:\n\t\t\tif handle != current_windows:\n\t\t\t\tself.driver.switch_to.window(handle)\n\t\t\t\tbreak"
    #如果存在【切换到新窗口并且不关闭老窗口】产生语句“.....”
    if("切换到新窗口并且不关闭老窗口" in line):
        mystr = mystr+"current_windows = self.driver.current_window_handle\n\t\tall_handles = self.driver.window_handles\n\t\t"
        mystr = mystr+"for handle in all_handles:\n\t\t\tif handle != current_windows:\n\t\t\t\tself.driver.switch_to.window(handle)\n\t\t\t\tbreak\n\t\t"
    #如果存在【执行js脚本“XXX”】”产生语句“self.driver.execute_script(XXX)”
    if("执行js脚本" in line):
        name = str(re.findall(r"执行js脚本“(.+?)”",line))[2:-2]
        mystr = "self.driver.execute_script(\""+name+"\")"
    #如果存在【确定弹出框】产生语句“self.driver.switch_to_alert().accept()”
    if("确定弹出框" in line):
        mystr = "self.driver.switch_to_alert().accept()"
    #如果存在【取消弹出框】”产生语句“self.driver.switch_to_alert().dismiss()”
    if("取消弹出框" in line):
        mystr = "self.driver.switch_to_alert().dismiss()"
    #如果存在【获取弹窗框里面的文字】产生语句“text=self.driver.switch_to.alert.text”
    if("获取弹窗框里面的文字" in line):
        mystr = "text=self.driver.switch_to.alert.text"
    #如果存在【属性为“XXX”的文字】产生语句“.get_attribute(XXX)”
    if("属性为" in line):
        name = str(re.findall(r"属性为“(.+?)”的文字",line))[2:-2]
        mystr = mystr+".get_attribute(\""+name+"\")"
    #如果存在“【设置名为“XXX”的cookie，值为“YYY”】”产生语句“self.driver.add_cookie({"name":"XXX","value":YYY})”
    if("设置名为“" in line) and ("cookie，值为“" in line):
        name = str(re.findall(r"设置名为“(.+?)”的",line))[2:-2]
        cookie = str(re.findall(r"cookie，值为“(.+?)”",line))[2:-2]
        mystr = "self.driver.add_cookie({\"name\":\""+name+"\",\"value\":"+cookie+"})"
    #如果存在【移动元素到...的位置】产生语句“ActionChains(self.driver).move_to_element(...).perform()”
    if("移动元素到" in line) and ("的位置" in line):
        mystr = "ActionChains(self.driver).move_to_element("+mystr+").perform()"
    #如果存在【获取HTML5 Viedo】”产生语句“video=element”
    if("获取HTML5 Viedo" in line):
        mystr = "video="+mystr
    #如果存在【获取HTML5 Viedo url】”产生语句“url=self.driver.execute_script("currentSrc;",video)”
    if("获取HTML5 Viedo url为" in line):
        mystr = "url=self.driver.execute_script(\"currentSrc;\",video)"
    #如果存在【执行HTML5 Viedo 播放操作】”产生语句“self.driver.execute_script("return arguments[0].play()",video)”
    if("执行HTML5 Viedo 播放操作" in line):
        mystr = "self.driver.execute_script(\"return arguments[0].play()\",video)"
    #如果存在【执行HTML5 Viedo 停止操作】”产生语句“self.driver.execute_script("return arguments[0].stop()",video)”
    if("执行HTML5 Viedo 停止操作" in line):
        mystr = "self.driver.execute_script(\"return arguments[0].stop()\",video)"
    #如果存在【执行HTML5 Viedo 暂停操作】”产生语句“self.driver.execute_script("return arguments[0].pause()",video)”
    if("执行HTML5 Viedo 暂停操作" in line):
        mystr = "self.driver.execute_script(\"return arguments[0].pause()\",video)"
    #如果存在【存储变量为“XXX”】产生语句“XXX=element”
    if("存储变量为" in line):
        name = str(re.findall(r"存储变量为“(.+?)”",line))[2:-2]
        mystr = name+"="+mystr
    #如果存在【获取下拉条】产生语句“se=element”
    if("获取下拉条" in line):
        mystr = "se="+mystr
    #如果存在“【选择可见文字为“XXX”的下拉条】的下拉条”产生语句“Select(se).select_by_visible_text('XXX')”
    if("选择可见文字为" in line):
        name = str(re.findall(r"选择可见文字为“(.+?)”的下拉条",line))[2:-2]
        mystr = "Select(se).select_by_visible_text(\""+name+"\")"
    #如果存在“【选择值为“XXX”的下拉条】”产生语句“Select(se).select_by_value('XXX')”
    if("选择值为“" in line):
        name = str(re.findall(r"选择值为“(.+?)”的下拉条",line))[2:-2]
        mystr = "Select(se).select_by_value(\""+name+"\")"
    #如果存在“【选择序号为“XXX”的下拉条】”产生语句“Select(se).select_by_index(3)”
    if("选择序号为“" in line):
        name = str(re.findall(r"选择序号为“(.+?)”的下拉条",line))[2:-2]
        mystr = "Select(se).select_by_index("+name+")"
    #如果存在“【打印“XXX”】”产生语句“Select(se).select_by_index(3)”
    if("打印“" in line):
        name = str(re.findall(r"打印“(.+?)”",line))[2:-2]
        mystr = "print(\"\"+name+"")"
    #如果存在【判断...被选中】”产生语句“self.assertTrue(....is_selected())”
    if("判断" in line) and ("被选中" in line):
        mystr = "self.assertTrue("+mystr+".is_selected())"
    #如果存在【判断元素...没有被选中】”产生语句“self.assertNotTrue(XXX.is_selected())”
    if("判断元素" in line) and ("没有被选中" in line):
        mystr = "self.assertNotTrue("+mystr+".is_selected())"
    return mystr

#进行断言
def myassert(line):
    mystr =""
    #如果存在【标题应该为“XXX”】产生语句“self.assertEqual(XXX,self.driver.title)”
    if("标题应该为" in line):
        word = str(re.findall(r"标题应该为“(.+?)”",line))[2:-2]
        mystr = "self.assertEqual(\""+word+"\",self.driver.title)"
    #如果存在【标题应该包含“XXX”】产生语句“self.assertIn(XXX,self.driver.title)”
    if("标题应该包含" in line):
        word = str(re.findall(r"标题应该包含“(.+?)”",line))[2:-2]
        mystr = "self.assertIn(\""+word+"\",self.driver.title)"
    #如果存在【网页路径应该为“XXX”】或【网页url应该为“XXX”】产生语句“self.assertEqual(XXX,driver.current_url)”
    if("网页路径应该为" in line) or ("网页url应该为" in line):
        word = str(re.findall(r"网页路径应该为“(.+?)”",line))[2:-2]
        if len(word)==0:
            word = str(re.findall(r"网页url应该为“(.+?)”",line))[2:-2]
        mystr = "self.assertEqual(\""+word+"\",self.driver.current_url)"
    #如果存在【返回值与“XXX”相同】产生语句“self.assertEqual(XXX,text)”
    if("返回值与" in line) and ("相同" in line):
        word = str(re.findall(r"返回值与“(.+?)”相同",line))[2:-2]
        mystr = "self.assertEqual(\""+word+"\",text)"
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
    
    


