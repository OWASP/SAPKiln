import time
import json
import os
import win32gui
import win32api
import win32con

def Default_Login_Checker(self, app):
    value = 0.0
    self.progressbar.set(value)
    self.textboxtk.delete("1.0", "end")
    Module = """Module - Attempt Login with Default SAP Credentials\n-------------------------"""
    self.textboxtk.insert("insert", Module + "\n")
    self.textboxtk.tag_config('gcolor', foreground='#00f18b')
    self.textboxtk.tag_config('rcolor', foreground='red')
    self.textboxtk.tag_config('ycolor', foreground='yellow')
    value = value + 0.1 #1
    self.progressbar.set(value)
    app.update_idletasks()

    # Check if user logged in or not
    if((self.session is None) and (self.OApp is not None)):
        self.textboxtk.insert("insert", '\u2717 '+"Not active user sessions detected\n", 'ycolor')
        value = value + 0.1 #2
        self.progressbar.set(value)
        app.update_idletasks()
        # Check if user had inputed path with custom Tables in json file
        if(self.entry.get()):
            TableListFilePath = self.entry.get()
            self.textboxtk.insert("insert", '\u2713 '+"Path set for referencing default credentials is " + TableListFilePath + "\n", 'ycolor')
            # load JSON from file
            with open(TableListFilePath) as f:
                TLJsonData = json.load(f)
            self.textboxtk.insert("insert", "Initiating logins with default credentials.... \n", 'ycolor')
            value = value + 0.1 #3
            self.progressbar.set(value)
            app.update_idletasks()
        else:
            cwd = os.getcwd()
            subdir = 'Config'
            path = os.path.join(cwd, subdir)
            filename = 'Default_Credentials.json'
            file_path = os.path.join(path, filename)
            self.textboxtk.insert("insert", '\u2717 '+"No default credentials list reference file provided for enumeration, only default data in ../Config/Default_Credentials.json is used for enumeration \n", 'ycolor')
            with open(file_path, 'r') as f:
                TLJsonData = json.load(f)
            self.textboxtk.insert("insert", "Initiating logins with default credentials.... \n", 'ycolor')
            value = value + 0.1 #3
            self.progressbar.set(value)
            app.update_idletasks()
        value = value + 0.1 #4
        self.progressbar.set(value)
        app.update_idletasks()
        # Configure the tags to set the foreground color
        self.textboxtk.tag_configure("pass", foreground='#00f18b')
        self.textboxtk.tag_configure("fail", foreground='red')
        self.textboxtk.insert("insert", "\n")
        value = value + 0.1 #5
        self.progressbar.set(value)
        app.update_idletasks()

        self, SAPAppName = Reconnect(TLJsonData['Connection'], self)
        SAPwindow = win32gui.FindWindow(None, SAPAppName)
        # send the minimize message to the window
        win32api.SendMessage(SAPwindow, win32con.WM_SYSCOMMAND, win32con.SC_MINIMIZE, 0)
        #self.session.findbyId("wnd[0]").maximize
        self.textboxtk.insert("insert", '\u2713'+"Connected to target SAP system \n", 'ycolor')
        
        self.textboxtk.insert("insert", "Attempting each credentials passed in json file.... \n\n", 'ycolor')
        value = value + 0.1 #5
        self.progressbar.set(value)
        app.update_idletasks()
        # Begining of loop
        for key, value in TLJsonData.items():
            if isinstance(value, list):
                Client = key                          
                for item in value:
                    # Default credential attempt logic                    
                    Login(self, Client, item['username'], item['pass'])
                    self, SAPAppName = Reconnect(TLJsonData['Connection'], self)
                    SAPwindow = win32gui.FindWindow(None, SAPAppName)
                    # send the minimize message to the window
                    win32api.SendMessage(SAPwindow, win32con.WM_SYSCOMMAND, win32con.SC_MINIMIZE, 0)
                    #self.session.findbyId("wnd[0]").maximize   
        self.session.ActiveWindow.Close() 
    elif(self.OApp is None):
        self.textboxtk.insert("insert", "\n"+ '\u2717'+"Please connect with SAP Logon app before executing this module \n", 'rcolor')
        self.textboxtk.insert("insert", "\n")
        value = value + 1.0
        self.progressbar.set(value)
        app.update_idletasks()
    else:
        self.textboxtk.insert("insert", '\u2713 '+"Please log out or restart SAPKiln before executing this module \n", 'rcolor')
        self.textboxtk.insert("insert", "\n")
        value = value + 0.9
        self.progressbar.set(value)
        app.update_idletasks()
         
    value = 1.0 #10
    self.progressbar.set(value)
    app.update_idletasks()

def Reconnect(address, self):
    connection = self.OApp.OpenConnection(address, True)
    time.sleep(0.5)
    
    self.session = connection.Children(0)
    SAPAppName = self.session.ActiveWindow.text
    
    return self, SAPAppName
        
def Login(self, client, username, password):
    self.session.findbyId("wnd[0]/usr/txtRSYST-BNAME").text = username
    self.session.findbyId("wnd[0]/usr/pwdRSYST-BCODE").text = password
    self.session.findbyId("wnd[0]").sendVKey(0)
    if (self.session.findById("wnd[0]/sbar").messagetype == "E") or (self.session.findById("wnd[0]/sbar").messagetype == "W") or (self.session.findById("wnd[0]/sbar").messagetype == "I") or (self.session.findById("wnd[0]/sbar").messagetype == "A"):
        Error = self.session.findById("wnd[0]/sbar").text
        self.textboxtk.insert("insert", "\n"+ '\u2717'+"Login failed for "+ client + " - "+username+" - " + password + " :: Error :: " + Error + "\n", 'rcolor')
        self.textboxtk.insert("insert", "\n")
        self.session.ActiveWindow.Close()
        #self.session.ActiveWindow.Close()
    else:
        self.textboxtk.insert("insert","\n"+'\u2713'+"Sucessfully loged in as " + client + " - "+username+" - " + password + "\n", 'gcolor')
        self.textboxtk.insert("insert", "\n")
        self.session.findById("wnd[1]").sendVKey(0)
        self.session.findbyId("wnd[0]").close()
        self.session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()
        #self.session = None
           