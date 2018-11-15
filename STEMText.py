import wx
import tab

class MyFrame(wx.Frame):
    def on_about(self, event):
        dlg = wx.MessageDialog(self, "U fuckin wot, m8?", "About TechText", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def on_exit(self, event):
        self.Close(True)

    def on_saveas(self, event):
        print("Something")

    def on_dark(self, event):
        print("Something")

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 500))
        #The Tabs
        panel = wx.Panel(self)
        notebook = tab.NotebookPanel(panel)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.ALL | wx.EXPAND, 5)
        panel.SetSizer(sizer)
        #The Menu
        menubar = wx.MenuBar()
        filemenu = wx.Menu()
        aboutitem = filemenu.Append(wx.ID_ABOUT, "About", "Information about this program")
        self.Bind(wx.EVT_MENU, self.on_about, aboutitem)
        filemenu.AppendSeparator()
        saveasitem = filemenu.Append(wx.ID_SAVEAS, "Save As", "Save this document as a new file")
        self.Bind(wx.EVT_MENU, self.on_saveas, saveasitem)
        filemenu.AppendSeparator()
        exititem = filemenu.Append(wx.ID_EXIT, "Exit", "Terminate the program")
        self.Bind(wx.EVT_MENU, self.on_exit, exititem)
        filemenu.AppendSeparator()
        menubar.Append(filemenu, "&File")

        editmenu = wx.Menu()
        menubar.Append(editmenu, "&Edit")

        viewmenu = wx.Menu()
        darkitem = viewmenu.Append(wx.ID_APPLY, "Dark Theme", "Set Dark Theme")
        self.Bind(wx.EVT_MENU, self.on_dark, darkitem)
        menubar.Append(viewmenu, "&View")

        spec_char_menu = wx.Menu()
        menubar.Append(spec_char_menu, "&Special Characters")

        graphmenu = wx.Menu()
        menubar.Append(graphmenu, "&Graphs")

        codemenu = wx.Menu()
        menubar.Append(codemenu, "&Code")

        self.SetMenuBar(menubar)
        self.Layout()
        self.Show(True)


app = wx.App(False)
frame = MyFrame(None, 'TechText')
frame.Center()
app.MainLoop()
