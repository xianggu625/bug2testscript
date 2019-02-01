'''
(基本)
【进入网站“url路径”】
(定位)
【进入网站“url”】
【id为“XXX”】、【编号为“XXX”】
【name为“XXX”】、【名称为“XXX”】、【名为“XXX”】
【classname为“XXX”】、【class名为“XXX”】、【类名为“XXX”】
【tagname为“XXX”】、【tag名为“XXX”】、【标签名为“XXX”】
【链接文字为“XXX”】、【url文字为“XXX”】
【链接部分文字为“XXX”】、【url部分文字为“XXX”】
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
【向提示框输入“XXX”】
【确定提示框】、【确定弹出框】
【取消提示框】、【取消弹出框】
【获得提示框里面的文字存为变量为“YYY”】
【获得弹出框里面的文字存为变量为“YYY”】
【属性为“XXX”的文字】
【添加cookie，名为“XXX”值为变量“YYY”】
【添加cookie，名为“XXX”值为“YYY”】
【获得所有cookie存为变量“YYY”】
【获得cookie，名为“XXX”，存为变量“YYY”】
【删除cookie，名为“XXX”】
【删除所有cookie】
【移动鼠标到元素名为...的位置】
【鼠标点击...的元素】
【在元素...的位置按下鼠标左键不放】
【在元素...的位置单击鼠标右键】
【在元素...的位置双击鼠标】
【从一个元素名...的位置拖鼠标到另一个元素...的位置松开】
【从...位置拖拽鼠标到（x,y）的位置】
【从当前位置移动鼠标到（x,y）的位置】
【移动到某个元素...的位置上，然后移动到该元素相对坐标为（x,y）的位置上】
【获取HTML5 Viedo...存储变量为“video”】
【获得HTML5 Viedo url为变量名“XXX”,HTML5 Viedo变量为“YYY”】
【执行HTML5 Viedo 播放操作,HTML5 Viedo变量为“YYY”】
【执行HTML5 Viedo 停止操作,HTML5 Viedo变量为“YYY”】
【执行HTML5 Viedo 暂停操作,HTML5 Viedo变量为“YYY”】
【存储变量名为“XXX”值为变量为“YYY”】
【存储变量为“YYY”】
【获取下拉条...】
【选择可见文字为“XXX”的下拉条...】
【选择值为“XXX”的下拉条...】、【选择value为“XXX”的下拉条...】
【选择序号为“XXX”的下拉条...】
【取消所有所选的下拉条...】
【取消值为“XXX”的下拉条...】、【取消value为“XXX”的下拉条...】
【取消index为“XXX”的下拉条...】、【取消索引为“XXX”的下拉条...】
【取消文字为“XXX”的下拉条...】、【取消text为“XXX”的下拉条...】
【如果“XXX”被选择】
【如果“XXX”没被选择】
【那么“XXX”】
【判断...被选中】
【判断...没有被选中】
(断言)
【标题应该为“XXX”】
【标题应该包含“XXX”】
【标题应该不包含“XXX”】
【网页路径应该为“XXX”】、【网页url应该为“XXX”】
【返回值“XXX”与变量“YYY”相同】
【判断条件“XXX”为真】
【判断条件“XXX”为假
【判断“XXX”为空】
【判断“XXX”不为空】

'''


