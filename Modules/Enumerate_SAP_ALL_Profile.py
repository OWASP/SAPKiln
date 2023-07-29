import time

def Enumerate_SAP_ALL(self, app):
    value = 0.0
    self.progressbar.set(value)
    self.textboxtk.delete("1.0", "end")
    Module = """Module - Enumerate for Usage of SAP_ALL Profile\n-------------------------"""
    self.textboxtk.insert("insert", Module + "\n")
    self.textboxtk.tag_config('gcolor', foreground='#00f18b')
    self.textboxtk.tag_config('rcolor', foreground='red')
    self.textboxtk.tag_config('ycolor', foreground='yellow')
    value = value + 0.1 #1
    self.progressbar.set(value)
    app.update_idletasks()
    if(self.session is None):
        self.textboxtk.insert("insert", "Please log in before executing this module \n", 'rcolor')
        self.textboxtk.insert("insert", "\n")
        value = value + 0.9
        self.progressbar.set(value)
        app.update_idletasks()

        #string = "Please log in before executing this module"
        #return string
    else:
        self.textboxtk.insert("insert", "Sucessfully detected loged in session\n", 'ycolor')
        if(self.entry.get()):
            UserName = self.entry.get()
            self.textboxtk.insert("insert",'\u2713 '+ "Executing module with user " + UserName  + "\n", 'ycolor')
            value = value + 0.1 #2
            self.progressbar.set(value)
            app.update_idletasks()
        else:
            UserName = self.session.Info.User
            self.textboxtk.insert("insert", '\u2713 '+ "Executing module with currently loged in user " + UserName  + "\n", 'ycolor')
            value = value + 0.1 #3
            self.progressbar.set(value)
            app.update_idletasks()

        value = value + 0.1 #4
        self.progressbar.set(value)
        app.update_idletasks()

        try:
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "SU01"
            self.session.findById("wnd[0]").sendVKey(0)
            time.sleep(1)
            self.textboxtk.insert("insert", '\u2713 '+"Executed T-code SU01 \n", 'ycolor')
            value = value + 0.1 #5
            self.progressbar.set(value)
            app.update_idletasks()

            self.session.findById("wnd[0]/usr/ctxtSUID_ST_BNAME-BNAME").text = UserName
            self.session.findById("wnd[0]/tbar[1]/btn[7]").press()

            #Check if user exists
            if (self.session.findById("wnd[0]/sbar").messagetype == "E") or (self.session.findById("wnd[0]/sbar").messagetype == "W"):
                Error = self.session.findById("wnd[0]/sbar").text
                #return "E", Error;
                value = value + 0.6 #10
                self.progressbar.set(value)
                app.update_idletasks()
                self.textboxtk.insert("insert", '\u2717 '+"User lookup failed -> " + Error + "\n", 'rcolor')
                self.textboxtk.insert("insert", "\n")
                self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
                self.session.findById("wnd[0]").sendVKey(0)

            else:
                #return "S", session;
                self.textboxtk.insert("insert", '\u2713 '+"User located \n", 'ycolor')

                self.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpPROF").select()
                self.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpPROF/ssubMAINAREA:SAPLSUID_MAINTENANCE:1103/cntlG_PROFILES_CONTAINER/shellcont/shell").pressToolbarButton("&MB_FILTER")
                self.textboxtk.insert("insert", "\n", 'ycolor')
                self.textboxtk.insert("insert", "Searching for SAP_ALL profile on user " + UserName  + "....\n", 'ycolor')
                value = value + 0.1 #6
                self.progressbar.set(value)
                app.update_idletasks()

                self.session.findById("wnd[1]/usr/subSUB_DYN0500:SAPLSKBH:0600/btnAPP_WL_SING").press()
                self.session.findById("wnd[1]/usr/subSUB_DYN0500:SAPLSKBH:0600/btn600_BUTTON").press()

                self.session.findById("wnd[2]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").text = "SAP_ALL"
                self.session.findById("wnd[2]/tbar[0]/btn[0]").press()

                #self.textboxtk.insert("insert", "Detecting SAP_ALL profile on user " + UserName  + "\n", 'ycolor')
                value = value + 0.1 #7
                self.progressbar.set(value)
                app.update_idletasks()

                try:
                    value = self.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpPROF/ssubMAINAREA:SAPLSUID_MAINTENANCE:1103/cntlG_PROFILES_CONTAINER/shellcont/shell").getCellValue(0,"PROFILE")
                except:
                    self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
                    self.session.findById("wnd[0]").sendVKey(0)
                    self.textboxtk.insert("insert", "\n", 'ycolor')
                    self.textboxtk.insert("insert", '\u2717 '+"SAP_ALL profile is not provinsioned for user " + UserName  + "\n", 'rcolor')
                    self.textboxtk.insert("insert", "\n")
                    #value = value + 0.3
                    value = float(0.7) + float(0.3)
                    self.progressbar.set(value)
                    app.update_idletasks()

                else:
                    self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
                    self.session.findById("wnd[0]").sendVKey(0)
                    self.textboxtk.insert("insert", "\n", 'ycolor')
                    self.textboxtk.insert("insert",'\u2713 '+ "SAP_ALL profile is provinsioned for user " + UserName  + "\n", 'gcolor')
                    self.textboxtk.insert("insert", "\n")
                    #value = value + 0.3
                    value = float(0.7) + float(0.3)
                    self.progressbar.set(value)
                    app.update_idletasks()
                    #self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
                    #self.session.findById("wnd[0]").sendVKey(0)
        except Exception as e:
            self.textboxtk.insert("insert"," \n")
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
