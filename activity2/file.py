c=0
s = "hello world"
n = 'l'
s1=len(s)-1
for i in range(len(s)):
if s[i] == n:c+=1
elif i == s1:print("Output is ",c)