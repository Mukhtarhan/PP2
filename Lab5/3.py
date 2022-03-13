import re

pattern='[a-m]*'
text="abcdff12587"
x=re.findall(pattern,text)
print(x)
