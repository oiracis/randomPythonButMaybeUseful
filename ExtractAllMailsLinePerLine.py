#oiracis
import re
out = open("out.txt", "w+")
c = 0
with open("file.txt", "r+", errors="ignore") as f: #ignore all errors so it reads the file not matter what
    for line in f:
        c = c + 1
        try:
            mail = (re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", line))
            print("Nº: " + str(c) + "\t" + mail[0])
            out.write(mail[0] + "\n")
        except:
            print("oopsie")
out.close()
