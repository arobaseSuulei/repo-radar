import subprocess
from pathlib import Path # Path.cwd() is for taking the path of user

def report():
    big = subprocess.run(["bash","scripts.sh"],capture_output=True,text=True)
    big_res = big.stdout
    with open(Path.cwd() / "REPORT.md",'w',encoding="utf-8") as f:
        f.write("| Info | Values |\n")
        f.write("|------|--------|\n")
        f.write(f"| largest file | {big_res} |\n")

def line_counter():
    counter=0
    with open("tests/test.py","r") as f:
        for line in f:
            counter+=1
    return counter

report()
res=line_counter()
print(res)




