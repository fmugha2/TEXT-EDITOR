import wx
import tab
import table

class WidgetPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.frame = parent
        self.widgetSizer = wx.BoxSizer(wx.VERTICAL)
        self.notebook = tab.NotebookPanel(self)
        self.mainsizer = wx.BoxSizer(wx.VERTICAL)
        buttonsizer = wx.BoxSizer(wx.HORIZONTAL)

        add_tab_button = wx.Button(self, label="Add Tab")
        add_tab_button.Bind(wx.EVT_BUTTON, self.add_tab)
        buttonsizer.Add(add_tab_button)

        remove_tab_button = wx.Button(self, label="Remove Tab")
        remove_tab_button.Bind(wx.EVT_BUTTON, self.remove_tab)
        buttonsizer.Add(remove_tab_button)

        self.mainsizer.Add(buttonsizer)

        self.mainsizer.Add(self.notebook, 1, wx.ALL | wx.EXPAND, 5)
        self.mainsizer.Add(self.widgetSizer, 0, wx.CENTER | wx.ALL, 10)
        self.SetSizer(self.mainsizer)

    # Creates a table toolbox.
    def add_table_toolbox(self):
        toolbox = TableToolbox(self)
        self.widgetSizer.Add(toolbox, 0, wx.ALL, 5)
        self.frame.fSizer.Layout()
        self.parent_layout()

    def parent_layout(self):
        self.frame.fSizer.Layout()

    # The method called by the create tab button. Creates a tab
    def add_tab(self, event):
        self.notebook.create_tab(name = "New Tab")

    # The method called by the remove tab button. NEEDS TO BE IMPLEMENTED
    def remove_tab(self, event):
        print("Something")

class TableToolbox(wx.Panel):

    def __init__(self, parent: WidgetPanel):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.t = table.Table
        self.rows = 1
        self.columns = 1
        self.pframe = parent
        sizerv = wx.BoxSizer(wx.VERTICAL)

        sizer_row1 = wx.BoxSizer(wx.HORIZONTAL)
        sizerv.Add(sizer_row1, wx.EXPAND)

        add_table_button = wx.Button(self, label="Add a Table", name="Table Adder")
        self.Bind(wx.EVT_BUTTON, self.add_table, add_table_button)
        sizer_row1.Add(add_table_button)

        remove_table_button = wx.Button(self, label = "Remove Table", name = "Table Remover")
        self.Bind(wx.EVT_BUTTON, self.remove_table, remove_table_button)
        sizer_row1.Add(remove_table_button)

        remove_toolbox_button = wx.Button(self, label="X", name="Toolbox Remover")
        self.Bind(wx.EVT_BUTTON, self.remove_toolbox, remove_toolbox_button)
        sizer_row1.Add(remove_toolbox_button)
        self.SetSizer(sizerv)

        sizer_row2 = wx.BoxSizer(wx.HORIZONTAL)
        sizerv.Add(sizer_row2, wx.EXPAND)

        add_table_row_button = wx.Button(self, label="Rows + 1", name="Row Add")
        self.Bind(wx.EVT_BUTTON, self.increase_rows, add_table_row_button)
        sizer_row2.Add(add_table_row_button)

        remove_table_row_button = wx.Button(self, label="Rows - 1", name="Row Subtract")
        self.Bind(wx.EVT_BUTTON, self.decrease_rows, remove_table_row_button)
        sizer_row2.Add(remove_table_row_button)

        self.row_num_display = wx.TextCtrl(self, 1, style=wx.TE_CENTER | wx.TE_READONLY, value=self.rows.__str__())
        sizer_row2.Add(self.row_num_display, 1, wx.EXPAND)

        sizer_row3 = wx.BoxSizer(wx.HORIZONTAL)
        sizerv.Add(sizer_row3, wx.EXPAND)

        add_table_column_button = wx.Button(self, label="Columns + 1", name="Column Add")
        self.Bind(wx.EVT_BUTTON, self.increase_columns, add_table_column_button)
        sizer_row3.Add(add_table_column_button)

        remove_table_column_button = wx.Button(self, label="Columns - 1", name="Column Subtract")
        self.Bind(wx.EVT_BUTTON, self.decrease_columns, remove_table_column_button)
        sizer_row3.Add(remove_table_column_button)

        self.column_num_display = wx.TextCtrl(self, 1, style=wx.TE_CENTER | wx.TE_READONLY, value=self.columns.__str__())
        sizer_row3.Add(self.column_num_display, 1, wx.EXPAND)

    # Removes the toolbox, and fits the window back to its normal state.
    def remove_toolbox(self, event):
        self.Destroy()
        self.pframe.Layout()
        self.pframe

    # Adds a table to the parent class's sizer.
    def add_table(self, event):
        self.t = table.Table(self.pframe, self.rows, self.columns)
        self.pframe.mainsizer.Add(self.t)
        self.pframe.parent_layout()

    def remove_table(self, event):
        self.t.Destroy()
        self.pframe.parent_layout()

    # increment the number of rows
    def increase_rows(self, event):
        self.rows += 1
        self.row_num_display.SetValue(self.rows.__str__())

    # Decrement the number of rows
    def decrease_rows(self, event):
        if self.rows > 1:
            self.rows -= 1
            self.row_num_display.SetValue(self.rows.__str__())

    # Increment the number of columns
    def increase_columns(self, event):
        self.columns += 1
        self.column_num_display.SetValue(self.columns.__str__())

    # Decrement the number of columns
    def decrease_columns(self, event):
        if self.columns > 1:
            self.columns -= 1
            self.column_num_display.SetValue(self.columns.__str__())

class MenuFrame(wx.Frame):

    #Displays a message. Called by the "about" menu item.
    def on_about(self, event):
        dlg = wx.MessageDialog(self, "STEMText is pretty neat, I guess.", "About TechText", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    #closes the program. Called by the "close" menu item
    def on_exit(self, event):
        self.Close(True)

    #NEED IMPLEMENTATION
    def on_saveas(self, event):
        print("Something")

    #NEED IMPLEMENTATION
    def on_dark(self, event):
        print("Something")

    #This method uses the Frame's panel to create a table toolbox object. Called by the "table toolbox" menu item.
    def on_table(self, event):
        self.panel.add_table_toolbox()


    #STEMText's main class's init method. Instantiates the menu bar and the MyPanel object.
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(1000, 600))


        #The Tabs
        self.panel = WidgetPanel(self)
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


app = wx.App(False)
frame = MenuFrame(None, 'TechText')
frame.Center()
app.MainLoop()
