import re


txt = "The rain in S.a,n"
pattern='\s|,|[.]'
x = re.sub(pattern, ";", txt)
print(x)

