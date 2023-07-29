import time

def OSCode_RSBDCOS0(self, app):

    cmd = "whoami"
    value = 0.0
    self.progressbar.set(value)
    self.textboxtk.delete("1.0", "end")
    Module = """Module - OS Commands Execution - RSBDCOS0\n-------------------------"""
    self.textboxtk.insert("insert", Module + "\n")
    self.textboxtk.tag_config('gcolor', foreground='#00f18b')
    self.textboxtk.tag_config('rcolor', foreground='red')
    self.textboxtk.tag_config('ycolor', foreground='yellow')
    value = value + 0.1 #1
    self.progressbar.set(value)
    app.update_idletasks()
    try:
        if(self.session is None):
            self.textboxtk.insert("insert", "Please log in before executing this module \n", 'rcolor')
            self.textboxtk.insert("insert", "\n")
            value = value + 0.9
            self.progressbar.set(value)
            app.update_idletasks()
        else:
            self.textboxtk.insert("insert", "Sucessfully detected loged in session\n", 'ycolor')
            if(self.entry.get()):
                cmd = self.entry.get()
                self.textboxtk.insert("insert", "Executing module with command " + cmd  + "\n", 'ycolor')
                value = value + 0.2 #3
                self.progressbar.set(value)
                app.update_idletasks()
            else:
                UserName = self.session.Info.User
                self.textboxtk.insert("insert", "Executing module with deafult command " + cmd  + "....\n", 'ycolor')
                value = value + 0.2 #3
                self.progressbar.set(value)
                app.update_idletasks()
            value = value + 0.2 #5
            self.progressbar.set(value)
            app.update_idletasks()
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "SA38"
            self.session.findById("wnd[0]").sendVKey(0)
            time.sleep(1)
            self.textboxtk.insert("insert", '\u2713 '+"Executed T-code SA38 \n", 'ycolor')
            value = value + 0.2 #6
            self.progressbar.set(value)
            app.update_idletasks()

            self.session.findById("wnd[0]/usr/ctxtRS38M-PROGRAMM").text = "RSBDCOS0"
            self.session.findById("wnd[0]/tbar[1]/btn[8]").press()
            self.session.findById("wnd[0]/usr/txt[0,8]").text = cmd

            self.session.findById("wnd[0]").sendVKey(0)
            self.textboxtk.insert("insert", "\n", 'ycolor')
            self.textboxtk.insert("insert", "Commencing code execution....\n", 'ycolor')
            ReturnValue = self.session.findById("wnd[0]/usr/lbl[0,9]").Text
            if ReturnValue == "[1]ReturnCode = 127":
                self.textboxtk.insert("insert", '\u2717 '+"Result of executing command " + cmd + " is Empty/Error"  + "\n", 'rcolor')
            else:
                self.textboxtk.insert("insert", '\u2713 '+"Result of executing command " + cmd + " is -> " + ReturnValue + "\n", 'gcolor')

            self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
            self.session.findById("wnd[0]").sendVKey(0)
            #print (ReturnValue)
            value = value + 0.4 #10
            self.progressbar.set(value)
            app.update_idletasks()
    except Exception as e:
        self.textboxtk.insert("insert"," \n")
        if (self.session.findById("wnd[0]/sbar").messagetype == "E") or (self.session.findById("wnd[0]/sbar").messagetype == "W"):
            Error = self.session.findById("wnd[0]/sbar").text
            self.textboxtk.insert("insert", '\u2717 '+ "Module execution failed with error -> " + Error + " \n", 'rcolor')
        else:
            self.textboxtk.insert("insert", '\u2717 '+ "Module execution failed with exception -> " + e + " \n", 'rcolor')
        value = value + 0.9 #10
        self.progressbar.set(value)
        app.update_idletasks()
        self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
        self.session.findById("wnd[0]").sendVKey(0)