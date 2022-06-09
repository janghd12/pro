char = re.compile(r'[A-Z][a-z]+:')

re.findall(char, script101)

a = [1, 2, 3, 4, 5, 2, 2]
set(a)

set(re.findall(char, script101))

rachel = "Rachel:"
rachel = re.sub(":", '', rachel)
rachel

rachel[:-1]

y = set(re.findall(char,script101))
z = list(y)
character = []
for i in z:
    character += [i[:-1]]
  
character

character = [x[:-1] for x in list(set(re.findall(r'[A-Z][a-z]+:',script101)))]
character

re.findall(r'\([A-Za-z].+[a-z|\.]\)', script101)[:6]
  
import os, re
os.chdir(r'C:\\Users\\user\\Downloads')
f = open('friends101.txt', 'r')
f.read(100)

f.seek(0)
  
sentences = f.readlines()
sentences[:3]
  
for i in sentences[:20]:
    if re.match(r'[A-Z][a-z]+:',i):
        print(i)
         
lines = [i for i in sentences if re.match(r'[A-z][a-z]+:', i)]
lines[:10]

would = [i for i in sentences if re.match(r'[A-z][a-z]+:', i) and re.search('would', i)]
would

take =  [i for i in sentences if re.match(r'[A-z][a-z]+:', i) and re.search('take', i)]
take

for i in take:
    print(i)
  
newf = open('would.txt', 'w')
newf.writelines(would)
newf.close()
