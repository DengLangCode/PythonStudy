# encoding:utf-8
# #指定编码为utf-8，目得是支持中文
'''
模拟浏览器抓取数据，模拟浏览器发出指令，不会被网址拦截
模块：selenium（浏览器自动化测试框架）
        Selenium 是一个用于Web应用程序测试的工具。
        Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。
        支持的浏览器包括IE（7, 8, 9, 10, 11），Mozilla Firefox，Safari，Google Chrome，Opera等。
        这个工具的主要功能包括：
        测试与浏览器的兼容性——测试你的应用程序看是否能够很好得工作在不同浏览器和操作系统之上。
        测试系统功能——创建回归测试检验软件功能和用户需求。
        支持自动录制动作和自动生成 .Net、Java、Perl等不同语言的测试脚本。
    re
        re模块是python独有的匹配字符串的模块，该模块中提供的很多功能是基于正则表达式实现的，
        而正则表达式是对字符串进行模糊匹配，提取自己需要的字符串部分，他对所有的语言都通用。
        注意：
        re模块是python独有的
        正则表达式所有编程语言都可以使用
        re模块、正则表达式是对字符串进行操作
'''
import selenium
import selenium.webdriver
import re
from selenium import webdriver
import wx

# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jan 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class Dlg
###########################################################################

class Dlg(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"python爬虫练习", pos=wx.DefaultPosition,
                           size=wx.Size(600, 600), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(600,600)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"查询结果:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer3.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.m_staticText_result = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_result.Wrap(-1)
        self.m_staticText_result.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer3.Add(self.m_staticText_result, 1, wx.ALL, 5)

        bSizer1.Add(bSizer3, 0, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel_html = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel_html.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_html = wx.StaticText(self.m_panel_html, wx.ID_ANY, u"1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1", wx.DefaultPosition,
                                           wx.DefaultSize, wx.ST_ELLIPSIZE_MIDDLE)
        self.m_static_html.Wrap(-1)
        bSizer5.Add(self.m_static_html, 1, wx.ALL, 5)

        self.m_panel_html.SetSizer(bSizer5)
        self.m_panel_html.Layout()
        bSizer5.Fit(self.m_panel_html)
        bSizer4.Add(self.m_panel_html, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1.Add(bSizer4, 1, wx.EXPAND, 5)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrlSearch = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_textCtrlSearch, 1, wx.ALL, 5)

        self.m_buttonSearch = wx.Button(self, wx.ID_ANY, u"搜索", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_buttonSearch, 0, wx.ALL, 5)

        bSizer1.Add(bSizer2, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_buttonSearch.Bind(wx.EVT_BUTTON, self.OnButtonClick_Search)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnButtonClick_Search(self, event):
        event.Skip()


###########################################################################
## Class RealDlg：继承Dlg，重写相关函数
###########################################################################
class RealDlg(Dlg):
    def __init__(self, parent):
        Dlg.__init__(self, parent)
        self.m_textCtrlSearch.SetValue(u"python")
        pass
    def OnButtonClick_Search(self, event):
        keyword = self.m_textCtrlSearch.GetValue()
        keyword = keyword.strip()
        html = [wx.EmptyString]
        value = GetResultFrom51Job(keyword, html)
        print(html[0])
        strShow = html[0]
        strShow = strShow[0:80000]
        self.m_static_html.SetLabel(strShow)
        self.m_staticText_result.SetLabel(value)

###########################################################################
## Method:
###########################################################################

def GetResultFrom51Job(searchname, html):
    url = "https://search.51job.com/list/090200,000000,0000,00,9,99,"+searchname+",2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    driver = selenium.webdriver.Chrome('D:\Python27\module\chromedriver.exe')
    driver.minimize_window()
    driver.get(url)
    pagesource = driver.page_source
    html[0] = pagesource
#    print(html)
#    restr = "<em>(\\d+)</em>"
    restr = """<div class="rt">([\s\S]*?)</div>"""
    regex = re.compile(restr,re.IGNORECASE)
    mylist = regex.findall(pagesource)
    newstr = mylist[0].strip()
#    print(newstr)
    restr = "(\\d+)"
    regex = re.compile(restr,re.IGNORECASE)
    mylist1 = regex.findall(newstr)
#    print(mylist[0])
    driver.close()
    if len(mylist1):
        return mylist1[0]
    else:
        return "失败"
    pass

###########################################################################
## Funtion:主函数
###########################################################################

if __name__ == "__main__":
        app = wx.App()
        dlg = RealDlg(None)
        dlg.Show()
        app.MainLoop()
