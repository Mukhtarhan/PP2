import re

pattern='[A-Z]*[a-z]*'
text="SADddkfkSkks"
x=re.findall(pattern,text)
print(x)
