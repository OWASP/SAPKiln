import tkinter as tk
import customtkinter
import os
import win32com.client
import win32gui
import win32api
import win32con
import subprocess
import time
from PIL import Image

# Import Modules
from Modules.Enumerate_Accessible_T_Codes import Enumerate_Tcodes
from Modules.Enumerate_SAP_ALL_Profile import Enumerate_SAP_ALL
from Modules.Help_SAP_Modules import help_sap_modules
from Modules.Check_Password_Policies import Password_Policies
from Modules.OS_Code_Execution_RSBDCOS0 import OSCode_RSBDCOS0
from Modules.OS_Code_Execution_SAPXPG import OSCode_SAPXPG
from Modules.Enumerate_Password_Hashes import View_Password_Hashes
from Modules.Enumerate_Use_of_Weak_Hash_Algorithms import Weak_Password_Hashes
from Modules.Lateral_Movement import Check_Lateral_Movement
from Modules.Enumerate_Accessible_Tables import Enumerate_Tables
from Modules.Default_Passwords import Default_Login_Checker

# ASCII art
__header__ = """
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡶⠋⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⠟⠀⣠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢀⡔⠀⢀⣾⣿⣿⣿⡏⠀⢰⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⣰⣿⠀⠀⣾⣿⣿⣿⣿⡇⠀⠸⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠠⣿⣿⠀⠀⢻⣿⣿⣿⣿⣷⡀⠀⠹⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⢿⣿⣧⠀⠈⢻⣿⣿⣿⣿⣿⣆⠀⠈⢿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠈⢻⣿⣷⣄⠀⠙⣿⣿⣿⣿⣿⣷⣄⠀⠹⣿⣿⣿⣄⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣦⡀⠈⢻⣿⣿⣿⣿⣿⣧⠀⠈⢿⣿⣿⡄⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣷⡄⠀⠙⣿⣿⣿⣿⣿⡇⠀⠘⣿⣿⠇⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣷⠀⠀⢸⣿⣿⣿⣿⡇⠀⢀⣿⠏⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠀⠀⠀⣿⣿⣿⡟⠀⠀⠜⠁⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⢰⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """
__owaspheader__ = """O W A S P"""
__subheader__ ="""
         __    __    ___   _     _   _     _
        ( (`  / /\  | |_) | |_/ | | | |   | |\ |
        _)_) /_/--\ |_|   |_| \ |_| |_|__ |_| \|

        """

# Setting appearance mode for the app
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Setting folder path to Images folder
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Images")

