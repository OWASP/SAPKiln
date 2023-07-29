import time
import win32gui
import win32api
import win32con

def View_Password_Hashes(self, app):

    value = 0.0
    self.progressbar.set(value)
    self.textboxtk.delete("1.0", "end")
    Module = """Module - Enumerate Weak Password Hashes (Hashes)\n-------------------------"""
    self.textboxtk.insert("insert", Module + "\n")
    self.textboxtk.tag_config('gcolor', foreground='#00f18b')
    self.textboxtk.tag_config('rcolor', foreground='red')
    self.textboxtk.tag_config('ycolor', foreground='yellow')
    value = value + 0.1 #1
    self.progressbar.set(value)
    app.update_idletasks()
    try:
        if(self.session is None):
            self.textboxtk.insert("insert", '\u2717 '+"Please log in before executing this module \n", 'rcolor')
            self.textboxtk.insert("insert", "\n")
            value = value + 0.9
            self.progressbar.set(value)
            app.update_idletasks()
        else:
            self.textboxtk.insert("insert", '\u2713 '+"Sucessfully detected loged in session\n", 'ycolor')
            value = value + 0.1 #2
            self.progressbar.set(value)
            app.update_idletasks()
            if(self.entry.get()):
                self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
                self.session.findById("wnd[0]").sendVKey(0)
                self.textboxtk.insert("insert", "\n", 'rcolor')
                self.textboxtk.insert("insert", '\u2713 '+"Invalid user input, this module dont require any user input for execution \n", 'rcolor')
                value = value + 0.8 #8
                self.progressbar.set(value)
                app.update_idletasks()
            else:
                self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
                self.session.findById("wnd[0]").sendVKey(0)

                value = value + 0.1 #3
                self.progressbar.set(value)
                app.update_idletasks()
                self.session.findById("wnd[0]/tbar[0]/okcd").text = "SE17"
                self.session.findById("wnd[0]").sendVKey(0)
                self.textboxtk.insert("insert", '\u2713 '+"Executed T-code SE17 \n", 'ycolor')
                value = value + 0.1 #4
                self.progressbar.set(value)
                app.update_idletasks()
                self.session.findById("wnd[0]/usr/ctxtDD02V-TABNAME").text = "USR02"
                self.session.findById("wnd[0]/tbar[0]/btn[0]").press()
                self.textboxtk.insert("insert", "Accessing Table USR02.... \n", 'ycolor')
                self.textboxtk.insert("insert", "Fetching Password Hashes.... \n", 'ycolor')
                self.textboxtk.insert("insert", "\n", 'ycolor')
                value = value + 0.1 #5
                self.progressbar.set(value)
                app.update_idletasks()
                self.session.findById("wnd[0]/usr/tblSAPMSTAZTABCTRL200").verticalScrollbar.position = 0
                self.session.findById("wnd[0]/usr/tblSAPMSTAZTABCTRL200/ctxtRSTAZ-SHOWFLAG[2,0]").text = "X"
                self.session.findById("wnd[0]/usr/tblSAPMSTAZTABCTRL200/ctxtRSTAZ-SHOWFLAG[2,1]").text = "X"
                self.session.findById("wnd[0]/usr/tblSAPMSTAZTABCTRL200/ctxtRSTAZ-SHOWFLAG[2,2]").text = "X"
                self.session.findById("wnd[0]/usr/tblSAPMSTAZTABCTRL200").verticalScrollbar.position = 30
                self.session.findById("wnd[0]/usr/tblSAPMSTAZTABCTRL200/ctxtRSTAZ-SHOWFLAG[2,0]").text = "X"
                self.session.findById("wnd[0]/usr/tblSAPMSTAZTABCTRL200/ctxtRSTAZ-SHOWFLAG[2,3]").text = "X"
                self.session.findById("wnd[0]/usr/tblSAPMSTAZTABCTRL200/ctxtRSTAZ-SHOWFLAG[2,12]").text = "X"
                self.session.findById("wnd[0]/tbar[1]/btn[8]").press()
                value = value + 0.3 #8
                self.progressbar.set(value)
                app.update_idletasks()
                SAPAppName = self.session.ActiveWindow.text
                #print(SAPAppName)
                SAPwindow = win32gui.FindWindow(None, SAPAppName)
                # Send the WM_SYSCOMMAND message with the SC_RESTORE parameter
                win32api.SendMessage(SAPwindow, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
                self.textboxtk.insert("insert", '\u2713 '+"Please view the Password Hashes displayed in SAP GUI popped up....\n", 'gcolor')
                value = value + 0.2 #10
                self.progressbar.set(value)
                app.update_idletasks()
                self.textboxtk.insert("insert", "\n", 'ycolor')
                self.textboxtk.insert("insert", "To continue using SAPKiln, please use Home button\n", 'rcolor')
    except Exception as e:
        self.textboxtk.insert("insert", " \n")
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