import time
from prettytable import PrettyTable
import json

def Password_Policies(self, app):
    # Default password policy parameters
    password_values = ["login/password_expiration_time", "login/min_password_lng", "login/min_password_digits", "login/min_password_letters", "login/min_password_lowercase", "login/min_password_uppercase", "login/min_password_specials"]
    table = PrettyTable()
    table.field_names = ["Parameter", "User-Defined Value", "System-Default Value", "Comment"]
    PasswordPolicyFilePath = None
    value = 0.0
    self.progressbar.set(value)
    self.textboxtk.delete("1.0", "end")
    Module = """Module - Enumerate Password Policies\n-------------------------"""
    self.textboxtk.insert("insert", Module + "\n")
    self.textboxtk.tag_config('gcolor', foreground='#00f18b')
    self.textboxtk.tag_config('rcolor', foreground='red')
    self.textboxtk.tag_config('ycolor', foreground='yellow')
    value = value + 0.1 #1
    self.progressbar.set(value)
    app.update_idletasks()
    try:
        # Check if user logged in or not
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

            # Check if user had inputed path with custom parameters in json file
            if(self.entry.get()):
                PasswordPolicyFilePath = self.entry.get()
                self.textboxtk.insert("insert", '\u2713 '+"Path set for referencing ideal Password Policy is " + PasswordPolicyFilePath + "\n", 'ycolor')
                # load JSON from file
                with open(PasswordPolicyFilePath) as f:
                    PPJsonData = json.load(f)
                value = value + 0.1 #3
                self.progressbar.set(value)
                app.update_idletasks()
            else:
                self.textboxtk.insert("insert", '\u2717 '+"No ideal Password Policy reference file provided for cross checking, only password policy enumeration is done \n", 'ycolor')
                value = value + 0.1 #3
                self.progressbar.set(value)
                app.update_idletasks()
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "SA38"
            self.session.findById("wnd[0]").sendVKey(0)
            time.sleep(1)
            self.textboxtk.insert("insert", '\u2713 '+"Executed T-code SA38 \n", 'ycolor')
            value = value + 0.1 #4
            self.progressbar.set(value)
            app.update_idletasks()
            self.textboxtk.insert("insert", "\n", 'ycolor')
            self.textboxtk.insert("insert", "Fetching password parameters via RSPARAM.... \n", 'ycolor')
            self.session.findById("wnd[0]/usr/ctxtRS38M-PROGRAMM").text = "RSPARAM"
            self.session.findById("wnd[0]/tbar[1]/btn[8]").press()
            self.session.findById("wnd[0]/tbar[1]/btn[8]").press()
            value = value + 0.1 #5
            self.progressbar.set(value)
            app.update_idletasks()

            for element in password_values:
                self.session.findById("wnd[0]/tbar[1]/btn[29]").press()
                self.session.findById("wnd[1]/usr/subSUB_DYN0500:SAPLSKBH:0600/btnAPP_WL_SING").press()
                self.session.findById("wnd[1]/usr/subSUB_DYN0500:SAPLSKBH:0600/btn600_BUTTON").press()
                self.session.findById("wnd[2]").sendVKey(4)
                self.session.findById("wnd[3]/tbar[0]/btn[17]").press()
                self.session.findById("wnd[3]/usr/tabsG_SELONETABSTRIP/tabpTAB001/ssubSUBSCR_PRESEL:SAPLSDH4:0220/sub:SAPLSDH4:0220/txtG_SELFLD_TAB-LOW[0,24]").text = element
                self.session.findById("wnd[3]/tbar[0]/btn[0]").press()
                self.session.findById("wnd[3]/tbar[0]/btn[0]").press()
                self.session.findById("wnd[2]/tbar[0]/btn[0]").press()
                UserValue = self.session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").getCellValue(0,"PAR_USER_WERT")
                SystemValue = self.session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").getCellValue(0,"PAR_DEFAULT_WERT1")
                CommentValue = self.session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").getCellValue(0,"DESCR")
                table.add_row([element, UserValue, SystemValue, CommentValue])
                time.sleep(1)

            # Configure the tags to set the foreground color
            self.textboxtk.tag_configure("pass", foreground='#00f18b')
            self.textboxtk.tag_configure("fail", foreground='red')
            #self.textboxtk.insert("insert", "\n")

            value = value + 0.2 #7
            self.progressbar.set(value)
            app.update_idletasks()

            if PasswordPolicyFilePath is not None:
                self.textboxtk.insert("insert", "Displaying fetched password parameters after comparing with provided Password Policy reference file.... \n", 'ycolor')
                self.textboxtk.insert("insert"," \n")
                for row in table:
                    row.border = False
                    row.header = False
                    UDValue = row.get_string(fields=["User-Defined Value"]).strip()
                    SDValue = row.get_string(fields=["System-Default Value"]).strip()
                    ParamValue = row.get_string(fields=["Parameter"]).strip()
                    if(UDValue):
                        intValue = int(UDValue)
                        #print("Value for Parameter : "+ParamValue+" is set as " + UDValue)
                    else:
                        intValue = int(SDValue)
                        #print("Value for Parameter : "+ParamValue+" is set as " + SDValue)
                    if(int(PPJsonData[ParamValue]) > intValue):
                        tag = "fail"
                        self.textboxtk.insert("insert", '\u2717 '+ParamValue+ " "+str(intValue)+" \n", tag)
                    else:
                        tag = "pass"
                        self.textboxtk.insert("insert", '\u2713 '+ParamValue+ " "+str(intValue)+" \n", tag)
            else:
                self.textboxtk.insert("insert", "Displaying fetched password parameters.... \n", 'ycolor')
                self.textboxtk.insert("insert"," \n")
                self.textboxtk.insert("insert", str(table), 'gcolor')

            value = value + 0.3 #10
            self.progressbar.set(value)
            app.update_idletasks()
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
            self.session.findById("wnd[0]").sendVKey(0)
    
    except Exception as e:
        self.textboxtk.insert("insert"," \n")
        if (self.session.findById("wnd[0]/sbar").messagetype == "E") or (self.session.findById("wnd[0]/sbar").messagetype == "W"):
            Error = self.session.findById("wnd[0]/sbar").text
            self.textboxtk.insert("insert", '\u2717 '+ "Module execution failed with error -> " + Error + " \n", 'rcolor')
        else:
            self.textboxtk.insert("insert", '\u2717 '+ "Module execution failed with exception -> " + str(e) + " \n", 'rcolor')
        value = value + 0.9 #10
        self.progressbar.set(value)
        app.update_idletasks()
        self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
        self.session.findById("wnd[0]").sendVKey(0)
    