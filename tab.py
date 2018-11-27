import wx
import wx.lib.agw.aui as aui


class TabPanel(wx.Panel):
    # Creates a new tab and sets it to expand to fill it's container
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        sizerv = wx.BoxSizer(wx.VERTICAL)
        sizerh = wx.BoxSizer(wx.HORIZONTAL)
        sizerv.Add(sizerh, wx.EXPAND)
        self.text_control = wx.TextCtrl(self, 1, style=wx.TE_MULTILINE)
        sizerv.Add(self.text_control, 1, wx.EXPAND)
        self.SetSizerAndFit(sizerv)


class NotebookPanel(aui.AuiNotebook):

    def load(self, name):
        tab = TabPanel(self)
        tab.text_control.LoadFile(name, fileType=wx.TEXT_TYPE_ANY)
        self.AddPage(tab, name)

    def save(self, name):
        tab: TabPanel
        tab = self.GetCurrentPage()
        tab.text_control.SaveFile(name, fileType=wx.TEXT_TYPE_ANY)

    # Creates a tab and adds it to the notebook
    def create_tab(self, name):
        tab = TabPanel(self)
        self.AddPage(tab, name)

    # initializes the notebook and adds a page to it
    def __init__(self, parent):
        aui.AuiNotebook.__init__(self, parent, id=wx.ID_ANY, style=
            aui.AUI_NB_TOP |
            aui.AUI_NB_TAB_SPLIT |
            aui.AUI_NB_TAB_MOVE |
            aui.AUI_NB_SCROLL_BUTTONS |
            aui.AUI_NB_CLOSE_ON_ALL_TABS |
            aui.AUI_NB_MIDDLE_CLICK_CLOSE)

        self.create_tab(name="New Tab")

    """
    These two methods are required for the pages to save the information on tabs
    when you change to a different tab. They seem like they are not implemented, but they are.
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
