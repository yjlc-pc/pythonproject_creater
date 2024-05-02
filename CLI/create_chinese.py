import os
print("欢迎创建python项目")
venv = input("要创建一个python虚拟环境吗?(Y/N):")
directory = None
readied_ = "你的项目准备好了!"
if venv == "Y" or venv =="y":
    directory = input("请输入一个路径,以创建虚拟环境:")
    while True:
        ispython3 = input("你要创建一个python3虚拟环境吗?:(Y/N)")
        if ispython3 == "y" or ispython3 == "Y":
            os.system(f"python3 -m venv {directory}")
            break
        elif ispython3 == "N" or ispython3 == "n":
            os.system(f"python -m venv {directory}")
            break
        else:
            print("请输入Y或N!")
            continue
have_package = input("你要安装python第三方包吗??(Y/N)")
if have_package == "y" or have_package == "Y":
    package = input("Please enter some package:")
    if directory:
        if os.name == "posix":
            os.system(f"source ./{directory}/bin/activate && pip install {package}")
            readied_ = "你的项目准备好了!如果你要进入虚拟环境,请运行:\nsource ./(Your venv path)/bin/activate "
        elif os.name == "nt":
            os.system(f"./{directory}/bin/activate.bat")
            os.system(f"pip install {package}")
            readied_ = "你的项目准备好了!如果你要进入虚拟环境,请运行:\n./(Your venv path)/bin/activate.bat "
        else:
            print("目前不支持你的系统.正在退出...")
            exit()
    else:
        os.system(f"pip install {package}")
print(readied_)
