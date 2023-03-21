import os

def install():
    """Installs python, pytube and ffmpeg (if not already installed)."""
    os.system("winget install --id=Python.Python.3.10 -e")
    os.system("pip install pytube")
    os.system("pip install ffmpeg-python")
    os.system("winget install ffmpeg --accept-source-agreements --accept-package-agreements")

def uninstall():
    """Uninstalls python, pytube and ffmpeg (if already installed)."""
    os.system("pip uninstall pytube -y")
    os.system("pip uninstall ffmpeg-python -y")
    os.system("winget uninstall ffmpeg")
    os.system("winget uninstall --id=Python.Python.3.10 -e")

# workaround for pytube
    # C:\Users\...\AppData\Local\Programs\Python\Python310\Lib\site-packages\pytube\cipher.py
    # change line 411
        #old:     transform_plan_raw = find_object_from_startpoint(raw_code, match.span()[1] - 1)
        #new:     transform_plan_raw = js
