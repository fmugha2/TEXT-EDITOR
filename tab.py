import wx


class TabPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        sizerv = wx.BoxSizer(wx.VERTICAL)
        sizerh = wx.BoxSizer(wx.HORIZONTAL)
        sizerv.Add(sizerh, wx.EXPAND)
        sizerv.Add(wx.TextCtrl(self, 1, style = wx.TE_MULTILINE), 1, wx.EXPAND)
        self.SetSizerAndFit(sizerv)


class NotebookPanel(wx.Notebook):

    def create_tab(self, name):
        tab = TabPanel(self)
        self.AddPage(tab, name)

    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=wx.BK_DEFAULT)

        self.create_tab(name = "New Tab")


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



