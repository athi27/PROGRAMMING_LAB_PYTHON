fn1=open("file.txt",'r')
s=fn1.readlines()
for x in range(0,len(s)):
    print(s[x])
fn1.close()