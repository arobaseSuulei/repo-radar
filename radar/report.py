import subprocess
from pathlib import Path # Path.cwd() is for taking the path of user
import sys

if(len(sys.argv)<2):
    print("Error : file structure\n")
    print("radar <chemin>\n")
    exit(1)

chemin = sys.argv[1] #the chemin given on args
p=Path(chemin)
size = p.stat().st_size

def report(counter:int):
    
    with open(Path.cwd() / "REPORT.md",'w',encoding="utf-8") as f:
        f.write(f" ༼ つ ◕_◕ ༽つ Your file count {counter} lines\n")
        f.write("\n")
        f.write(f" The size file is {size} octects \n")

    print("*****************\n")
    print("\n")
    print("your report is ready at REPORT.md ༼ つ ◕_◕ ༽つ")
    print("\n")
    print("***************\n")


def line_counter():
    counter=0
    with open(chemin,"r") as f:
        for line in f:
            counter+=1
    return counter

res=line_counter()
report(res)






