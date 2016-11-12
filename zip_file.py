import zipfile
import re

o, n, f = [], "90052", "%s.txt"
nnr = "Next nothing is (\d+)"

# Download the ZIP file from http://www.pythonchallenge.com/pc/def/channel.zip

file = zipfile.ZipFile("channel.zip")

while True:
    try:
        n = re.search(nnr, file.read(f % n)).group(1)
    except:
        print file.read(f % n)
        break

    o.append(file.getinfo(f % n).comment)

print "".join(o)
