import re

pattern='^a.*b$'
text="adfsdfbdsf45b"
x=re.findall(pattern,text)
print(x)
