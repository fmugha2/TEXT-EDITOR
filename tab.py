import wx

class TabPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        self.control = wx.TextCtrl(self, size = (465, 405), style = wx.TE_MULTILINE)



class NotebookPanel(wx.Notebook):

    def createTab(self, name):
        tab = TabPanel(self)
        tab.SetBackgroundColour(wx.LIGHT_GREY)
        self.AddPage(tab, name)

    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=wx.BK_DEFAULT)

        self.createTab(name = "Tab 1")
        self.createTab(name = "Tab 2")


        """
        THIS IS HOW YOU ADD AN IMAGE TO A PANEL, COULD BE HELPFUL
        
        il = wx.ImageList(16, 16)
        idx1 = il.Add(images.Smiles.GetBitmap())
        self.AssignImageList(il)
        self.SetPageImage(0, idx1)
        """

        def OnPageChanged(self, event):
            old = event.GetOldSelection()
            new = event.GetSelection()
            sel = self.GetSelection()
            print('OnPageChanged,  old:%d, new:%d, sel:%d\n' % (old, new, sel))
            event.Skip()

        def OnPageChanging(self, event):
            old = event.GetOldSelection()
            new = event.GetSelection()
            sel = self.GetSelection()
            print('OnPageChanging, old:%d, new:%d, sel:%d\n' % (old, new, sel))
            event.Skip()



