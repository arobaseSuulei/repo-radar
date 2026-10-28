import subprocess

def report():
    big = subprocess.run(["bash","scripts.sh"],capture_output=True,text=True)
    big_res = big.stdout
    with open("output/REPORT.md",'w',encoding="utf-8") as f:
        f.write("| Info | Values |\n")
        f.write("|------|--------|\n")
        f.write(f"| largest file | {big_res} |\n")

report()




