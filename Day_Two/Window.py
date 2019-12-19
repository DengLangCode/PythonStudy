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
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):
    """构造函数"""
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)
        """self相当于C++中的this指针"""
        self.m_panel5 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel5.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_panel5.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        gSizer1.Add(self.m_panel5, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel6 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel6.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        gSizer1.Add(self.m_panel6, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel7 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel7.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWFRAME))

        gSizer1.Add(self.m_panel7, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel8 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel8.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        gSizer1.Add(self.m_panel8, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(gSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
if __name__ == "__main__":
    app = wx.App()
    window = MyFrame1(None)
    window.Show(True)
    app.MainLoop()
    pass