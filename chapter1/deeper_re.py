import re

match = re.search(r"the phone number is ([\d-]+)", "37: the phone number is 1234-567-890")
print(match.group())
print(match.group(1))

"""
Match a phone pattern as part of a group (in brackets). Note the use of \d as a special
character for any digit.
"""
pattern = re.compile(r"The answer to question (\w+) is (yes|no)", re.IGNORECASE)
print(pattern)

print(pattern.search("Naturally, the answer to question 3b is YES").groups())


"""
Match all the occurrences of cities and state abbreviations in the text. Note
that they are separated by a single character, and the name of the city always
starts with an uppercase letter. Only four states are matched for simplicity:
"""
PATTERN = re.compile(r'([A-Z][\w\s]+?).(TX|OR|OH|MI)')
TEXT = 'the jackalopes are the team of Odessa,TX while the\
        knights are native of Corvallis OR and the mud hens come from\
        Toledo.OH; the whitecaps have their base in Grand Rapids,MI'
print(list(PATTERN.finditer(TEXT)))

print(re.search(r'the phone number is ([\d-]+)', '37: the phone number is 1234-567-890'))

PATTERN = re.compile(r'([A-Z][\w\s]+).(TX|OR|OH|MI)')
print(list(PATTERN.finditer(TEXT))[1])

PATTERN = re.compile(r'(?P<city>[A-Z][\w\s]+?).(?P<state>TX|OR|OH|MN)')
match = PATTERN.search(TEXT)
print(match.groupdict())  # Output: {'city': 'Odessa', 'state': 'TX'}
print(match.group("city"))  # Outputs: Odessa
print(match.group("state"))  # Outputs: TX
print(match.group(1), match.group(2))  # Outputs: Odessa TX
