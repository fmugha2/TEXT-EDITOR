import wx
import wx.grid


class Table(wx.grid.Grid):
    def __init__(self, parent, rows, columns):
        wx.grid.Grid.__init__(self, parent=parent)
        self.pframe = parent
        self.CreateGrid(rows, columns)
        self.SetRowSize(0, 15)
        self.SetColSize(0, 40)
        # https://docs.wxpython.org/grid_overview.html#grid-overview


