import re
name = 'CamelCaseName'
name = re.sub(r'(?<!^)(?=[a-z])', '', name).upper()
print(name)
