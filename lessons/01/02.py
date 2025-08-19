# import this

import sys
import os
import platform
import site


print("Python Version Info:")
print(f"  Version: {platform.python_version()}")
print(f"  Implementation: {platform.python_implementation()}")
print(f"  Executable: {sys.executable}\n")

print("Paths:")
print(f"  sys.path:\n    " + "\n    ".join(sys.path))
print(f"\n  Current Working Directory: {os.getcwd()}")
print(f"  Site Packages Directories:\n    " + "\n    ".join(site.getsitepackages()))
print(f"  User Site Directory: {site.getusersitepackages()}\n")

