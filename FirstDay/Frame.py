"""
框架结构
2019/12/18
一个wx程序由两个必要的对象构成：
应用程序对象，即wx.App或其子类
顶级窗口对象，即wx.Frame或其子类对象
创建一个wx.App的子类，需要执行四个步骤：
    1.定义这个子类
    2.在定义的子类中写一个OnInit方法
    3.在程序中创建这个子类的一个实例
    4.调用应用程序实例的MainLoop方法，将这个程序的控制权交给wxPython
"""

import wx
App_Title = "框架测试"
class mainFrame(wx.Frame): #定义一个wx.Frame子类对象
    def __init__(self):
        '''构造函数'''
        wx.Frame.__init__(self, None, -1, App_Title)
        self.SetBackgroundColour(wx.Colour(250, 0, 0))
        self.SetSize(600, 600)
        self.Center()
        pass
class mainApp(wx.App): #定义一个wx.App子类对象
        def OnInit(self): #在子类中写OnInit方法
            self.SetAppName(App_Title)
            self.Frame = mainFrame()
            self.Frame.Show()
            return True
            pass
if __name__ == "__main__":
        app = mainApp(redirect=True, filename="debug.txt")
        app.MainLoop(),