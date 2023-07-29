import time
import win32gui
import win32api
import win32con

# Function to display message 
def msg(self, app):
    self.textboxtk.insert("insert", "\n", 'ycolor')
    self.textboxtk.insert("insert", "To continue using SAPKiln, please use Home button\n", 'rcolor')

# Fucntion that filters for users with particular password hash code version
def ExeTCodes(self, app, x, y, value):
    self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
    self.session.findById("wnd[0]").sendVKey(0)
    value = value + 0.1 
    self.progressbar.set(value)
    app.update_idletasks()
    try:
        self.session.findById("wnd[0]/tbar[0]/okcd").text = "SE16"
        self.session.findById("wnd[0]").sendVKey(0)
        self.textboxtk.insert("insert", '\u2713 '+"Executed T-code SE16 \n", 'ycolor')
        value = value + 0.2 
        self.progressbar.set(value)
        app.update_idletasks()
        self.session.findById("wnd[0]/usr/ctxtDATABROWSE-TABLENAME").text = "USH02"
        self.session.findById("wnd[0]/tbar[0]/btn[0]").press()
        self.textboxtk.insert("insert", "Accessing Table USH02.... \n", 'ycolor')
        self.textboxtk.insert("insert", "Fetching Users with Password Hashing algorithms set to Code Versions "+ x + " and " + y +".... \n", 'ycolor')
        self.textboxtk.insert("insert", "\n", 'ycolor')
        value = value + 0.1 #4
        self.progressbar.set(value)
        app.update_idletasks()
        self.session.findById("wnd[0]/usr/ctxtI15-LOW").text = x
        self.session.findById("wnd[0]/usr/ctxtI15-HIGH").text = y
        self.session.findById("wnd[0]/tbar[1]/btn[8]").press()
        time.sleep(0.5)

        if (self.session.findById("wnd[0]/sbar").messagetype == "E") or (self.session.findById("wnd[0]/sbar").messagetype == "W") or (self.session.findById("wnd[0]/sbar").messagetype == "S"):
            Error = self.session.findById("wnd[0]/sbar").text
            self.textboxtk.insert("insert", "\n", 'ycolor')
            self.textboxtk.insert("insert", '\u2717 '+ Error  + " \n", 'rcolor')
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
            self.session.findById("wnd[0]").sendVKey(0)
            self.textboxtk.insert("insert", "\n", 'ycolor')
            __header__ = """
For viewing password hash alogorithms set for users's, provide user input as below
'BECODE'        -> Code Versions A to E (MD5 hashing algorithm)
'PASSCODE'      -> Code Versions F to G (SHA1 hashing algorithm)
'PWDSALTEDHASH' -> Code Versions H to I (Salted SHA-1 hashing algorithm)
            """
            self.textboxtk.insert("insert", __header__ + "\n", 'hcolor')
            value = value + 0.6 #10
            self.progressbar.set(value)
            app.update_idletasks()
            
        else:
            self.textboxtk.insert("insert", "\n", 'ycolor')
            self.textboxtk.insert("insert", '\u2713 '+"Please view the Users with Password Hashe Algorithm being set to Code Versions "+ x + " and " + y +" displayed in SAP GUI popped up.... \n", 'gcolor')
            SAPAppName = self.session.ActiveWindow.text
            #print(SAPAppName)
            SAPwindow = win32gui.FindWindow(None, SAPAppName)
            # Send the WM_SYSCOMMAND message with the SC_RESTORE parameter
            win32api.SendMessage(SAPwindow, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
            value = value + 0.6 #10
            self.progressbar.set(value)
            app.update_idletasks()
            self.textboxtk.insert("insert", "\n", 'ycolor')
            __header__ = """
For viewing password hash alogorithms set for users's, provide user input as below
'BECODE'        -> Code Versions A to E (MD5 hashing algorithm)
'PASSCODE'      -> Code Versions F to G (SHA1 hashing algorithm)
'PWDSALTEDHASH' -> Code Versions H to I (Salted SHA-1 hashing algorithm)
            """
            self.textboxtk.insert("insert", __header__ + "\n", 'hcolor')
            msg(self, app)
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

# Function that invoked when module is executed and filters user input from user
def Weak_Password_Hashes(self, app):
    count = 0
    value = 0.0
    self.progressbar.set(value)
    self.textboxtk.delete("1.0", "end")
    Module = """Module - Enumerate Weak Password Hashes (Users)\n-------------------------"""
    self.textboxtk.insert("insert", Module + "\n")
    self.textboxtk.tag_config('gcolor', foreground='#00f18b')
    self.textboxtk.tag_config('rcolor', foreground='red')
    self.textboxtk.tag_config('ycolor', foreground='yellow')
    self.textboxtk.tag_config('hcolor', foreground='#AED6F1')
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
        value = value + 0.1 #2
        self.progressbar.set(value)
        app.update_idletasks()
        # print("Entry is " + self.entry.get())
        if(self.entry.get()):
            UserInp = self.entry.get()
            if(UserInp == "BCODE"):
                ExeTCodes(self, app, "A","E", value) 
            elif(UserInp == "PASSCODE"):
                ExeTCodes(self, app, "F","G", value)      
            elif(UserInp == "PWDSALTEDHASH"):
                ExeTCodes(self, app, "H","I", value)         
            else:
                self.textboxtk.insert("insert", "\n", 'rcolor')
                self.textboxtk.insert("insert", '\u2713 '+"Invalid user input, please refer Help section for expected user inputs \n", 'rcolor')
                value = value + 0.8 #8
                self.progressbar.set(value)
                app.update_idletasks()        
        else:
            ExeTCodes(self, app, "A","E", value)
