import re
text="sdsabbbbb"
pattern='ab*'
x=re.findall(pattern,text)
print(x)
