''' template for counting how many times Esther appears in each chapter'''
import re
import urllib.request
import matplotlib.pyplot as plt
#visit the webpage:
hand =  urllib.request.urlopen('https://www.gutenberg.org/cache/epub/1023/pg1023.txt') #your code here

#initialize the chapter counter
chapter = 0
chapter_list = [0] #initialize the chapter list
counts_esther = [0] #initialize the counts of how many times Esther is mentioned
counts_guppy = [0]

#Goal: to populate chapter_list [0,1,2,...] and counts_esther [11, 0, 0, 18, 2,...]
for line in hand:
    line = line.decode().strip()
    #identify when we hit a new chapter so we can start over with the counting
    new_chapter = re.search('CHAPTER', line) #regex is overkill for this
    if new_chapter: 
        chapter += 1 #figure out which chapter we are on
        chapter_list.append(chapter) #create a new item in the list to track the chapters
        counts_esther.append(0)#start the counter for counts of Esther
        counts_guppy.append(0)
    num_counts_e = len(re.findall('Esther', line))#your code here - use regex and figure out how many times 'Esther' is found in the line
    num_counts_g = len(re.findall('Guppy', line))
    counts_esther[chapter] += num_counts_e
    counts_guppy[chapter] += num_counts_g
print(counts_esther) #check that this comes out to be: [11, 0, 0, 18, 2, 0, 13, ...]
print(counts_guppy)


# your code here - display a plot with chapter on the x axis, counts_esther on the y axis
plt.plot(chapter_list,counts_esther,color='red')
plt.plot(chapter_list,counts_guppy,color='blue')
plt.xlabel('Chapter')
plt.ylabel('Mentions')
plt.legend(['Esther','Guppy'])
plt.title('Character Mentions per Chapter in Bleak House')

plt.savefig('character_count.png',dpi=200)
plt.show()
