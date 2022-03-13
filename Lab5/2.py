import re

pattern='ab{2}b|'
text="dfabbsdf"
x=re.findall(pattern,text)
print(x)
