import re

pattern='[A-Z]'

txt = "The rain in Spain"
x = re.split(pattern, txt)
print(x)
