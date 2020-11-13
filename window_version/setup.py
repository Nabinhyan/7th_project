import sys, os
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","tkinter","matplotlib", "requests"], 
'include_files':['dataset/', 'imgs/', 'trained_model/',
(os.path.join('C:/Users/hyanm/AppData/Local/Programs/Python/Python37/', 'DLLs', 'tk86t.dll'), os.path.join('lib', 'tk86t.dll')),
(os.path.join('C:/Users/hyanm/AppData/Local/Programs/Python/Python37/', 'DLLs', 'tcl86t.dll'), os.path.join('lib', 'tcl86t.dll'))]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Import Export Prediction System",
        version = "0.1.0",
        description = "Predict the Import and Export of the Agricultural Products",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base, icon='imgs/logo.ico')])

