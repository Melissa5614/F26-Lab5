# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Melissa Aydin
# Date: 21 Oct
# Purpose: Process File data.
# Usage: ./lab5d.py

# TO DO 1: Copy the files pythonStatements.txt and machineCode.txt in folder.
pyth = open("pythonStatements.txt", "r")
macod = open("machineCode.txt", "r")
output = open("output.txt", "w")
pyth_line = pyth.readline()
macod_line = macod.readline()
while pyth_line and macod_line:
    clean_py = pyth_line.split('#')[0].strip()
    clean_mc = macod_line.strip()
    output.write(f"{clean_py}\t{clean_mc}\n")
    print(f"  {clean_py}    {clean_mc}")
    pyth_line = pyth.readline()
    macod_line = macod.readline()
pyth.close()
macod.close()
output.close()
