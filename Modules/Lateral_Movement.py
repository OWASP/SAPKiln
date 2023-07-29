import traceback
import time
from prettytable import PrettyTable

def Enumerate_Connections(self, app, key, col):
    Connection_Name = self.session.findById("wnd[0]/usr/cntlSM59CNTL_AREA/shellcont/shell/shellcont[1]/shell[1]").GetItemText(key, col)
    self.session.findById("wnd[0]/usr/cntlSM59CNTL_AREA/shellcont/shell/shellcont[1]/shell[1]").selectItem(key, col)
    self.session.findById("wnd[0]/usr/cntlSM59CNTL_AREA/shellcont/shell/shellcont[1]/shell[1]").ensureVisibleHorizontalItem(key, col)
    self.session.findById("wnd[0]/usr/cntlSM59CNTL_AREA/shellcont/shell/shellcont[1]/shell[1]").doubleClickItem(key, col)
    self.session.findById("wnd[0]/usr/tabsTAB_SM59/tabpSIGN").select()
    PWSTATUS = self.session.findById("wnd[0]/usr/tabsTAB_SM59/tabpSIGN/ssubSUB_SM59:SAPLCRFC:0600/txtG_STPWSTATE-PWSTATUSVALUE").text
    if PWSTATUS == "saved":
        pass
        RFCUSER = self.session.findById("wnd[0]/usr/tabsTAB_SM59/tabpSIGN/ssubSUB_SM59:SAPLCRFC:0600/txtRFCDISPLAY-RFCUSER").text
        RFCCLIENT = self.session.findById("wnd[0]/usr/tabsTAB_SM59/tabpSIGN/ssubSUB_SM59:SAPLCRFC:0600/txtRFCDISPLAY-RFCCLIENT").text
        self.session.findById("wnd[0]/tbar[0]/btn[3]").press()
        return Connection_Name, RFCCLIENT, RFCUSER, PWSTATUS
    else:
        self.session.findById("wnd[0]/tbar[0]/btn[3]").press()    
        return None, None, None, None
    
def Check_Lateral_Movement(self, app):
    table = PrettyTable()
    table.field_names = ["RFC Connection", "RFC Client", "RFC User", "Password Status"]
    
    value = 0.0
    self.progressbar.set(value)
    self.textboxtk.delete("1.0", "end")
    Module = """Module - Enumerate Instances for Lateral Movement\n-------------------------"""
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
                self.textboxtk.insert("insert", '\u2713 '+"Currently this module does not accept user input, The deafult node on which connections are enumerated is 'ABAP Connections' \n", 'ycolor')
                value = value + 0.1 #3
                self.progressbar.set(value)
                app.update_idletasks()
            else:
                self.textboxtk.insert("insert", '\u2713 '+"The deafult node on which connections are enumerated is 'ABAP Connections' \n", 'ycolor')
                value = value + 0.1 #3
                self.progressbar.set(value)
                app.update_idletasks()
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "SM59"
            self.session.findById("wnd[0]").sendVKey(0)
            time.sleep(1)
            self.textboxtk.insert("insert", '\u2713 '+ "Executed T-code SM59 \n", 'ycolor')
            value = value + 0.1 #4
            self.progressbar.set(value)
            app.update_idletasks()
            self.textboxtk.insert("insert", "Identifying instances of saved user credentials for performing lateral movement.... \n", 'ycolor')
            TotalNodes = self.session.findById("wnd[0]/usr/cntlSM59CNTL_AREA/shellcont/shell/shellcont[1]/shell[1]").GetAllNodeKeys()
            for i in range(0, TotalNodes.Count):
                NodeText = self.session.findById("wnd[0]/usr/cntlSM59CNTL_AREA/shellcont/shell/shellcont[1]/shell[1]").GetNodeTextByKey(TotalNodes(i))
                if(NodeText == 'ABAP Connections'):
                    self.session.findById("wnd[0]/usr/cntlSM59CNTL_AREA/shellcont/shell/shellcont[1]/shell[1]").expandNode(TotalNodes(i))
                    test = self.session.findById("wnd[0]/usr/cntlSM59CNTL_AREA/shellcont/shell/shellcont[1]/shell[1]").GetColumnNames()
                    colname = test.ElementAt(0)
                    j = TotalNodes.Count+1
                    while j > TotalNodes.Count:
                        try:
                            j_str = str(j)
                            # To check returned node key/number has preceeding spaces and remove those spaces. e.g k_str is          11 
                            if len(j_str) < 11:
                                k_str = j_str.rjust(11, " ")
                            Connection_Name, RFCCLIENT, RFCUSER, PWSTATUS = Enumerate_Connections(self, app, k_str, colname)
                            if Connection_Name is not None:
                                table.add_row([Connection_Name, RFCCLIENT, RFCUSER, PWSTATUS])                                
                            j += 1
                        except Exception as e:
                            #print("An exception occurred, exiting loop")
                            #print(traceback.format_exc())
                            j = int(TotalNodes(i))
                else:
                    pass
            self.textboxtk.insert("insert", "\n Displaying instances of connections with saved user credentials....\n", 'ycolor')
            value = value + 0.6 #10
            self.progressbar.set(value)
            app.update_idletasks()
            self.textboxtk.insert("insert", str(table), 'gcolor')
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
            self.session.findById("wnd[0]").sendVKey(0)
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