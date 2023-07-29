
import time

def OSCode_SAPXPG(self, app):
    # Configure the tags to set the foreground color
    self.textboxtk.tag_configure("pass", foreground='#00f18b')
    self.textboxtk.tag_configure("fail", foreground='red')
    self.textboxtk.tag_config('gcolor', foreground='#00f18b')
    self.textboxtk.tag_config('rcolor', foreground='red')
    self.textboxtk.tag_config('ycolor', foreground='yellow')

    #Defining values for default execution
    cmd = "whoami"
    ExpName = "SAPKILN GATEWAY EXP SAPXPG"
    CmdName = "SAPKILN GE"
    value = 0.0
    self.progressbar.set(value)
    self.textboxtk.delete("1.0", "end")
    Module = """Module - OS Commands Execution - SAPXPG\n-------------------------"""
    self.textboxtk.insert("insert", Module + "\n")
    value = value + 0.1 #1
    self.progressbar.set(value)
    app.update_idletasks()
    if(self.session is None):
        self.textboxtk.insert("insert", '\u2717 '+"Please log in before executing this module \n", 'rcolor')
        self.textboxtk.insert("insert", "\n")
        value = value + 0.9
        self.progressbar.set(value)
        app.update_idletasks()
    else:
        self.textboxtk.insert("insert", '\u2713 '+"Sucessfully detected loged in session\n", 'ycolor')
        if(self.entry.get()):
            userinput = self.entry.get()
            split_string = userinput.split(";")
            cmd = split_string[0]
            ExpName = split_string[1].upper()
            CmdName = split_string[2].upper()
            self.textboxtk.insert("insert", "Executing module with command " + cmd  + "....\n", 'ycolor')
            value = value + 0.2 #3
            self.progressbar.set(value)
            app.update_idletasks()
        else:
            UserName = self.session.Info.User
            self.textboxtk.insert("insert", "Executing module with deafult command " + cmd  + "....\n", 'ycolor')
            value = value + 0.2 #3
            self.progressbar.set(value)
            app.update_idletasks()
        value = value + 0.1 #4
        self.progressbar.set(value)
        app.update_idletasks()
        try:
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "SM59"
            self.session.findById("wnd[0]").sendVKey(0)
            time.sleep(1)
            self.textboxtk.insert("insert", '\u2713 '+"Executed T-code SM59 \n", 'ycolor')
            value = value + 0.1 #5
            self.progressbar.set(value)
            app.update_idletasks()
            self.textboxtk.insert("insert", "\n", 'ycolor')
            self.session.findById("wnd[0]/usr/cntlSM59CNTL_AREA/shellcont/shell/shellcont[1]/shell[0]").pressButton("CREATE")
            self.session.findById("wnd[0]/usr/ctxtRFCDISPLAY-RFCDEST").text = ExpName
            self.session.findById("wnd[0]/usr/ctxtRFCDISPLAY-RFCTYPE").text = "T"
            self.session.findById("wnd[0]/usr/txtRFCDOC-RFCDOC1").text = ExpName
            self.session.findById("wnd[0]/tbar[0]/btn[11]").press()
            self.session.findById("wnd[0]/usr/tabsTAB_SM59/tabpTECH/ssubSUB_SM59:SAPLCRFC:0510/radGL_TYPT_2").select()
            self.session.findById("wnd[0]/usr/tabsTAB_SM59/tabpTECH/ssubSUB_SM59:SAPLCRFC:0510/subSUB_TYPT:SAPLCRFC:0512/txtRFCDISPLAY-RFCEXEC").text = "sapxpg"
            self.session.findById("wnd[0]/tbar[0]/btn[11]").press()
            self.session.findById("wnd[0]/tbar[1]/btn[27]").press()
            result = self.session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").getCellValue(1,"ACTION")
            #print(result)
            if(result == "Error Details"):
                self.textboxtk.insert("insert", '\u2717 '+"Error in establishing sucessfull connection with host \n", 'rcolor')
                value = value + 0.5 #5
                self.progressbar.set(value)
                app.update_idletasks()
                self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
                self.session.findById("wnd[0]").sendVKey(0)
            else:
                self.textboxtk.insert("insert", '\u2713 '+"Sucessfull in establishing connection with host \n", 'gcolor')
                self.textboxtk.insert("insert", "\n", 'ycolor')
                value = value + 0.1 #6
                self.progressbar.set(value)
                app.update_idletasks()
                self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
                self.session.findById("wnd[0]").sendVKey(0)
                time.sleep(1)
                self.session.findById("wnd[0]/tbar[0]/okcd").text = "SM49"
                self.session.findById("wnd[0]").sendVKey(0)
                time.sleep(1)
                self.textboxtk.insert("insert", '\u2713 '+"Executed T-code SM49 \n", 'ycolor')
                value = value + 0.1 #7
                self.progressbar.set(value)
                app.update_idletasks()
                self.session.findById("wnd[0]/usr/cntlEXT_COM/shellcont/shell").pressToolbarButton("CREATE")
                self.session.findById("wnd[0]/usr/txtEXT_COMMAND_SCREEN-NAME").text = CmdName
                self.session.findById("wnd[0]/usr/txtEXT_COMMAND_SCREEN-OPCOMMAND").text = cmd
                self.session.findById("wnd[0]/tbar[1]/btn[13]").press()
                self.session.findById("wnd[1]/tbar[0]/btn[2]").press()
                self.session.findById("wnd[0]/tbar[1]/btn[8]").press()
                value = value + 0.1 #8
                self.progressbar.set(value)
                app.update_idletasks()
                self.session.findById("wnd[0]/usr/radRADIO_DEST").select()
                self.session.findById("wnd[0]").sendVKey(4)
                self.session.findById("wnd[1]/tbar[0]/btn[17]").press()
                self.session.findById("wnd[1]/usr/tabsG_SELONETABSTRIP/tabpTAB001/ssubSUBSCR_PRESEL:SAPLSDH4:0220/sub:SAPLSDH4:0220/txtG_SELFLD_TAB-LOW[0,24]").text = ExpName
                self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
                self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
                self.session.findById("wnd[0]/tbar[1]/btn[8]").press()
                value = value + 0.2 #10
                self.progressbar.set(value)
                app.update_idletasks()
                ExeControl = self.session.findById("wnd[0]/usr/cntlEXT_COM_RESULTS/shellcont/shell")
                ExeResult = ExeControl.Text
                self.textboxtk.insert("insert",'\u2713 '+ "OS Code Execution Achieved in host. Displaying result of executing " + cmd + "....\n\n", 'ycolor')
                self.textboxtk.insert("insert", ExeResult, 'gcolor')
                self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
                self.session.findById("wnd[0]").sendVKey(0)
        except Exception as e:
            if (self.session.findById("wnd[0]/sbar").messagetype == "E") or (self.session.findById("wnd[0]/sbar").messagetype == "W"):
                Error = self.session.findById("wnd[0]/sbar").text
                self.textboxtk.insert("insert", '\u2717 '+ "Module execution failed with error -> " + Error + " \n", 'rcolor')
            else:
                self.textboxtk.insert("insert", '\u2717 '+ "Module execution failed with exception -> " + e + " \n", 'rcolor')
            value = value + 0.6 #10
            self.progressbar.set(value)
            app.update_idletasks()
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
            self.session.findById("wnd[0]").sendVKey(0)
