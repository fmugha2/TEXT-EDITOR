import wx
import tab
#import TableToolbox

class MyPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.frame = parent
        self.widgetSizer = wx.BoxSizer(wx.VERTICAL)
        notebook = tab.NotebookPanel(self)
        self.mainsizer = wx.BoxSizer(wx.VERTICAL)
        self.mainsizer.Add(notebook, 1, wx.ALL | wx.EXPAND, 5)
        self.mainsizer.Add(self.widgetSizer, 0, wx.CENTER | wx.ALL, 10)
        self.SetSizer(self.mainsizer)

"""
    This method adds the toolbox that is used to add tables, but I'm not
    pushing it yet because it doesn't really do anything atm.
    
    def add_table(self):
        #new_button = wx.Button(self, label="notin", name="IDK")
        toolbox = TableToolbox.TableToolbox(self)
        self.widgetSizer.Add(toolbox, 0, wx.ALL, 5)
        self.frame.fSizer.Layout()
"""



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

    def on_table(self, event):
        self.panel.add_table()



    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 500))


        #The Tabs
        self.panel = MyPanel(self)
        self.fSizer = wx.BoxSizer(wx.VERTICAL)
        self.fSizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(self.fSizer)

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
        tableitem = graphmenu.Append(wx.ID_APPLY, "Table Toolbox", "Open the toolbox used for creating tables.")
        self.Bind(wx.EVT_MENU, self.on_table, tableitem)
        menubar.Append(graphmenu, "&Graphs")

        codemenu = wx.Menu()
        menubar.Append(codemenu, "&Code")

        self.SetMenuBar(menubar)
        self.Layout()
        self.Show(True)
        #wx.lib.inspection.InspectionTool().Show()


app = wx.App(False)
frame = MyFrame(None, 'TechText')
frame.Center()
app.MainLoop()
