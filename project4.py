import os, re
os.chdir(r'C:\Users\user\python')
f = open('friends101.txt', 'r', encoding = 'utf8')
script101 = f.read()
print(script101[:100]

Line = re.findall(r'Monica:.+', script101)
print(Line[:3])
      
for item in Line[:3]:
print(item)
f.close()
f = open('monica.txt', 'w', encoding = 'utf8')
monica = ''
for i in Line:
monica += i 
f.weite(monica)
f.close()
print('다음과 같은 표기를 줄을 바꿀 수 있습니다. \.n이제 줄이 바뀌었군요!')
monica = ''
for i in Line:
monica += i +'\n'
monica[:100]
f = open('monica.txt', 'w', encoding = 'utf-8')
f.write(monica)
f.close()
