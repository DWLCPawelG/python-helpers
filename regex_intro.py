# re module introduction + exercises
# source: https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-Regular-Expressions
import re

"""
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"""

text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat
mat
pat
bat
"""

sentence = "Start a sentence and then bring it to an end"

# r'string' means 'raw string' - special characters such as \n \t are ignored, and treated as string characters
print(r"\tTab")
print("---------------------------------")
#### search for characters - case sensitive ####
pattern = re.compile(pattern=r"abc")
matches = pattern.finditer(string=text_to_search)
for match in matches:
    print(match)
# the above matches
print(text_to_search[1:4])
print("---------------------------------")

##### escaping characters #####
# . equals "every, single character"
pattern = re.compile(pattern=r".")
matches = pattern.finditer(string=text_to_search)
for match in matches:
    print(match)
print("---------------------------------")

# use \ before a special character to treat it literally
pattern = re.compile(pattern=r"\.")
matches = pattern.finditer(string=text_to_search)
for match in matches:
    print(match)
print("---------------------------------")

# useful for searching urls:
pattern = re.compile(pattern=r"coreyms\.com")
matches = pattern.finditer(string=text_to_search)
for match in matches:
    print(match)
print("---------------------------------")


#### anchors ####
# match Ha HaHa
# \b stands for Word boundary BEFORE Ha
pattern = re.compile(pattern=r"\bHa")
matches = pattern.finditer(string=text_to_search)
for match in matches:
    print(match)
print("---------------------------------")

# ^ matches beginning of a string
pattern = re.compile(pattern=r"^Start")
matches = pattern.finditer(string=sentence)
for match in matches:
    print(match)
print("---------------------------------")

# $ matches end of a string
pattern = re.compile(pattern=r"end$")
matches = pattern.finditer(string=sentence)
for match in matches:
    print(match)
print("---------------------------------")

#### exercises ####
# match phone number
pattern = re.compile(pattern=r"\d\d\d.\d\d\d.\d\d\d")
matches = pattern.finditer(string=text_to_search)
for match in matches:
    print(match)
print("---------------------------------")

# match phone number with character sets []
# no need to escape special characters in sets
pattern = re.compile(pattern=r"\d\d\d[.-]\d\d\d[.-]\d\d\d")
matches = pattern.finditer(string=text_to_search)
for match in matches:
    print(match)
print("---------------------------------")

# match phone number starting with 800 or 900
pattern = re.compile(pattern=r"[89]00.\d\d\d.\d\d\d")
matches = pattern.finditer(string=text_to_search)
for match in matches:
    print(match)
print("---------------------------------")

# match digit between 1 and 5
pattern = re.compile(pattern=r"[1-5]")
matches = pattern.finditer(string=text_to_search)
for match in matches:
    print(match)
print("---------------------------------")

# match uppercase & lowercase letters
pattern = re.compile(pattern=r"[a-zA-z]")
matches = pattern.finditer(string=text_to_search)
for match in matches:
    print(match)
print("---------------------------------")

# ^ in set negates the set content - so matches everything that is NOT in set
pattern = re.compile(pattern=r"[^a-zA-Z]")
matches = pattern.finditer(string=text_to_search)
for match in matches:
    print(match)
print("---------------------------------")

# match cat, pat, mat but not bat using caret in set
pattern = re.compile(pattern=r"[^b]at")
matches = pattern.finditer(string=text_to_search)
for match in matches:
    print(match)
print("---------------------------------")


#### quantifiers ####
# {3} matches exact number in the curly braces
# so \d{3} will match 3 digits
# phone number match using {3}
pattern = re.compile(pattern=r"\d{3}.\d{3}.\d{4}")
matches = pattern.finditer(string=text_to_search)
for match in matches:
    print(match)
print("---------------------------------")

# match patterns starting with Mr
pattern = re.compile(pattern=r"Mr\.?\s[A-Z]\w*")
matches = pattern.finditer(string=text_to_search)
for match in matches:
    print(match)
print("---------------------------------")


# match Mr, Ms & Mrs
# match patterns starting with Mr
pattern = re.compile(pattern=r"(Mr|Ms|Mrs)\.?\s[A-Z]\w*")
matches = pattern.finditer(string=text_to_search)
for match in matches:
    print(match)
print("---------------------------------")

# email pattern
emails = """
dwlcpablo@gmail.com
pablito888@o2.pl
pawel.grzybek.official@gmail.com
"""

pattern = re.compile(pattern=r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

matches = pattern.finditer(emails)

for match in matches:
    print(match)
print("---------------------------------")

# url pattern
urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

# use a group with ? for optional www
# groups in captured regex are numbered:
# (www\.) is group #1
# (\w+) is group #2
# (\.\w+) is group #3
# whole pattern is group #0
pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
matches = pattern.finditer(urls)
for match in matches:
    print(match)
    # print out whole matching pattern
    print(match.group(0))
    print(match.group(2))


# substitute() method using group indexes
# pattern.sub(r'\2\3', urls) will substitute all matches in urls with group #2 & #3
subbed_urls = pattern.sub(r"\2\3", urls)
print(subbed_urls)

print("--------------------------------")

#### findall() ####
# re.findall() returns a list of strings that match the pattern
pattern = re.compile(pattern=r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
matches = pattern.findall(emails)
print(matches)
for match in matches:
    print(match)
print("--------------------------------")


#### match() & search() ####
pattern = re.compile(pattern=r"Start")
# match only looks for pattern the the beginning of a string
matches = pattern.match(sentence)
print(matches)
# search() looks for pattern throughout the string
pattern = re.compile(pattern=r"sentence")
matches = pattern.match(sentence)
print(matches)
print("--------------------------------")


#### flags ####
# most popular IGNORECASE, ASCII, MULTILINE
# see docs https://docs.python.org/3/library/re.html#re.A
pattern = re.compile(pattern=r"S", flags=re.IGNORECASE)
matches = pattern.findall(sentence)
print(matches)
