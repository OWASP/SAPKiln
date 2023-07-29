
def help_sap_modules(self, app):
    self.textboxtk.delete("1.0", "end")
    self.textboxtk.tag_config('gcolor', foreground='#00f18b')
    self.textboxtk.tag_config('ycolor', foreground='yellow')

    if(self.optionmenu_1.get() == "Attempt Login with Default SAP Credentials"):
        HelpMsg = """Help - Attempt Login with Default SAP Credentials\n-------------------------"""
        self.textboxtk.insert("insert", HelpMsg + "\n")
        discription = """This module is designed to attempt login into the SAP system using known default credentials. The SAP Logon application has a built-in feature that automatically terminates itself after three consecutive failed login attempts. To overcome this challenge, module effectively closes and reopens sessions after each login attempt, ensuring a continuous login process. 
        
However, it's important to verify the "login/fails_to_user_lock" parameter via RZ11 to prevent potential account lockouts."""
        Tmsg = """\nSAP's known login credentials are stored in the "Default_Credentials.json" file, accessible from the Config folder. Please remember to modify the "Connection" and "Client ID" details within this file. If you wish to provide a custom JSON file to this module, kindly specify the file path in the designated "User Inputs" text box."""
        
        self.textboxtk.insert("insert", discription + "\n", 'gcolor')
        self.textboxtk.insert("insert", Tmsg + "\n", 'ycolor')
    elif(self.optionmenu_1.get() == "Enumerate for Accessible T-Codes"):
        HelpMsg = """Help - Enumerate for Accessible T-Codes\n-------------------------"""
        
        discription = """This module facilitates the identification of accessible T-Codes (Transaction codes) for the currently logged-in user. Enumerating accessible T-Codes is a crucial initial step in SAP auditing and penetration testing processes."""
        Tmsg = """\nThis module utilizes "T-Codes_List_Small.json" in the Config folder, containing sensitive transaction codes for enumeration purposes. To enumerate using a custom JSON file with a list of T-codes, please provide the file path in the designated "User Inputs" text box."""
        self.textboxtk.insert("insert", HelpMsg + "\n")
        self.textboxtk.insert("insert", discription + "\n", 'gcolor')
        self.textboxtk.insert("insert", Tmsg + "\n", 'ycolor')
    elif(self.optionmenu_1.get() == "Enumerate for Accessible Tables"):
        HelpMsg = """Help - Enumerate for Accessible Tables\n-------------------------"""
        
        discription = """This module facilitates the identification of accessible tables within the SAP system for the current logged-in user. Enumerating these accessible tables is a critical initial activity in SAP auditing and penetration testing."""
        Tmsg = """\nThe module utilizes "Tables_List_Large.json" from the Config folder, which contains a list of sensitive tables used for enumeration. To conduct enumeration with a custom JSON file containing specific tables, kindly provide the file path in the designated "User Inputs" text box."""
        self.textboxtk.insert("insert", HelpMsg + "\n")
        self.textboxtk.insert("insert", discription + "\n", 'gcolor')
        self.textboxtk.insert("insert", Tmsg + "\n", 'ycolor')
    elif(self.optionmenu_1.get() == "Enumerate for Usage of SAP_ALL Profile"):
        HelpMsg = """Help - Enumerate for Usage of SAP_ALL Profile\n-------------------------"""
        self.textboxtk.insert("insert", HelpMsg + "\n")
        discription = """This module conducts enumeration to identify the usage of the SAP_ALL profile in the target SAP System. By default, it checks if the current logged-in user is authorized with SAP_ALL profile. To perform enumeration for a custom user, kindly specify the username in the designated "User Inputs" text box."""
        Tmsg = """\nTransaction Flow: Login -> SU01 -> Filter for SAP_ALL profile w.r.t given username"""
        self.textboxtk.insert("insert", discription + "\n", 'gcolor')
        self.textboxtk.insert("insert", Tmsg + "\n", 'ycolor')
    elif(self.optionmenu_1.get() == "Enumerate Password Policies"):
        HelpMsg = """Help - Enumerate Password Policies\n-------------------------"""
        self.textboxtk.insert("insert", HelpMsg + "\n")
        discription = """This module performs an enumeration of password policies implemented in the SAP system. By default, the module retrieves and displays below listed seven parameters related to password strength in the system."""
        Tmsg = """\n1. login/password_expiration_time\n2. login/min_password_lng\n3. login/min_password_digits\n4. login/min_password_letters\n5. login/min_password_lowercase\n6. login/min_password_uppercase\n7. login/min_password_specials

This module employs the "PasswordPolicy.json" file located in the Config folder for enumeration purposes. If you wish to use a custom JSON file, please specify its file path in the designated "User Inputs" text box."""
        self.textboxtk.insert("insert", discription + "\n", 'gcolor')
        self.textboxtk.insert("insert", Tmsg + "\n", 'ycolor')
    elif(self.optionmenu_1.get() == "Enumerate Weak Password Hashes (Users)"):
        HelpMsg = """Help - Enumerate Weak Password Hashes (Users)\n-------------------------"""
        self.textboxtk.insert("insert", HelpMsg + "\n")
        discription = """This module performs enumeration to identify if any user's password is hashed with weak hashing algorithms. While hash methods are one-way and prevent password derivation from hash values, it is essential to ensure strong hashing algorithms / code versions are used to safeguard passwords. By comparing values produced by tools like Hashcat to those saved in SAP tables, plain text passwords can be recovered from hash values."""
        Tmsg = """\nTransaction Flow: Login -> SE16 -> Access table USH02 -> Filter with SAP password code versions 'A-E', 'F-G', 'H-I'"""
        discription2 = """\nDetailed description of SAP password code versions are listed below. By default, this module checks for 'BCODE' password code version. For identifying users with other password code versions, you have to provide 'PASSCODE' or 'PWDSALTEDHASH' in "User Inputs" text box."""
        Tmsg2 = """\n'BCODE'        -> Code Versions A to E (MD5 hashing algorithm)
'PASSCODE'      -> Code Versions F to G (SHA1 hashing algorithm)
'PWDSALTEDHASH' -> Code Versions H to I (Salted SHA-1 hashing algorithm)"""
        self.textboxtk.insert("insert", discription + "\n", 'gcolor')
        self.textboxtk.insert("insert", Tmsg + "\n", 'ycolor')
        self.textboxtk.insert("insert", discription2 + "\n", 'gcolor')
        self.textboxtk.insert("insert", Tmsg2 + "\n", 'ycolor')
    elif(self.optionmenu_1.get() == "Enumerate Weak Password Hashes (Hashes)"):
        HelpMsg = """Help - Enumerate Weak Password Hashes (Hashes)\n-------------------------"""
        self.textboxtk.insert("insert", HelpMsg + "\n")
        discription = """This module enumerates for password hash's of users in system."""
        Tmsg = """\nTransaction Flow: Login -> SE17 -> Access table USR02 -> Filter with SAP password code versions 'A-E', 'F-G', 'H-I'"""
        discription2 = """\nDetailed description of SAP password code versions are listed below."""
        Tmsg2 = """\nA - Code version A (obsolete)
B - Code version B (MD5-based, 8 characters, uppercase, ASCII)
C - Code Version C (Not Implemented)
D - Code version D (MD5-based, 8 characters, uppercase, UTF-8)
E - Code version E (= corrected code version D)
F - Code version F (SHA1, 40 characters, case-sensitive, UTF-8)
G - Code version G = version F + version B (two hash values)
H - Code version H (generic hash method)
I - Code version I = code versions H + F + B (three hash values)"""
        self.textboxtk.insert("insert", discription + "\n", 'gcolor')
        self.textboxtk.insert("insert", Tmsg + "\n", 'ycolor')
        self.textboxtk.insert("insert", discription2 + "\n", 'gcolor')
        self.textboxtk.insert("insert", Tmsg2 + "\n", 'ycolor')
    elif(self.optionmenu_1.get() == "OS Commands Execution - SAPXPG"):
        HelpMsg = """Help - OS Commands Execution - SAPXPG\n-------------------------"""
        discription = """SAPXPG is an important component of the SAP system as it allows for the execution of operating system commands as background process from within the SAP system, helping to integrate SAP with other systems and automate certain tasks. If no proper access control is implemented on SAPXPG program, an attacker could abuse it to create custom RFC destinations to execute OS commands. 
Currently SAPKiln only supports local code execution via this module"""
        Tmsg = """\nTransaction Flow: Login -> SM59 -> Create RFC destination with SAPXPG program -> SM49 -> Execute created command in later step with user supplied OS cmd"""
        discription2 = """\nExpected user input format"""
        Tmsg2 = """\n<OS Command>;<RFC Destination Name>;<Command Name>

By default SAPKiln executes this module with payload as \"whoami;SAPKILN GATEWAY EXP SAPXPG;SAPKILN GE\" 
Please note no duplicates are allowed in SAP as RFC Destination Name and Command Name
"""
        self.textboxtk.insert("insert", HelpMsg + "\n")
        self.textboxtk.insert("insert", discription + "\n", 'gcolor')
        self.textboxtk.insert("insert", Tmsg + "\n", 'ycolor')
        self.textboxtk.insert("insert", discription2 + "\n", 'gcolor')
        self.textboxtk.insert("insert", Tmsg2 + "\n", 'ycolor')
    elif(self.optionmenu_1.get() == "OS Commands Execution - RSBDCOS0"):
        HelpMsg = """Help - OS Commands Execution - RSBDCOS0\n-------------------------"""
        discription = """RSBDCOS0 is a powerful report that allows the execution of operating system level commands, including system commands, programs, and reports. Often utilized for automating administrative tasks in SAP systems, such as managing background jobs, this module examines if the logged-in user has access to RSBDCOS0 via transaction SA38 and attempts to execute OS commands. The default execution involves the 'whoami' command, and for custom OS command execution, you can specify them in the "User Inputs" text box."""
        Tmsg = """\nTransaction Flow: Login -> SA38 -> RSBDCOS0 -> Execute OS Commands"""
        self.textboxtk.insert("insert", HelpMsg + "\n")
        self.textboxtk.insert("insert", discription + "\n", 'gcolor')
        self.textboxtk.insert("insert", Tmsg + "\n", 'ycolor')
    elif(self.optionmenu_1.get() == "Enumerate Instances for Lateral Movement"):
        HelpMsg = """Enumerate Instances for Lateral Movement\n-------------------------"""
        discription = """This module takes advantage of SAP misconfiguration which would allow an attacker to perform Remote Logon into another SAP system via ABAP connections which have saved user credentials thus moving across or through a network, from one compromised system to another"""
        Tmsg = """\nTransaction Flow: Login -> SM59 -> Access ABAP Connections -> Enumerates RFC Destinations with saved Logon details"""
        self.textboxtk.insert("insert", HelpMsg + "\n")
        self.textboxtk.insert("insert", discription + "\n", 'gcolor')
        self.textboxtk.insert("insert", Tmsg + "\n", 'ycolor')        
    else:
        self.textboxtk.insert("insert", self.optionmenu_1.get() + "\n")
