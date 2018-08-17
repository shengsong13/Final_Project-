#coding=utf-8
#!python
import wx
import final_function
from Modified_file import SimpleEditor
import wx.lib.scrolledpanel
import os

class TestFrame(wx.Frame):
    def __init__(self):
        ID_OPEN = 100      
        wx.Frame.__init__(self, None, -1, "Hello World", size = (710,800))
        self.scroll = wx.ScrolledWindow(self, -1, size= (1000, 750))
        self.scroll.SetScrollbars(1,1,400,800)
        panel = wx.lib.scrolledpanel.ScrolledPanel(self.scroll, -1, size =(1000,800))
        panel.SetupScrolling()


        
        # ---------------------create a menu bar -----------------------
        menuBar = wx.MenuBar()
               
        menuFile = wx.Menu()             

        menuFile.Append(ID_OPEN, '&Change the input file', 'open a file')

        menuBar.Append(menuFile, '&Tools')

        self.SetMenuBar(menuBar)
        # ----------------------------------------------------------------------
        wx.EVT_MENU(self, ID_OPEN, self.OnOpen)


        # First create the controls header
        topLbl = wx.StaticText(panel, -1, "Generate text file")
        topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        # state list
        list_name = []
        r = final_function.listdir("/home/mphyg002/Desktop/test_python/input2", list_name)
        filelist_stat = final_function.spilts(r)
        self.statelistbox = wx.CheckListBox(panel, -1, (200,20),(250,120), filelist_stat) 
        # tran list
        tran_list = [] 
        rs = final_function.listdir2("/home/mphyg002/Desktop/test_python/input2", tran_list)
        filelist = final_function.spilts(rs)
        self.tranlistbox = wx.CheckListBox(panel, -1, (200,20),(250,120), filelist,wx.LB_SINGLE) 
        # temp staff
        saveBtn = wx.Button(panel, -1, "Display Text")
        cancelBtn = wx.Button(panel, -1, "Generate input file")
        clearBtn = wx.Button(panel, -1, "Clear")


        self.label_temp = wx.StaticText(panel, -1, 'Temperature:  ')
        self.Text_temp = wx.TextCtrl(panel, -1, size=(100, 28), style=wx.TE_MULTILINE) 
        self.Bind(wx.EVT_BUTTON, self.GetValue, saveBtn)
        self.Bind(wx.EVT_BUTTON, self.Clear, clearBtn)
        self.Bind(wx.EVT_BUTTON, self.define_root, cancelBtn)
        # range staff
        self.label_range = wx.StaticText(panel, -1, 'Range')
        self.Text_range = wx.TextCtrl(panel, -1, size=(50, 28), style=wx.TE_MULTILINE)
        self.label_range_1 = wx.StaticText(panel, -1, ' to ')
        self.Text_range_1 = wx.TextCtrl(panel, -1, size=(50, 28),style=wx.TE_MULTILINE)
        # cooling staff
        self.label_tempmex = wx.StaticText(panel, -1, 'tempmex:', pos = (210, 135))
        self.label_cqooling = wx.StaticText(panel, -1, 'ntemps:', pos = (340, 135))
        self.Text_cooling_1 = wx.TextCtrl(panel, -1, size=(80, 28), pos=(280,130),style=wx.TE_MULTILINE)
        self.Text_cooling_2 = wx.TextCtrl(panel, -1, size=(80, 28), pos=(400,130),style=wx.TE_MULTILINE)
        #type of spectra staffb
        self.spectra = wx.RadioBox(panel, -1, "Type of spectra", (100, 100), wx.DefaultSize,  
                        ["No spectra                  ",
                         "lifetime                    ", 
                         "emission                    ",
                         "absorption                  "], 4, wx.RA_SPECIFY_COLS) 
        self.ProfileType = wx.RadioBox(panel, -1, "Profile Type", (100, 100), wx.DefaultSize,  
                        ["No profile type            ",
                         "Gaus0           ", 
                         "Guassian          ",
                         "Sticks            ",
                         "Rect                ",
                         "Lorentzian             ",
                         "Dopp10             ",
                         "Voigt             ",
                         "Voi-Quad          ",
                         "Voi-fast          ",
                         "Voi-norm        "], 5, wx.RA_SPECIFY_COLS)
        # Species
        self.label_species1 = wx.StaticText(panel, -1, 'N:  ')
        self.label_species2 = wx.StaticText(panel, -1, 'Gamma:  ')
        self.label_species3 = wx.StaticText(panel, -1, 'Delta: ')
        self.label_species4 = wx.StaticText(panel, -1, 'TO: ')
        self.label_species5 = wx.StaticText(panel, -1, 'PO: ')
        self.label_species6 = wx.StaticText(panel, -1, 'Ratio: ')
        self.label_species7 = wx.StaticText(panel, -1, 'File: ')
        self.Text_species1 = wx.TextCtrl(panel, -1, size=(50, 28),style=wx.TE_MULTILINE)
        self.Text_species2 = wx.TextCtrl(panel, -1, size=(50, 28),style=wx.TE_MULTILINE)
        self.Text_species3 = wx.TextCtrl(panel, -1, size=(50, 28),style=wx.TE_MULTILINE)
        self.Text_species4 = wx.TextCtrl(panel, -1, size=(50, 28),style=wx.TE_MULTILINE)
        self.Text_species5 = wx.TextCtrl(panel, -1, size=(50, 28),style=wx.TE_MULTILINE)
        self.Text_species6 = wx.TextCtrl(panel, -1, size=(50, 28),style=wx.TE_MULTILINE)
        self.Text_species7 = wx.TextCtrl(panel, -1, size=(50, 28),style=wx.TE_MULTILINE)
        # All information
        self.Text_All = wx.TextCtrl(panel, -1, size=(500, 200), style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.label_Name = wx.StaticText(panel, -1, "Name of input file:  ")
        self.Text_Name = wx.TextCtrl(panel, -1, size=(100, 28), style=wx.TE_MULTILINE)
        # Main Sizer 
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(topLbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(panel), 0,
                wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
        #row one sizer
        row1boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        #temp sizer
        tempbox = wx.StaticBox(panel, -1, "temp")
        tempsizer = wx.StaticBoxSizer(tempbox, wx.HORIZONTAL)
        tempsizer.Add((40,40), 0, wx.ALL, 2)
        tempsizer.Add(self.label_temp, 0, wx.ALL, 2)
        tempsizer.Add(self.Text_temp, 0, wx.ALL, 2)
        tempsizer.Add((40,40), 0, wx.ALL, 2)
        # range sizer
        rangebox = wx.StaticBox(panel, -1, "range")
        rangesizer = wx.StaticBoxSizer(rangebox, wx.HORIZONTAL)
        rangesizer.Add((40,40), 0, wx.ALL, 2)
        rangesizer.Add(self.label_range, 0, wx.ALL, 2)
        rangesizer.Add(self.Text_range, 0, wx.ALL, 2)
        rangesizer.Add(self.label_range_1, 0, wx.ALL, 2)
        rangesizer.Add(self.Text_range_1, 0, wx.ALL, 2)
        rangesizer.Add((40,40), 0, wx.ALL, 2)
        # add range and temp to row one sizer
        row1boxsizer.Add((40,40), 0, wx.ALL, 2)
        row1boxsizer.Add(tempsizer)
        row1boxsizer.Add((40,40), 0, wx.ALL, 2)
        row1boxsizer.Add(rangesizer)
        row1boxsizer.Add((40,40), 0, wx.ALL, 2)
        mainSizer.Add(row1boxsizer, 0, wx.EXPAND|wx.BOTTOM, 10)
        # row tow has one static box sizer
        row2boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        coolingbox = wx.StaticBox(panel, -1, "cooling")
        coolingsizer = wx.StaticBoxSizer(coolingbox, wx.HORIZONTAL)
        coolingsizer.Add((125,40), 0, wx.ALL, 2)
        coolingsizer.Add(self.label_tempmex, 0, wx.ALL, 2)
        coolingsizer.Add(self.Text_cooling_1, 0, wx.ALL, 2)
        coolingsizer.Add((50,40), 0, wx.ALL, 2)
        coolingsizer.Add(self.label_cqooling, 0, wx.ALL, 2)
        coolingsizer.Add(self.Text_cooling_2, 0, wx.ALL, 2)
        coolingsizer.Add((125,40), 0, wx.ALL, 2)
        row2boxsizer.Add((40,40), 0, wx.ALL, 2)
        row2boxsizer.Add(coolingsizer)
        row2boxsizer.Add((40,40), 0, wx.ALL, 2)
        
        # type of spectra
        row3boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        row3boxsizer.Add((40,40), 0, wx.ALL, 2)
        row3boxsizer.Add(self.spectra, 0, wx.ALL, 2)
        mainSizer.Add(row3boxsizer, 0,  wx.EXPAND|wx.BOTTOM, 10)
        # Profile type
        row5boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        row5boxsizer.Add((40,40), 0, wx.ALL, 2)
        row5boxsizer.Add(self.ProfileType, 0, wx.ALL, 2)
        mainSizer.Add(row5boxsizer, 0,  wx.EXPAND|wx.BOTTOM, 10)
        # species
        row4boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        speciesbox = wx.StaticBox(panel, -1, "Species")
        speciessizer = wx.StaticBoxSizer(speciesbox, wx.VERTICAL)
        species1sizer = wx.BoxSizer(wx.HORIZONTAL)
        species2sizer = wx.BoxSizer(wx.HORIZONTAL)
        species1sizer.Add((45,40), 0, wx.ALL, 2)
        species1sizer.Add(self.label_species1)
        species1sizer.Add(self.Text_species1)
        species1sizer.Add((45,40), 0, wx.ALL, 2)
        species1sizer.Add(self.label_species2)
        species1sizer.Add(self.Text_species2)
        species1sizer.Add((45,40), 0, wx.ALL, 2)

        species1sizer.Add(self.label_species3)
        species1sizer.Add(self.Text_species3)
        species1sizer.Add((45,40), 0, wx.ALL, 2)
        species1sizer.Add(self.label_species4)
        species1sizer.Add(self.Text_species4)
        species1sizer.Add((45,40), 0, wx.ALL, 2)

        species2sizer.Add((75,40), 0, wx.ALL, 2)
        species2sizer.Add(self.label_species5)
        species2sizer.Add(self.Text_species5)
        species2sizer.Add((75,40), 0, wx.ALL, 2)
        species2sizer.Add(self.label_species6)
        species2sizer.Add(self.Text_species6)
        species2sizer.Add((75,40), 0, wx.ALL, 2)

        species2sizer.Add(self.label_species7)
        species2sizer.Add(self.Text_species7)
        species2sizer.Add((75,40), 0, wx.ALL, 2)

        speciessizer.Add(species1sizer, 0, wx.ALL, 2)
        speciessizer.Add(species2sizer, 0, wx.ALL, 2)
        row4boxsizer.Add((40,40), 0, wx.ALL, 2)
        row4boxsizer.Add(speciessizer, 0, wx.ALL, 2)
        row4boxsizer.Add((40,40), 0, wx.ALL, 2)

        #state list section
        statebox = wx.StaticBox(panel, -1, "State Section")
        statesizer = wx.StaticBoxSizer(statebox, wx.HORIZONTAL)
        statesizer.Add((20,20), 0, wx.ALL, 2)
        statesizer.Add(self.statelistbox, 0, wx.ALL, 2)
        statesizer.Add((20,20), 0, wx.ALL, 2)

        tranbox = wx.StaticBox(panel, -1, "Tran Section")
        transizer = wx.StaticBoxSizer(tranbox, wx.HORIZONTAL)
        transizer.Add((20,20), 0, wx.ALL, 2)
        transizer.Add(self.tranlistbox, 0, wx.ALL, 2)
        transizer.Add((20,20), 0, wx.ALL, 2)
        row6boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        row6boxsizer.Add((40,40), 0, wx.ALL, 2)
        row6boxsizer.Add(statesizer, 0, wx.ALL, 2)
        row6boxsizer.Add(transizer, 0, wx.ALL, 2)

        mainSizer.Add(row6boxsizer, 0,  wx.EXPAND|wx.BOTTOM, 10)
        mainSizer.Add(row4boxsizer, 0,  wx.EXPAND|wx.BOTTOM, 10)
        mainSizer.Add(row2boxsizer, 0, wx.EXPAND|wx.BOTTOM, 10)
        #button sizer
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((100,40), 0, wx.ALL, 2)
        btnSizer.Add(saveBtn)
        btnSizer.Add((100,20), 0, wx.ALL, 2)
        btnSizer.Add((100,20), 0, wx.ALL, 2)
        btnSizer.Add(clearBtn)
        mainSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)

        #All text file
        Alltextbox = wx.StaticBox(panel, -1, "Final Text")
        textsizer = wx.StaticBoxSizer(Alltextbox, wx.HORIZONTAL)
        textsizer.Add((45,240), 0, wx.ALL, 2)
        textsizer.Add(self.Text_All,0, wx.CENTER)
        textsizer.Add((45,20), 0, wx.ALL, 2)
        row7sizer = wx.BoxSizer(wx.HORIZONTAL)
        row7sizer.Add((45,30), 0, wx.ALL, 2)
        row7sizer.Add(textsizer)
        row7sizer.Add((45,30), 0, wx.ALL, 2)
        mainSizer.Add(row7sizer, 0, wx.EXPAND|wx.BOTTOM, 10)

        Namesizer = wx.BoxSizer(wx.HORIZONTAL)
        Namesizer.Add((70, 60), 0, wx.ALL, 2)
        Namesizer.Add(self.label_Name, 0, wx.CENTER)
        Namesizer.Add(self.Text_Name, 0, wx.CENTER)
        Namesizer.Add((45, 60), 0, wx.ALL, 2)
        Namesizer.Add(cancelBtn, 0, wx.CENTER)

        mainSizer.Add(Namesizer)


        panel.SetSizer(mainSizer)
        #mainSizer.Fit(self)
        #mainSizer.SetSizeHints(self)

    def OnOpen(self, event):
        app = wx.App()
        frame = SimpleEditor(None, wx.ID_ANY, 'Simple Editor')
        frame.Show()
        app.MainLoop()

    def Clear(self, event):
        self.Text_All.Clear()

    def define_root(self, event):
        dlg = wx.DirDialog(self, message = 'Choose a file',  style = wx.DD_DEFAULT_STYLE)
        # if we click 'OK' button it do something                
        if dlg.ShowModal() == wx.ID_OK:
            self.dirname = dlg.GetPath()
            print self.dirname
            if os.path.exists(self.dirname):
                full_name = self.dirname + "/"+ self.Text_Name.GetValue() + ".inp"
                file = open(full_name, "w")
                file.write(self.Text_All.GetValue())
                alert = wx.MessageDialog(None, u"Generate Success, would you like to close?", 
                                         u"Congratulation")
                if alert.ShowModal() == wx.ID_OK:
                    self.Close(True)
                alert.Destroy()
        dlg.Destroy()

    def GetValue(self,event):
        self.Text_All.Clear()
        imsage = ""
        Temp_input = self.Text_temp.GetValue()
        if len(Temp_input)!=0:
            imsage = "Temperature  %s  \n\n" % (Temp_input)
        Range_input = self.Text_range.GetValue()
        Range_input_1 = self.Text_range_1.GetValue()
        if len(Temp_input)!=0:
            imsage += "Range  %s %s  \n\n" % (Range_input, Range_input_1)
        spectra_input = self.spectra.GetStringSelection()
        if spectra_input != "No spectra                  ":
            imsage += "%s \n\n" % (spectra_input)
        profileTpye_input = self.ProfileType.GetStringSelection()
        if profileTpye_input != "No profile type            ":
            imsage += "%s \n\n" % (profileTpye_input)

        state_input = self.statelistbox.GetCheckedStrings()
        if len(state_input) == 1:
            imsage += "States %s \n\n" % (state_input[0])
        if len(state_input) > 1:
            imsage += "States \n"
            for i in range(len(state_input)):
                imsage += "   %s \n" % (state_input[i])
            imsage += "end \n\n"

        tran_input = self.tranlistbox.GetCheckedStrings()
        if len(tran_input) == 1:
            imsage += "Transections %s \n\n" % (tran_input[0])
        if len(tran_input) > 1:
            imsage += "Transections \n"
            for i in range(len(tran_input)):
                imsage += "   %s \n" % (tran_input[i])
            imsage += "end \n\n"

        species_content = ""
        if len(self.Text_species1.GetValue()) != 0:
            species_content += "    N  %s \n" % (self.Text_species1.GetValue())
        if len(self.Text_species2.GetValue()) != 0:
            species_content += "    Gamma  %s \n" % (self.Text_species2.GetValue())
        if len(self.Text_species3.GetValue()) != 0:
            species_content += "    Delta  %s \n" % (self.Text_species3.GetValue())
        if len(self.Text_species4.GetValue()) != 0:
            species_content += "    TO  %s \n" % (self.Text_species4.GetValue())
        if len(self.Text_species5.GetValue()) != 0:
            species_content += "    PO  %s \n" % (self.Text_species5.GetValue())
        if len(self.Text_species6.GetValue()) != 0:
            species_content += "    Ratio  %s \n" % (self.Text_species6.GetValue())
        if len(self.Text_species7.GetValue()) != 0:
            species_content += "    File  %s \n" % (self.Text_species7.GetValue())
        if len(species_content) != 0:
            imsage += "Species \n%s end \n\n" % (species_content)
        cooling_content = ""
        if len(self.Text_cooling_1.GetValue()) != 0:
            cooling_content += "    Tempmex  %s \n" % (self.Text_cooling_1.GetValue())
        if len(self.Text_cooling_2.GetValue()) != 0:
            cooling_content += "    ntemps  %s \n" % (self.Text_cooling_2.GetValue())
        if len(cooling_content) != 0:
            imsage += "Cooling \n%s end \n\n" % (cooling_content)
        self.Text_All.AppendText(imsage)



        

app = wx.App()
TestFrame().Show()
app.MainLoop()