class App(customtkinter.CTk):
    WIDTH = 820
    HEIGHT = 620
    def __init__(self):
        super().__init__()
        self.title("SAPKiln")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        self.session = None
        self.OApp = None
        # ============ create two frames ============
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")
        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        self.frame_right.configure(fg_color='#000')
        # ============ frame_left ============
        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, minsize=10)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=10)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(16, weight=1)  # empty row with minsize as spacing

        # Setting widgets including labels, textboxes and buttons in frame_left
        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="SAPKiln v1.0",
                                              font=("Eccentric Std", -15))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=5, padx=5)
        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="About",
                                                command=self.button_event_about)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)
        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Prerequisites",
                                                command=self.button_event_Prerequisites)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)
        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Set saplogon.exe Path:")
        self.label_mode.grid(row=4, column=0, pady=0, padx=20, sticky="w")
        self.entry_path = customtkinter.CTkEntry(master=self.frame_left, placeholder_text="*Path")
        self.entry_path.grid(row=5, column=0, pady=8, padx=24, sticky="w")
        self.entry_sapapp = customtkinter.CTkEntry(master=self.frame_left, placeholder_text="SAP Logon 750")
        self.entry_sapapp.grid(row=6, column=0, pady=8, padx=24, sticky="w")
        self.button_set_path = customtkinter.CTkButton(master=self.frame_left,
                                                text="Connect SAPLogon",
                                                command=self.button_event_set_path)
        self.button_set_path.grid(row=7, column=0, pady=8, padx=20)
        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Enter Connection Details:")
        self.label_mode.grid(row=8, column=0, pady=0, padx=20, sticky="w")
        self.entry_connection = customtkinter.CTkEntry(master=self.frame_left, placeholder_text="*Connection")
        self.entry_connection.grid(row=9, column=0, pady=8, padx=24, sticky="w")
        self.entry_client = customtkinter.CTkEntry(master=self.frame_left, placeholder_text="*Client")
        self.entry_client.grid(row=10, column=0, pady=8, padx=24, sticky="w")
        self.entry_user = customtkinter.CTkEntry(master=self.frame_left, placeholder_text="*User")
        self.entry_user.grid(row=11, column=0, pady=8, padx=24, sticky="w")
        self.entry_password = customtkinter.CTkEntry(master=self.frame_left, placeholder_text="*Password", show="*")
        self.entry_password.grid(row=12, column=0, pady=8, padx=24, sticky="w")
        self.entry_LL = customtkinter.CTkEntry(master=self.frame_left, placeholder_text="*Logon Language")
        self.entry_LL.grid(row=13, column=0, pady=8, padx=24, sticky="w")
        self.button_login = customtkinter.CTkButton(master=self.frame_left,
                                                text="Login",
                                                command=self.button_event_login)
        self.button_login.grid(row=15, column=0, pady=8, padx=20)
        # ============ frame_right ============
        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        #self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)
        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=3, rowspan=4, pady=20, padx=20, sticky="nsew")
        self.frame_info.configure(fg_color='#333')
        # ============ frame_info ============
        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        # Setting textbox for outputing results
        self.textboxtk = tk.Text(master=self.frame_info)
        self.textboxtk.grid(row=0, column=0, columnspan=2, padx=15, pady=(15, 0), sticky="nsew")
        self.textboxtk.config(bg='#333', fg='#fff', font=("Courier", 10))

        # Setting progress bar to keep track of progress
        self.progressbar = customtkinter.CTkProgressBar(master=self.frame_info, determinate_speed=5)
        self.progressbar.configure(fg_color="black", progress_color="#AED6F1")
        self.progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)
        self.progressbar.set(0)

        # Setting widgets textboxes, dropdowns and buttons in frame_right
        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_right, width=290,
                                                        values=["Attempt Login with Default SAP Credentials",
                                                        "Enumerate for Accessible T-Codes", "Enumerate for Accessible Tables", "Enumerate for Usage of SAP_ALL Profile", "Enumerate Password Policies", "Enumerate Weak Password Hashes (Users)", "Enumerate Weak Password Hashes (Hashes)", "OS Commands Execution - RSBDCOS0", "OS Commands Execution - SAPXPG", "Enumerate Instances for Lateral Movement" ])
        self.optionmenu_1.grid(row=5, column=0, pady=10, padx=10, sticky="we")
        self.help_button = customtkinter.CTkButton(master=self.frame_right,
                                                text="Help",
                                                border_width=2,  # <- custom border_width
                                                fg_color="transparent",  # <- no fg_color
                                                command=self.help_button_event)
        self.help_button.grid(row=5, column=1, pady=10, padx=10, sticky="we")
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "homebutton.png")), size=(22, 22))
        self.home_button = customtkinter.CTkButton(master=self.frame_right,
                                                text="",width=5,
                                                border_width=0,  # <- custom border_width
                                                image=self.image_icon_image, command=self.button_event_home,fg_color="transparent")
        self.home_button.grid(row=5, column=2, padx=(0, 10), pady=(10, 10), sticky="nsew")
        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            placeholder_text="User Inputs")
        self.entry.grid(row=6, column=0, pady=10, padx=10, sticky="we")
        self.button_5 = customtkinter.CTkButton(master=self.frame_right, width=160,
                                                text="Execute Module",
                                                command=self.scan_module_event)
        self.button_5.grid(row=6, column=1, pady=10, padx=10, sticky="we")
        self.image_logout = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logout.png")), size=(22, 22))
        self.logout_button = customtkinter.CTkButton(master=self.frame_right,
                                                text="",width=5,
                                                border_width=0,  # <- custom border_width
                                                image=self.image_logout, fg_color="transparent", command=self.logout_button_event)
        self.logout_button.grid(row=6, column=2, padx=(0, 10), pady=(10, 10), sticky="nsew")

        # Rendering ASCII art
        self.textboxtk.delete("1.0", "end")
        self.textboxtk.tag_config('hcolor', foreground='#AED6F1')
        self.textboxtk.tag_config('rcolor', foreground='red')
        self.textboxtk.tag_config('gcolor', foreground='#00f18b')
        self.textboxtk.tag_config('ycolor', foreground='yellow')
        self.textboxtk.insert("insert", __header__ , 'rcolor')
        self.textboxtk.insert("insert", __owaspheader__ , 'ycolor')
        self.textboxtk.insert("insert", __subheader__ , 'gcolor')

    # Funtions with actions for button clicks
    def button_event_set_path(self):
        self.textboxtk.delete("1.0", "end")
        value = 0.0
        about = """SAPKiln - Connect to SAPLogon\n-------------------------"""
        self.textboxtk.insert("insert", about + "\n")
        path = self.entry_path.get()
        #path = "C:\Program Files (x86)\SAP\FrontEnd\SapGui\saplogon.exe"
        #print("Set Path pressed is " + path)
        self.textboxtk.insert("insert", "Accessing SAPLogon applicaiton at "+ path +".... \n", 'ycolor')
        self.textboxtk.insert("insert", "Opening SAPLogon applicaiton.... \n", 'ycolor')
        subprocess.Popen(path)
        time.sleep(1)
        value = value + 0.5
        self.progressbar.set(value)
        app.update_idletasks()
        # get the handle of the window
        if(self.entry_sapapp.get()):
            WindowName = self.entry_sapapp.get()
            SAPLogonWindow = win32gui.FindWindow(None, WindowName)
        else:
            SAPLogonWindow = win32gui.FindWindow(None, "SAP Logon 750")
        # send the minimize message to the window
        win32api.SendMessage(SAPLogonWindow, win32con.WM_SYSCOMMAND, win32con.SC_MINIMIZE, 0)
        SapGuiAuto = win32com.client.GetObject("SAPGUI")
        if not type(SapGuiAuto) == win32com.client.CDispatch:
            return
        self.OApp = SapGuiAuto.GetScriptingEngine
        self.textboxtk.insert("insert", "\n"+'\u2713 '+ "Opened & connected to SAPLogon applicaiton \n", 'gcolor')
        value = value + 0.5
        self.progressbar.set(value)
        app.update_idletasks()

    def button_event_login(self):
        self.textboxtk.delete("1.0", "end")
        value = 0.0
        self.progressbar.set(value)
        about = """SAPKiln - Initiating Login\n-------------------------"""
        self.textboxtk.insert("insert", about + "\n")
        if(self.OApp is None):
            self.textboxtk.insert("insert", "\n"+ '\u2717 '+"Please connect with SAP Logon app before executing this module \n", 'rcolor')
            self.textboxtk.insert("insert", "\n")
            value = value + 1.0
            self.progressbar.set(value)
            app.update_idletasks()
        else:
            ConnName = self.entry_connection.get()
            if(self.entry_connection.get()):
                #connection = self.OApp.OpenConnection("NPL [127.0.0.1]", True)
                connection = self.OApp.OpenConnection(ConnName, True)
                time.sleep(0.5)
                self.textboxtk.insert("insert", '\u2713 '+"Connected to target SAP system \n", 'ycolor')
                value = value + 0.1
                self.progressbar.set(value)
                app.update_idletasks()
                self.session = connection.Children(0)
                SAPAppName = self.session.ActiveWindow.text
                SAPwindow = win32gui.FindWindow(None, SAPAppName)
                # send the minimize message to the window
                win32api.SendMessage(SAPwindow, win32con.WM_SYSCOMMAND, win32con.SC_MINIMIZE, 0)
                #self.session.findbyId("wnd[0]").maximize
                self.textboxtk.insert("insert", "Accessing SAP System screen.... \n", 'ycolor')
                value = value + 0.1 #2
                self.progressbar.set(value)
                app.update_idletasks()
                #Login to the SAP GUI
                self.session.findbyId("wnd[0]/usr/txtRSYST-MANDT").text = self.entry_client.get()
                self.session.findbyId("wnd[0]/usr/txtRSYST-BNAME").text = self.entry_user.get()
                self.session.findbyId("wnd[0]/usr/pwdRSYST-BCODE").text = self.entry_password.get()
                self.session.findbyId("wnd[0]/usr/txtRSYST-LANGU").text = self.entry_LL.get()
                '''
                self.session.findbyId("wnd[0]/usr/txtRSYST-MANDT").text = '001'
                self.session.findbyId("wnd[0]/usr/txtRSYST-BNAME").text = 'user'
                self.session.findbyId("wnd[0]/usr/pwdRSYST-BCODE").text = 'password'
                self.session.findbyId("wnd[0]/usr/txtRSYST-LANGU").text = 'EN'
                '''
                self.session.findbyId("wnd[0]").sendVKey(0)
                self.textboxtk.insert("insert", "Attempting login.... \n", 'ycolor')
                value = value + 0.5 #7
                self.progressbar.set(value)
                app.update_idletasks()
                #Check if login was Sucessfull
                if (self.session.findById("wnd[0]/sbar").messagetype == "E") or (self.session.findById("wnd[0]/sbar").messagetype == "W"):
                    Error = self.session.findById("wnd[0]/sbar").text
                    #return "E", Error;
                    self.textboxtk.insert("insert", "\n"+ '\u2717 '+"Login failed -> " + Error + "\n", 'rcolor')
                    self.textboxtk.insert("insert", "\n")
                    value = value + 0.3 #10
                    self.progressbar.set(value)
                    app.update_idletasks()
                    self.session.ActiveWindow.Close()
                else:
                    Username = self.session.Info.User
                    self.textboxtk.insert("insert","\n"+'\u2713 '+"Sucessfull loged in as user " + Username + "\n", 'gcolor')
                    self.textboxtk.insert("insert", "\n")
                    value = value + 0.3 #10
                    self.progressbar.set(value)
                    app.update_idletasks()

            else:
                self.textboxtk.insert("insert", "\n"+ '\u2717 '+"Please provide connection name \n", 'rcolor')
                self.textboxtk.insert("insert", "\n")
                value = value + 1.0
                self.progressbar.set(value)
                app.update_idletasks()

    def button_event_about(self):
        about = """SAPKiln - About\n-------------------------"""
        self.textboxtk.delete("1.0", "end")
        self.textboxtk.insert("insert", about + "\n")
        discription = """SAPKiln is an open-source GUI tool designed to empower security researchers in conducting efficient auditing and penetration testing of SAP systems through SAP Logon/GUI (desktop application). It caters to both experienced SAP professionals and those unfamiliar with the SAP environment, as it streamlines the process of performing security checks with a user-friendly interface.

Powered by saplogon.exe and SAP scripting in its backend, SAPKiln executes automated checks in the SAP system. The current version (v1.0) boasts a comprehensive array of over 70+ checks divided into 10 modules. Beyond its built-in checks, SAPKiln provides flexibility with dynamic checks, accommodating custom user inputs. By automating security assessments, SAPKiln effectively bridges the knowledge gap for security researchers compared to SAP domain experts.
        """
        self.textboxtk.insert("insert", discription + "\n", 'gcolor')

    def button_event_Prerequisites(self):
        prerequisites = """SAPKiln - Prerequisites\n-------------------------"""
        self.textboxtk.delete("1.0", "end")
        self.textboxtk.insert("insert", prerequisites + "\n")
        discription = """Check if SAP scripting is enabled in SAP system with transaction"""
        Tmsg = """RZ11 -> sapgui/user_scripting -> TRUE"""
        discription2 = """\nOptional
Uncheck below SAP scripting options 
'Notify when a script attaches to SAP GUI'
'Notify when a script opens a connection' """
        Tmsg2 = """Options -> Accessibility & Scripting -> Scripting"""
        #discription3 = """\nEnsure SAP Logon application is not opened or active before running SAPKiln checks."""
        self.textboxtk.insert("insert", discription + "\n", 'gcolor')
        self.textboxtk.insert("insert", Tmsg + "\n", 'ycolor')
        self.textboxtk.insert("insert", discription2 + "\n", 'gcolor')
        self.textboxtk.insert("insert", Tmsg2 + "\n", 'ycolor')
        #self.textboxtk.insert("insert", discription3 + "\n", 'gcolor')

    def button_event_home(self):
        self.textboxtk.delete("1.0", "end")
        self.textboxtk.insert("insert", __header__ , 'rcolor')
        self.textboxtk.insert("insert", __owaspheader__ , 'ycolor')
        self.textboxtk.insert("insert", __subheader__ , 'gcolor')
        if(self.session is not None):
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
            self.session.findById("wnd[0]").sendVKey(0)
            SAPAppName = self.session.ActiveWindow.text
            SAPwindow = win32gui.FindWindow(None, SAPAppName)
            # send the minimize message to the window
            win32api.SendMessage(SAPwindow, win32con.WM_SYSCOMMAND, win32con.SC_MINIMIZE, 0)

    def logout_button_event(self):
        self.textboxtk.delete("1.0", "end")
        about = """SAPKiln - Initiating Logout\n-------------------------"""
        self.textboxtk.insert("insert", about + "\n")
        if(self.session is None):
            self.textboxtk.insert("insert", '\u2717 '+"No active sessions were avialable, Please log in before attempting to log out from the application\n", 'rcolor')
            self.textboxtk.insert("insert", "\n")
        else:
            #SAPAppName = self.session.ActiveWindow.text
            Username = self.session.Info.User
            self.session.findbyId("wnd[0]").close()
            self.session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()
            self.session = None
            self.textboxtk.insert("insert", '\u2713 '+"Session terminated for user " + Username + "\n", 'gcolor')

    def on_closing(self, event=0):
        self.destroy()

    def scan_event(self):
        print("checkbox toggled, current value:", self.check_box_1.get())

    def scan_module_event(self):
        # print("Module selected from Optionbox is:", self.optionmenu_1.get())
        if(self.optionmenu_1.get() == "Attempt Login with Default SAP Credentials"):
            Default_Login_Checker(self, app)
        elif(self.optionmenu_1.get() == "Enumerate for Accessible T-Codes"):
            #long process here
            Enumerate_Tcodes(self, app)
            #done = True
        elif(self.optionmenu_1.get() == "Enumerate for Usage of SAP_ALL Profile"):
            Enumerate_SAP_ALL(self, app)
        elif(self.optionmenu_1.get() =="Enumerate Password Policies"):
            Password_Policies(self, app)
        elif(self.optionmenu_1.get() =="OS Commands Execution - RSBDCOS0"):
            OSCode_RSBDCOS0(self, app)
        elif(self.optionmenu_1.get() =="OS Commands Execution - SAPXPG"):
            OSCode_SAPXPG(self, app)
        elif(self.optionmenu_1.get() == "Enumerate Weak Password Hashes (Hashes)"):
            View_Password_Hashes(self, app)
        elif(self.optionmenu_1.get() == "Enumerate Weak Password Hashes (Users)"):
            Weak_Password_Hashes(self, app)
        elif(self.optionmenu_1.get() == "Enumerate Instances for Lateral Movement"):
            Check_Lateral_Movement(self, app)
        elif(self.optionmenu_1.get() == "Enumerate for Accessible Tables"):
            Enumerate_Tables(self, app)
        else:
            pass

    def help_button_event(self):
        # print("Module selected from Optionbox is:", self.optionmenu_1.get())
        help_sap_modules(self, app)

if __name__ == "__main__":
    app = App()
    app.wm_iconbitmap('.\Images\kiln.ico')
    app.mainloop()
