import os
print("Welcome to create a python project.")
venv = input("Are you want create a python venv?(Y/N):")
directory = None
readied_ = "Your project is readied."
if venv == "Y" or venv =="y":
    directory = input("Please enter a venv path:")
    while True:
        ispython3 = input("Are you want use python3?:(Y/N)")
        if ispython3 == "y" or ispython3 == "Y":
            os.system(f"python3 -m venv {directory}")
            break
        elif ispython3 == "N" or ispython3 == "n":
            os.system(f"python -m venv {directory}")
            break
        else:
            print("Please enter Y or N!")
            continue
have_package = input("Are you want install some python package?(Y/N)")
if have_package == "y" or have_package == "Y":
    package = input("Please enter some package:")
    if directory:
        if os.name == "posix":
            os.system(f"source ./{directory}/bin/activate && pip install {package}")
            readied_ = "Your project is readied.\nIf you want open the venv,please run:\nsource ./(Your venv path)/bin/activate "
        elif os.name == "nt":
            os.system(f"./{directory}/bin/activate.bat")
            os.system(f"pip install {package}")
            readied_ = "Your project is readied.\nIf you want open the venv,please run:\n./(Your venv path)/bin/activate.bat "
        else:
            print("Cant install!\nNot supported your system!\nexiting...")
    else:
        os.system(f"pip install {package}")
print(readied_)
