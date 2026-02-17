import os
import subprocess
import platform
import shutil

def open_app(app_name):
    system = platform.system()

    try:
        if system == "Windows":
            subprocess.Popen(app_name)
        elif system == "Darwin":  # macOS
            subprocess.Popen(["open", "-a", app_name])

        else:
            subprocess.Popen([app_name])
        
        return f"Opened {app_name} successfully."
    
    except Exception as e:
        return f"Error opening {app_name}: {str(e)}"
    
def open_path(path):
    system = platform.system()

    try:
        if system == "Windows":
            os.startfile(path)
        elif system == "Darwin":  # macOS
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])

    except Exception as e:
        return f"Error opening {path}: {str(e)}"

def delete_file(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
        else:
            return "File not found."

        return f"Deleted {path}"

    except Exception as e:
        return f"Delete failed: {e}"
    
def shutdown():
    system = platform.system()

    if system == "Windows":
        os.system("shutdown /s /t 1")
    elif system == "Darwin":  # macOS
        os.system("sudo shutdown -h now")
    else:
        os.system("sudo shutdown -h now")
    
    return "Shutting down..."