#!/usr/bin/env python
#coding:utf-8
import re
import codecs
#初始化
class bug2report:
    def __init__(self):
         self.flag = 1
    
    def init(self,line):
        line = line.replace("选取","选择")
        line = line.replace("URL","url")
        line = line.replace(",","，")
        return line

    def create_code(self,check_words_left,check_words_right, mystring_left,mystring_right,line,mystr):
        i = 0
        name = ""
        for check_word_left in check_words_left:
            if (check_word_left in line) and (len(name)==0):
                name = str(re.findall(check_words_left[i]+"(.+?)"+check_words_right[i],line))[2:-2]
            i = i+1
        if len(name)!=0:
            return mystring_left+name+mystring_right
        else:
            return ""

    #获得对象
    def getElenument(self,line):
        mystr =""
        line = self.init(line)
        #如果存在【进入网站“url”】产生语句“self.driver.get(url)”
        check_words_left = ["进入网站“"]
        check_words_right = ["”"]
        mystring_left="self.driver.get(\""
        mystring_right="\")"
        code = self.create_code(check_words_left,check_words_right,mystring_left,mystring_right,line,mystr)
        if len(code)!=0:
            mystr = code
        #如果存在【id为“XXX”】或【编号为“XXX”】产生语句“self.driver.find_element_by_id(XXX)”
        check_words_left = ["id为“","编号为“"]
        check_words_right = ["”","”"]
        mystring_left="self.driver.find_element_by_id(\""
        mystring_right="\")"
        code = self.create_code(check_words_left,check_words_right,mystring_left,mystring_right,line,mystr)
        if len(code)!=0:
            mystr = code
        #如果存在【name为“XXX”】或【名称为“XXX”】或【名为“XXX”】产生语句“self.find_element_by_id(XXX)”
        check_words_left = ["name为“","名称为“","名为“"]
        check_words_right = ["”","”","”"]
        mystring_left="self.driver.find_element_by_name(\""
        mystring_right="\")"
        code = self.create_code(check_words_left,check_words_right,mystring_left,mystring_right,line,mystr)
        if len(code)!=0:
            mystr = code
        #如果存在【classname为“XXX”】或【class名为“XXX”】或【类名为“XXX”】产生语句“self.driver.find_element_by_class_name(XXX)”
        check_words_left = ["classname为“","class名为“","类名为“"]
        check_words_right = ["”","”","”"]
        mystring_left="self.driver.find_element_by_class_name(\""
        mystring_right="\")"
        code = self.create_code(check_words_left,check_words_right,mystring_left,mystring_right,line,mystr)
        if len(code)!=0:
            mystr = code
        #如果存在【tagname为“XXX”】或【tag名为“XXX”】或【标签名为“XXX”】产生语句“self.driver.find_element_by_tag_name(XXX)”
        check_words_left = ["tagname为“","tag名为“","标签名为“"]
        check_words_right = ["”","”","”"]
        mystring_left="self.driver.find_element_by_tag_name(\""
        mystring_right="\")"
        code = self.create_code(check_words_left,check_words_right,mystring_left,mystring_right,line,mystr)
        if len(code)!=0:
            mystr = code
        #如果存在【链接文字为“XXX”】或【url文字为“XXX”】产生语句“self.driver.find_element_by_link_text(XXX)”
        check_words_left = ["链接文字为“","url文字为“"]
        check_words_right = ["”","”"]
        mystring_left="self.driver.find_element_by_link_text(\""
        mystring_right="\")"
        code = self.create_code(check_words_left,check_words_right,mystring_left,mystring_right,line,mystr)
        if len(code)!=0:
            mystr = code
        #如果存在【链接部分文字为“XXX”】或【url部分文字为“XXX”】产生语句“self.driver.find_element_by_partial_link_text(XXX)”
        check_words_left = ["链接部分文字为“","url部分文字为“"]
        check_words_right = ["”","”"]
        mystring_left="self.driver.find_element_by_partial_link_text(\""
        mystring_right="\")"
        code = self.create_code(check_words_left,check_words_right,mystring_left,mystring_right,line,mystr)
        if len(code)!=0:
            mystr = code
        #如果存在【cssselector为“XXX”】或【css选择为“XXX”】产生语句“self.driver.find_element_by_css_selector(XXX)”
        check_words_left = ["cssselector为“","css选择为“"]
        check_words_right = ["”","”"]
        mystring_left="self.driver.find_element_by_css_selector(\""
        mystring_right="\")"
        code = self.create_code(check_words_left,check_words_right,mystring_left,mystring_right,line,mystr)
        if len(code)!=0:
            mystr = code
        #如果存在【xpath为“XXX”】产生语句“self.driver.find_element_by_xpath(XXX)”
        check_words_left = ["xpath为“"]
        check_words_right = ["”"]
        mystring_left="self.driver.find_element_by_css_selector(\""
        mystring_right="\")"
        code = self.create_code(check_words_left,check_words_right,mystring_left,mystring_right,line,mystr)
        if len(code)!=0:
            mystr = code
        return self.action(line,mystr)

    #进行操作
    def action(self,line,mystr):
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
            sec = str(re.findall(r"强制等待(\d+)秒",line))[2:-2]
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
        #如果存在【向提示框输入“XXX”】产生语句“switch_to.alert.send_keys(XXX)”
        check_words_left = ["向提示框输入“"]
        check_words_right = ["”"]
        mystring_left="switch_to.alert.send_keys(\""
        mystring_right="\")"
        code = self.create_code(check_words_left,check_words_right,mystring_left,mystring_right,line,mystr)
        if len(code)!=0:
            mystr = code
        #如果存在【确定提示框】或【确定弹出框】产生语句“self.driver.switch_to_alert.accept()”
        if("确定提示框" in line) or ("确定弹出框" in line):
            mystr = "self.driver.switch_to_alert.accept()"
        #如果存在【取消提示框】或【取消弹出框】产生语句“self.driver.switch_to_alert.dismiss()”
        if("取消提示框" in line) or ("取消弹出框" in line):
            mystr = "self.driver.switch_to_alert.dismiss()"
        #如果存在【获得提示框里面的文字存为变量为“YYY”】或【获得弹出框里面的文字存为变量为“YYY”】产生语句“text=self.driver.switch_to.alert.text”
        if(("获得提示框里面的文字" in line) or ("获得弹出框里面的文字" in line)) and ("存为变量为“" in line):
            value = str(re.findall(r"存为变量为“(.+?)”",line))[2:-2]
            mystr = value+"=self.driver.switch_to.alert.text"
        #如果存在【属性为“XXX”的文字】产生语句“.get_attribute(XXX)”
        if("属性为" in line):
            name = str(re.findall(r"属性为“(.+?)”的文字",line))[2:-2]
            mystr = mystr+".get_attribute(\""+name+"\")"
        #如果存在“【添加cookie，名为“XXX”值为变量“YYY”】”产生语句“self.driver.add_cookie({"name":"XXX","value":YYY})”
        if(line.startswith("添加cookie，")) and ("名为“" in line) and ("值为变量“" in line):
            name = str(re.findall(r"名为“(.+?)”",line))[2:-2]
            cookie = str(re.findall(r"值为变量“(.+?)”",line))[2:-2]
            mystr = "self.driver.add_cookie({\"name\":\""+name+"\",\"value\":"+cookie+"})"
        #如果存在“【添加cookie，名为“XXX”值为“YYY”】”产生语句“self.driver.add_cookie({"name":"XXX","value":"YYY"})”
        if (line.startswith("添加cookie，")) and ("名为“" in line) and ("值为“" in line):
            name = str(re.findall(r"添加cookie，名为“(.+?)”",line))[2:-2]
            cookie = str(re.findall(r"值为“(.+?)”",line))[2:-2]
            mystr = "self.driver.add_cookie({\"name\":\""+name+"\",\"value\":\""+cookie+"\"})"
        #如果存在【获得所有cookie存为变量“YYY”】产生语句“YYY=self.driver.get_cookies()”
        if("获得所有cookie存为变量“" in line):
            value = str(re.findall(r"获得所有cookie存为变量“(.+?)”",line))[2:-2]
            mystr = value+"=self.driver.get_cookies()"
        #如果存在【获得cookie，名为“XXX”,存为变量“YYY”】产生语句“YYY=self.driver.get_cookies(name="XXX")”
        if(line.startswith("获得cookie，")) and ("名为“" in line) and ("存为变量“" in line):
            name = str(re.findall(r"获得cookie，名为“(.+?)”",line))[2:-2]
            value = str(re.findall(r"存为变量“(.+?)”",line))[2:-2]
            mystr = value+"=self.driver.get_cookies(name=\""+name+"\")"
        #如果存在【删除cookie，名为“XXX”】产生语句“delete_cookies("XXX")”
        if(line.startswith("删除cookie")) and ("名为“" in line):
            name = str(re.findall(r"删除cookie，名为“(.+?)”",line))[2:-2]
            mystr = "self.delete_cookies(\""+name+"\")"
        #如果存在【删除所有cookie】产生语句“self.driver.delete_all_cookies()”
        if("删除所有cookie" in line):
            mystr = "self.driver.delete_all_cookies()"
        #如果存在【移动鼠标到元素...的位置】产生语句“ActionChains(self.driver).move_to_element(...).perform()”
        if("移动鼠标到元素" in line) and ("的位置" in line):
            mystr = "ActionChains(self.driver).move_to_element("+mystr+").perform()"
        #如果存在【点击...的元素】产生语句“ActionChains(driver).click(...).perform()”
        if("点击" in line) and ("的元素" in line):
            mystr = "ActionChains(driver).click("+mystr+").perform()"
        #如果存在【在元素...的位置按下鼠标左键不放】产生语句“ActionChains(driver).click_and_hold(...).perform()”
        if("在元素" in line) and ("的位置按下鼠标左键不放" in line):
            mystr = "ActionChains(driver).click_and_hold("+mystr+").perform()"
        #如果存在【在元素...的位置单击鼠标右键】产生语句“ActionChains(driver).context_click(...).perform()”
        if("在元素" in line) and ("的位置单击鼠标右键" in line):
            mystr = "ActionChains(driver).context_click("+mystr+").perform()"
        #如果存在【在元素...的位置双击鼠标】产生语句“ActionChains(driver).double_click(...).perform()”
        if("在元素" in line) and ("的位置双击鼠标" in line):
            mystr = "ActionChains(driver).double_click("+mystr+").perform()"
        #如果存在【从一个元素...的位置拖鼠标到另一个元素...的位置松开】产生语句“ActionChains(driver).drag_and_drop(source,target).perform()”
        if("从一个元素" in line) and ("的位置拖鼠标到另一个元素" in line) and ("的位置松开" in line):
            mystr1 = self.getElenument(line[:20])
            mystr2 = self.getElenument(line[15:])
            mystr = mystr1+","+mystr2
            mystr = "ActionChains(driver).drag_and_drop("+mystr+").perform()"
        #如果存在【从...位置拖拽鼠标到（x,y）的位置】产生语句“ActionChains(driver).drag_and_drop_by_offset(...,x,y)”
        if("从" in line) and ("位置拖拽鼠标到" in line):
            x = str(re.findall(r"（(\d+)，\d+）",line))[2:-2]
            y = str(re.findall(r"（\d+，(\d+)）",line))[2:-2]
            mystr = "ActionChains(driver).drag_and_drop_by_offset("+mystr+","+x+","+y+")"
        #如果存在【从当前位置移动鼠标到（x,y）的位置】产生语句“ActionChains(driver).move_by_offset(x,y)”
        if("从当前位置移动鼠标到" in line) and ("的位置" in line):
            x = str(re.findall(r"（(\d+)，\d+）",line))[2:-2]
            y = str(re.findall(r"（\d+，(\d+)）",line))[2:-2]
            mystr = "ActionChains(driver).move_by_offset("+x+","+y+")"
        #如果存在【移动到某个元素...的位置上，然后移动到该元素相对坐标为（x,y）的位置上】产生语句“ActionChains(driver).move_to_element_with_offset(element,x,y)”
        if("移动到某个元素" in line) and ("的位置上，然后移动到该元素相对坐标为" in line):
            x = str(re.findall(r"（(\d+)，\d+）",line))[2:-2]
            y = str(re.findall(r"（\d+，(\d+)）",line))[2:-2]
            mystr = "ActionChains(driver).move_to_element_with_offset("+mystr+","+x+","+y+").perform()"
        #如果存在【获得HTML5 Viedo 存储为变量“XXX”】”产生语句“XXX=element”
        if("获得HTML5 Viedo" in line) and ("存储为变量“" in line):
            name = str(re.findall(r"存储为变量“(.+?)”",line))[2:-2]
            mystr = name+" = "+mystr
        #如果存在【获得HTML5 Viedo url为变量名“XXX”,HTML5 Viedo变量为“YYY”】”产生语句“XXX=self.driver.execute_script("currentSrc;",YYY)”
        if("获得HTML5 Viedo url为变量名“" in line) and ("HTML5 Viedo变量为“" in line):
            name = str(re.findall(r"获得HTML5 Viedo url为变量名“(.+?)”",line))[2:-2]
            value = str(re.findall(r"HTML5 Viedo变量为“(.+?)”",line))[2:-2]
            mystr = name+"=self.driver.execute_script(\"currentSrc;\","+value+")"
        #如果存在【执行HTML5 Viedo 播放操作,HTML5 Viedo变量为“YYY”】”产生语句“self.driver.execute_script("return arguments[0].play()",YYY)”
        if("执行HTML5 Viedo 播放操作" in line) and ("HTML5 Viedo变量为“" in line):
            value = str(re.findall(r"HTML5 Viedo变量为“(.+?)”",line))[2:-2]
            mystr = "self.driver.execute_script(\"return arguments[0].play()\","+value+")"
        #如果存在【执行HTML5 Viedo 停止操作,HTML5 Viedo变量为“YYY”】”产生语句“self.driver.execute_script("return arguments[0].stop()",YYY)”
        if("执行HTML5 Viedo 停止操作" in line) and ("HTML5 Viedo变量为“" in line):
            value = str(re.findall(r"HTML5 Viedo变量为“(.+?)”",line))[2:-2]
            mystr = "self.driver.execute_script(\"return arguments[0].stop()\","+value+")"
        #如果存在【执行HTML5 Viedo 暂停操作,HTML5 Viedo变量为“YYY”】”产生语句“self.driver.execute_script("return arguments[0].pause()",YYY)”
        if("执行HTML5 Viedo 暂停操作" in line) and ("HTML5 Viedo变量为“" in line):
            value = str(re.findall(r"HTML5 Viedo变量为“(.+?)”",line))[2:-2]
            mystr = "self.driver.execute_script(\"return arguments[0].pause()\","+value+")"
        #如果存在【存储变量名为“XXX”值为变量为“YYY”】产生语句“YYY=XXX”
        if("存储变量名为" in line) and ("值为变量为" in line):
            name = str(re.findall(r"存储变量名为“(.+?)”",line))[2:-2]
            value = str(re.findall(r"值为变量为“(.+?)”",line))[2:-2]
            mystr = value+"="+name
        #如果存在【存储变量为“YYY”】产生语句“YYY=element”
        if("存储变量为“" in line):
            value = str(re.findall(r"存储变量为“(.+?)”",line))[2:-2]
            mystr = value+" = "+mystr
        #如果存在“【取消所有所选的下拉条】的下拉条”产生语句“Select(elemiume).deselect_all()”
        if("取消所有所选的下拉条" in line):
            name = str(re.findall(r"取消所有所选的下拉条",line))[2:-2]
            mystr = "Select("+mystr+").deselect_all()"
        #如果存在“【取消值为“XXX”的下拉条】或【取消value为“XXX”的下拉条】的下拉条”产生语句“Select(elemiume).deselect_by_value(XXX)”
        if("取消值为" in line) and ("”的下拉条" in line):
            name = str(re.findall(r"取消值为“(.+?)”的下拉条",line))[2:-2]
            mystr = "Select("+mystr+").deselect_by_value(\""+name+"\")"
        elif("取消value为" in line) and ("”的下拉条" in line):
            name = str(re.findall(r"取消value为“(.+?)”的下拉条",line))[2:-2]
            mystr = "Select("+mystr+").deselect_by_value(\""+name+"\")"
        #如果存在“【取消index为“XXX”的下拉条】或【取消索引为“XXX”的下拉条】的下拉条”产生语句“Select(elemiume).deselect_by_index(XXX)”
        if("取消index为" in line) and ("”的下拉条" in line):
            name = str(re.findall(r"取消index为“(.+?)”的下拉条",line))[2:-2]
            mystr = "Select("+mystr+").deselect_by_index(\""+name+"\")"
        elif("取消索引为" in line) and ("”的下拉条" in line):
            name = str(re.findall(r"取消索引为“(.+?)”的下拉条",line))[2:-2]
            mystr = "Select("+mystr+").deselect_by_index(\""+name+"\")"
        #如果存在“【取消文字为“XXX”的下拉条】或【取消text为“XXX”的下拉条】的下拉条”产生语句“Select(elemiume).deselect_by_visible_text(XXX)”
        if("取消文字为" in line) and ("”的下拉条" in line):
            name = str(re.findall(r"取消文字为“(.+?)”的下拉条",line))[2:-2]
            mystr = "Select("+mystr+").deselect_by_visible_text(\""+name+"\")"
        elif("取消text为" in line) and ("”的下拉条" in line):
            name = str(re.findall(r"取消text为“(.+?)”的下拉条",line))[2:-2]
            mystr = "Select("+mystr+").deselect_by_visible_text(\""+name+"\")"
        #如果存在“【选择可见文字为“XXX”的下拉条】的下拉条”产生语句“Select(se).select_by_visible_text('XXX')”
        if("选择可见文字为" in line):
            name = str(re.findall(r"选择可见文字为“(.+?)”的下拉条",line))[2:-2]
            mystr = "Select("+mystr+").select_by_visible_text(\""+name+"\")"
        #如果存在“【选择值为“XXX”的下拉条】或【选择value为“XXX”的下拉条】”产生语句“Select(elemiume).select_by_value('XXX')”
        if("选择值为“" in line) and ("”的下拉条" in line):
            name = str(re.findall(r"选择值为“(.+?)”的下拉条",line))[2:-2]
            mystr = "Select("+mystr+").select_by_value(\""+name+"\")"
        elif ("选择value为“" in line) and ("”的下拉条" in line):
            name = str(re.findall(r"选择value为“(.+?)”的下拉条",line))[2:-2]
            mystr = "Select("+mystr+").select_by_value(\""+name+"\")"
        #如果存在“【选择序号为“XXX”的下拉条】”产生语句“Select(elemiume).select_by_index(3)”
        if("选择序号为“" in line):
            name = str(re.findall(r"选择序号为“(\d+)”的下拉条",line))[2:-2]
            mystr = "Select("+mystr+").select_by_index("+name+")"
        #如果存在“【打印“XXX”】”产生语句“Select(elemiume).select_by_index(3)”
        if("打印“" in line):
            name = str(re.findall(r"打印“(.+?)”",line))[2:-2]
            mystr = "print(\"\"+name+"")"
        #如果存在【判断...被选中】”产生语句“self.assertTrue(....is_selected())”
        if("判断" in line) and ("被选中" in line):
            mystr = "self.assertTrue("+mystr+".is_selected())"
        #如果存在【判断...没有被选中】”产生语句“self.assertNotTrue(XXX.is_selected())”
        if("判断" in line) and ("没有被选中" in line):
            mystr = "self.assertNotTrue("+mystr+".is_selected())"
        return mystr

    #进行断言
    def myassert(self,line):
        mystr =""
        #如果存在【标题应该为“XXX”】产生语句“self.assertEqual(XXX,self.driver.title)”
        if("标题应该为" in line):
            judge = str(re.findall(r"标题应该为“(.+?)”",line))[2:-2]
            mystr = "self.assertEqual(\""+judge+"\",self.driver.title)\n"
        #如果存在【标题应该包含“XXX”】产生语句“self.assertIn(XXX,self.driver.title)”
        if("标题应该包含" in line):
            judge = str(re.findall(r"标题应该包含“(.+?)”",line))[2:-2]
            mystr = "self.assertIn(\""+judge+"\",self.driver.title)\n"
        #如果存在【标题应该不包含“XXX”】产生语句“self.assertNotIn(XXX,self.driver.title)”
        if("标题应该不包含" in line):
            judge = str(re.findall(r"标题应该不包含“(.+?)”",line))[2:-2]
            mystr = "self.assertNotIn(\""+judge+"\",self.driver.title)\n"
        #如果存在【网页路径应该为“XXX”】或【网页url应该为“XXX”】产生语句“self.assertEqual(XXX,driver.current_url)”
        if("网页路径应该为" in line) or ("网页url应该为" in line):
            judge = str(re.findall(r"网页路径应该为“(.+?)”",line))[2:-2]
            if len(judge)==0:
                judge = str(re.findall(r"网页url应该为“(.+?)”",line))[2:-2]
            mystr = "self.assertEqual(\""+judge+"\",self.driver.current_url)\n"
        #如果存在【返回值与“XXX”相同】产生语句“self.assertEqual(XXX,text)”
        if("返回值与" in line) and ("相同" in line):
            judge = str(re.findall(r"返回值与“(.+?)”相同",line))[2:-2]
            mystr = "self.assertEqual(\""+judge+"\",text)\n"
        #如果存在【判断条件“XXX”为真】产生语句“self.assertTrue(XXX)”
        if("判断条件“" in line) and ("为真" in line):
            judge = str(re.findall(r"判断条件“(.+?)”为真",line))[2:-2]
            mystr = "self.assertTrue("+judge+")\n"
        #如果存在【判断条件“XXX”为假】产生语句“self.assertFalse(XXX)”
        if("判断条件“" in line) and ("为假" in line):
            judge = str(re.findall(r"判断条件“(.+?)”为假",line))[2:-2]
            mystr = "self.assertFalse("+judge+")\n"
        #如果存在【判断“XXX”为空】产生语句“self.assertIsNone(XXX)”
        if("判断“" in line) and ("为空" in line):
            judge = str(re.findall(r"判断“(.+?)”为空",line))[2:-2]
            mystr = "self.assertIsNone("+judge+")\n"
        #如果存在【判断“XXX”不为空】产生语句“self.assertIsNotNone(XXX)”
        if("判断“" in line) and ("不为空" in line):
            judge = str(re.findall(r"判断“(.+?)”不为空",line))[2:-2]
            mystr = "self.assertIsNotNone("+judge+")\n"
        return mystr

    #读模板文件
    def readfile(self,file,txt):
        f2 = open(file,"r")
        line=f2.read()
        f2.close()
        line = line.replace('+++1',txt)
        return line

    #写入文件
    def writefile(self,file,mystr):
        f3=codecs.open(file,"w",encoding='utf8')
        f3.write(mystr)
        f3.close()

    #初始化
    def ceratescript(self):
        #从文本中读入缺陷报告，存在bugReport字段中
        f1=codecs.open("bugReport.txt",encoding='utf8') 
        txt=""
        for line in f1:
            #进行匹配
            code = self.getElenument(line)
            txt=txt+"\t\t"+code+"\n"
            ast = self.myassert(line)
            if not (ast) =="":
                txt = txt[:-1]
                txt = txt+ast
            elif(code==""):
                self.flag = 0
                print("句子【"+line+"】错误，无法进行匹配")
        f1.close()
        return txt
            
if __name__=='__main__':
    b2j = bug2report()
    txt = b2j.ceratescript()
    if (b2j.flag):
        #读入unittest的测试文件模板
        line = b2j.readfile("model.py",txt)
        #写入py文件
        b2j.writefile("test.py",line)
    
    


