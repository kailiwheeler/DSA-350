import re
from urllib.request import Request, urlopen
import matplotlib.pyplot as plt

req = Request('https://en.wikipedia.org/wiki/Ada_Lovelace',headers={'User-Agent':'Mozilla/5.0'})
hand = urlopen(req)
years = []

#https://stackoverflow.com/questions/2973436/regex-lookahead-lookbehind-and-atomic-groups
#https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Cheatsheet
#sources for neagitive lookahead and lookbehind assertions

for line in hand:
    line = line.decode().strip()
    if(re.search('Bodleian Display',line)):
        print(line)
        break
    found1 = re.findall('(?<![0-9A-Za"&-])(1[89][0-9]{2})(?![0-9A-Za-z"&-])',line)
    found2 = re.findall('(?<![0-9A-Za-z"&-])(20[0-2][0-9])(?![0-9A-Za-z"&-])', line)
    #not leading or trailing digit, character a to z or A to Z, " & and -
    if(len(found1) != 0):
        for i in found1:
            num = int(i)
            years.append(num)
    if(len(found2) != 0):
        for i in found2:
            num = int(i)
            years.append(num)
years.sort()
print(years)
data = years
plt.hist(data, bins=20,color='skyblue', edgecolor='black')
plt.xlabel('Years')
plt.ylabel('Count')
plt.title('Count of Years Mentioned in Ada Lovelace\'s Wiki Page')
plt.savefig('Wiki.png', dpi=200)
plt.show()
