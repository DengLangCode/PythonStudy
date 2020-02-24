# -*- coding: utf-8 -*-
# encoding:utf-8
###########################################################################
## Python code generated with wxFormBuilder (version Jan 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button1, 0, wx.ALL, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        #事件绑定
        self.m_button1.Bind(wx.EVT_BUTTON, self.ButtonClicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def ButtonClicked(self, event):
        event.Skip()
#另一个类去继承MyFrame
class Test(MyFrame1):
    def __init__(self, parent):
        super(Test, self).__init__(parent)
        pass
    def __del__(self):
        pass
    def ButtonClicked(self, event):
        dlg = wx.Dialog(None, wx.ID_ANY, "点击窗口")
        dlg.Show()
        pass
if __name__ == "__main__":
    app = wx.App()
    window = Test(None)
    window.Show(True)
    app.MainLoop()
    pass
