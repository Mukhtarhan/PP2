import re
pattern='[A-Z]'
txt="DdsfD fsdfDfds"
x = re.sub(pattern, " ", txt)
print(x)
