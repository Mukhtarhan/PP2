import re
name = 'CamelCaseName'
name = re.sub(r'(?<!^)(?=[a-z])', '', name).lower()
print(name)
