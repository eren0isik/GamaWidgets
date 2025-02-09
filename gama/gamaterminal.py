import os
print("Gama Widgets Script Control Terminal(V0.1(B))")
while True:
    gamaterm = input("><Gama>>")

    if "help" in gamaterm:
        print("""
              
┌────────┐  ┌──────────────────────────┐
│izolecmd├──┤Open python command prompt│
└────├───┘  └──────────────────────────┘
┌────├──┐  ┌─────────────────────────────┐
│izoleps├──┤Open python PowerShell prompt│
└───────┘  └─────────────────────────────┘
              
""")
    if "izolecmd" in gamaterm:
        os.startfile(r"python\WinPython Command Prompt.exe")
    if "izoleps" in gamaterm:
        os.startfile(r"python\WinPython Powershell Prompt.exe")
    if "exit" in gamaterm:
        exit()