#! python3
# fileCopyandPaste.py - find the second column of a file, and outputs it to another file

f = open("dnsList.txt", "r")
g = open("dnsListfixed.txt", "w")

for line in f:
    if line.strip():
        g.write("\t".join(line.split()[1:2]) + "\n")

f.close()
g.close()
