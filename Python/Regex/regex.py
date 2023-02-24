import re
string1 = "Test test test"
string2 = "zero zero zero \n Test"
string3 = "zero Test"

regex = re.compile("test", re.IGNORECASE | re.VERBOSE)

# re.match -> matches pattern and returns the first occurrence only at the beginning of the string in the first line
match = re.match(regex, string1)
if match:
    print(match)
    print(match.span())
    print(match.start())
    print(match.end())
    match_group = match.group(0)
    print(match_group)
    match_groups = match.groups()
    print(match_groups)

string = "zero zero zero \n zero Test"

# re.search-> matches pattern and returns the first occurrence in all the lines
match = re.search(regex, string)
if match:
    print(match)
    match_group = match.group(0)
    print(match_group)
    match_groups = match.groups()
    print(match_groups)

string = "Test test test \n Test"

# re.findall -> matches pattern and returns all occurrences in all the lines of the file
# return list of strings
matches = re.findall(regex, string)
for match in matches:
    print(match)

# re.finditer -> matches pattern and returns all occurrences in all the lines of the file
# return list of match objects
matches = re.finditer(regex, string)
for match in matches:
    print(match)
    print(type(match.group()))
