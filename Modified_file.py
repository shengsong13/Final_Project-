import wx 
# -------- new: we need os module to handle path, dir stuffs-----------
import os       
 
# ------- new: make our own id numbers --------------
ID_OPEN = 100      
ID_SAVE = 101          
ID_EXIT = 102
ID_ABOUT = 200
 
class SimpleEditor(wx.Frame):
        def __init__(self, parent, id, title):
                wx.Frame.__init__(self, parent, id, title, size = (700, 600))
                
                # ---------------------create a text area ----------------------
                self.text = wx.TextCtrl(self, 1, style=wx.TE_MULTILINE)
                
                # ---------------------create a status bar ---------------------
                self.CreateStatusBar()
                
                # ---------------------create a menu bar -----------------------
                menuBar = wx.MenuBar()
        
                # ---------------------create a menu ---------------------------        
                # making two new menus                
                menuFile = wx.Menu()
                menuHelp = wx.Menu()                
 
                menuFile.Append(ID_OPEN, '&Open', 'open a file')
                menuFile.Append(ID_SAVE, '&Save', 'save the file')
                # ----------------------------------------------------------------------
 
                # adding a separator to separate the menu list
                menuFile.AppendSeparator()
        
                # ------------- Changed: use our own id instead wx.ID_ANY ------------------ 
                
                #menuFile.Append(wx.ID_ANY, 'E&xit', 'terminate the program')                
                #menuHelp.Append(wx.ID_ANY, 'A&bout', 'info about this program')
 
                menuFile.Append(ID_EXIT, 'E&xit', 'terminate the program')                
                menuHelp.Append(ID_ABOUT, 'A&bout', 'info about this program')                
                # -------------------------------------------------------------------------
 
                # add the menu list we made to menu bar
                # This will show 'File' on the menu bar
                menuBar.Append(menuFile, '&File')
                # This will show 'Help' on the menu bar
                menuBar.Append(menuHelp, '&Help')
                
                # Last step, set the menu bar
                self.SetMenuBar(menuBar)
                        
                # ------------------------- new: 4 events handler -------------------------------
                
                wx.EVT_MENU(self, ID_OPEN, self.OnOpen)
                wx.EVT_MENU(self, ID_SAVE, self.OnSave)
                wx.EVT_MENU(self, ID_EXIT, self.OnExit)
                wx.EVT_MENU(self, ID_ABOUT, self.OnAbout)
 
        # ---------------------- new: Declare 4 functions for the events--------------------------
                
        # open file when you click File -> open
        def OnOpen(self, event):
                # open a file using wx.FileDialog
                # wx.FileDialog(self, parent, message = FileSelectorPromptStr, defaultDir = EmptyString, defaultFile = EmptyString,                 
                #                           wildcard = FileSelectorDefaultWildcardStr, style = FD_DEFAULT_STYLE, pos = DefaultPosition)  
                dlg = wx.FileDialog(self, message = 'Choose a file', defaultDir = '',
                                                    defaultFile = '', wildcard = '*.*', style = wx.OPEN)
                # if we click 'OK' button it do something                
                if dlg.ShowModal() == wx.ID_OK:
                        # get the file name and directory 
                        self.filename = dlg.GetFilename()
                        self.dirname = dlg.GetDirectory()
                        print self.dirname
                        # add the directory path and file name
                        f = open(os.path.join(self.dirname, self.filename),'r')
                        # read the file , show on the text area 
                        self.text.SetValue(f.read())
                        f.close()
                dlg.Destroy()
 
        # save file when you click File -> save
        def OnSave(self, event):
                # get the current value from text area
                itcontains = self.text.GetValue()
                # overwrite the same file with current value 
                f = open(os.path.join(self.dirname, self.filename), 'w')
                f.write(itcontains)
 
                f.close()
 
        # exit program when you click File -> exit
        def OnExit(self, event):
                # close the frame
                app = wx.PySimpleApp()
                self.Close(True)
                
        # about this program Help -> About
        def OnAbout(self, event):
                # make a message dialog 
                # wx.MessageDialog(self, parent, message, caption=MessageBoxCaptionStr, 
                #                                 style=wxOK|wxCANCEL|wxCENTRE, pos=DefaultPosition)  
                dlg = wx.MessageDialog(self, message = 'A simple editor created by wxPython!\n'
                                                          'author : sheng_song \n date : Aug 16, 2018',  caption = 'About this program', style = wx.OK)
                # show the message dialog
                dlg.ShowModal()
                # we destroy it when finished
                dlg.Destroy()                        
        # ----------------------------------------------------------------------------------------------
        
if __name__=='__main__':
        app = wx.PySimpleApp()
        frame = SimpleEditor(None, wx.ID_ANY, 'Change Input File')
        frame.Show()
        app.MainLoop()