"""
    Python学习之wxPython窗口
    2019/12/18
"""
import wx                                                       #导入wx模块，实质就是路径搜索和搜索路径
app = wx.App()                                                  #实例化应用程序对象
window = wx.Frame(None,title = "Python Test!",size = (600,600)) #实例化顶级窗口对象
panel = wx.Panel(window)                                        #实例化panel窗口
label = wx.StaticText(panel,label = "Test",pos = (0,0))
window.Show(True)
app.MainLoop()                                                  #进行图形渲染与游戏逻辑处理