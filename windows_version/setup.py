import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","tkinter","matplotlib"], 
'include_files':['dataset/', 'imgs/', 'trained_model/']}

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

