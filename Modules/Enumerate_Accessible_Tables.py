import time
import json
import os

def Enumerate_Tables(self, app):
    value = 0.0
    self.progressbar.set(value)
    self.textboxtk.delete("1.0", "end")
    Module = """Module - Enumerate for Accessible Tables\n-------------------------"""
    self.textboxtk.insert("insert", Module + "\n")
    self.textboxtk.tag_config('gcolor', foreground='#00f18b')
    self.textboxtk.tag_config('rcolor', foreground='red')
    self.textboxtk.tag_config('ycolor', foreground='yellow')
    value = value + 0.1 #1
    self.progressbar.set(value)
    app.update_idletasks()

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

        # Check if user had inputed path with custom Tables in json file
        if(self.entry.get()):
            TableListFilePath = self.entry.get()
            self.textboxtk.insert("insert", '\u2713 '+"Path set for referencing Tables list is " + TableListFilePath + "\n", 'ycolor')
            # load JSON from file
            with open(TableListFilePath) as f:
                TLJsonData = json.load(f)
            self.textboxtk.insert("insert", "\n", 'ycolor')
            self.textboxtk.insert("insert", "Fetching Accessible Tables.... \n", 'ycolor')
            value = value + 0.1 #3
            self.progressbar.set(value)
            app.update_idletasks()
        else:
            cwd = os.getcwd()
            subdir = 'Config'
            path = os.path.join(cwd, subdir)
            filename = 'Tables_List_Large.json'
            file_path = os.path.join(path, filename)
            self.textboxtk.insert("insert", '\u2717 '+"No Tables list reference file provided for enumeration, only default Tables in ../Config/Tables_List_Large.json is used for enumeration \n", 'ycolor')
            with open(file_path, 'r') as f:
                TLJsonData = json.load(f)
            self.textboxtk.insert("insert", "\n", 'ycolor')
            self.textboxtk.insert("insert", "Fetching Accessible Tables.... \n", 'ycolor')
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

        self.session.findById("wnd[0]/tbar[0]/okcd").text = "SE16"
        self.session.findById("wnd[0]").sendVKey(0)
        if (self.session.findById("wnd[0]/sbar").messagetype == "E") or (self.session.findById("wnd[0]/sbar").messagetype == "W"):
            Error = self.session.findById("wnd[0]/sbar").text
            #return "E", Error;
            tag = "fail"
            self.textboxtk.insert("insert", "\u2717 SE16 -> " + Error + " \n", tag)
        else:
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
            self.session.findById("wnd[0]").sendVKey(0)
            # Loop through each key-value pair in the JSON data
            for index, (key, value) in enumerate(TLJsonData.items()):
                # Print the key-value pair
                # print(f"{index}. {key}: {value}")
                self.session.findById("wnd[0]/tbar[0]/okcd").text = "SE16"
                self.session.findById("wnd[0]").sendVKey(0)

                self.session.findById("wnd[0]/usr/ctxtDATABROWSE-TABLENAME").text = key
                self.session.findById("wnd[0]").sendVKey(0)
                time.sleep(1)
                if (self.session.findById("wnd[0]/sbar").messagetype == "E") or (self.session.findById("wnd[0]/sbar").messagetype == "W"):
                    Error = self.session.findById("wnd[0]/sbar").text
                    #return "E", Error;
                    tag = "fail"
                    self.textboxtk.insert("insert", '\u2717 '+ key + "    " + value +" -> " + Error + " \n", tag)
                else:
                    tag = "pass"
                    self.textboxtk.insert("insert", '\u2713 '+ key + "    " + value +" \n", tag)
                self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
                self.session.findById("wnd[0]").sendVKey(0)
        value = 0.5 + 0.5
        self.progressbar.set(value)
        app.update_idletasks()
