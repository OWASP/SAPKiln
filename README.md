# OWASP SAPKiln ![SAPKiln](./Images/kiln.ico) 
![SAPiln Version](https://img.shields.io/badge/1.0-0000?label=Version)

The world :earth_americas: of SAP is very vast and unique. SAP has multiple products to tackle various problems as well as multiple technology platforms such as NetWeaver etc. SAPKiln is an open-source GUI tool :computer: designed to empower security researchers in conducting efficient auditing and penetration testing of SAP systems through SAP Logon/GUI (desktop application). It caters to both experienced SAP professionals and those unfamiliar with the SAP environment, as it streamlines the process of performing security checks with a user-friendly interface:sparkles:.

Powered :battery: by saplogon.exe and SAP scripting in its backend, SAPKiln executes automated checks in the SAP system. The current version (v1.0) boasts a comprehensive array of over 70+ checks :exclamation: divided into 10 modules. Beyond its built-in checks, SAPKiln provides flexibility with dynamic checks, accommodating custom user inputs. By automating security assessments, SAPKiln effectively bridges the knowledge gap for security researchers :cop: compared to SAP domain experts:eyeglasses:.

### Modules Included :cyclone:
* Attempt Login with Default SAP Credentials
* Enumerate for Accessible T-Codes
* Enumerate for Accessible Tables
* Enumerate for Usage of SAP_ALL Profile
* Enumerate Password Policies
* Enumerate Weak Password Hashes (Users)
* Enumerate Weak Password Hashes (Hashes)
* OS Commands Execution - RSBDCOS0
* OS Commands Execution - SAPXPG
* Enumerate Instances for Lateral Movement
### Installation :hammer_and_wrench:
```
git clone https://github.com/alexdevassy/SAPkiln.git
cd SAPKiln
pip install -r requirements.txt
```
*SAPKiln v1.0 is only supported in windows due to its dependency with `pywin32` library. Its tested in `windows 10` with `python 3.10.11`.

### Prerequisites :construction:
Before executing SAPKiln make sure below prerequisite is met.
* SAP scripting is enabled in backend SAP system
  - To enable SAP scripting, execute T-Code "RZ11", search for "sapgui/user_scripting", change its value from "False" to "True".

Optional prerequisites

* SAP scripting options are unchecked in SAP GUI
  - Navigate to "Options" within SAP GUI, inside options navigate to "Accessibility & Scripting" -> "Scripting". And uncheck below options 
    - "Notify when a script attaches to SAP GUI"
    - "Notify when a script opens a connection"

### Usage :space_invader:
```
python .\SAPKiln.py
```
https://github.com/OWASP/OWASP-SAPKiln/assets/31893005/7a28e87c-3b40-4ea0-88cd-510088d5f392


