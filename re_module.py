import re

email_list = ["john.doe@example.com", "jane.smith@example.net", "bob@example.com", "alice@example.org"]

# Define a regular expression pattern to match email addresses ending with ".com"
pattern = r'(\b([\w\.]+)@(\w+\.com)(\d)?\b)'
pattern2 = r'[\w\.]+@\w+\.com'
# Create a regex object using the pattern


# Use the findall() method to extract all the email addresses that match the pattern
text = " ".join(email_list)
# print(text)


# Print the list of email addresses ending with ".com"

# print(match.group(2, 3))


# print(match.group()) ->
# print(match.groups()) ->
# print(match.start()) -> index first match letter
# print(match.end()) -> index last match letter

# print(match.span())
# print(match.expand(r"\1 text"))


regex = r'^(?P<name>[A-Za-z]+) is (?P<age>\d+) years old$'
input_str = 'John is 25 years old'
match = re.match(regex, input_str)

print(match.group(1))
print(match.group(0))
print(match.groups())
print(match.groupdict())
print(match.expand('Hello, \g<name>! You are \g<age> years old.'))
# print(match.expand('Hello, \g<name>! You are \g<age> years old.')) -> Hello, John! You are 25 years old.
# print(match.groupdict()) -> {'name': 'John', 'age': '25'}


# re.search() - Searches throughout the text
# re.search(r'Analytics', 'AV Analytics Vidhya AV') -> Analytics

# re.split() - split string for term
# result_split = re.split(r'@', 'AOYastrebov@gmail.com')  -> ['AOYastrebov', 'gmail.com']

# re.fullmatch() -> check whole string matches the regular expression pattern

# re.match() - start find the result on the first letter
# re.match(r'AV', 'AV Analytics Vidhya AV')  ->  None

# re.findall(pattern, text) - find all words for pattern. create list with findwords
# re.findall(r'AV', 'AV Analytics Vidhya AV') -> ['AV', 'AV']

# re.sub()
# re.sub(pattern, repl, string) - replese the part of text

# re.compile(pattern, repl, string)
# pattern = re.compile('AV') - create regular expression object
# result = pattern.findall('AV Analytics Vidhya AV')

# re.subn() - the same that sub, but return tuple with second param count of replese part
# text_sub = 'I have a lot of fruts. There are apples and pears. I have a lot of vegitables. There are potatos and tomatos.'
# pattern_subn = r'I have'
# res = re.subn(pattern_subn, 'He has', text_sub)


# re.escape() - returns a string where any characters that have a special meaning in regular expressions are escaped with a backslash
# pattern = "(hello+world)*"
# escaped_pattern = re.escape(pattern) -> \(hello\+world\)\*

# re.purge -> Clear the regular expression cache.

# re.finditer() -> The same that findall, but method returns an iterator.

# re.template()


# m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
#
# m.groupdict()
# {'first_name': 'Malcolm', 'last_name': 'Reynolds'}

text = """
Hello, my name is John Doe and my email is john.doe@example.com. You can also reach me at (555) 123-4567.

I work at https://www.example.com as a software engineer. You can visit our website to learn more about our products and services.

If you have any questions, you can email our customer support team at support@example.com or call us at (555) 987-6543.

My colleague, Jane Smith, can also help you with any inquiries. You can contact her at jane.smith@example.com or (555) 555-1212.

Thank you for your interest in our company!
"""

text2 = """
Hello, my name is John Doe and my email is john.doe@example.com. You can also reach me at (555) 123-4567.

I work at https://www.example.com as a software engineer. You can visit our website to learn more about our products and services.

If you have any questions, you can email our customer support team at support@example.com or call us at (555) 987-6543.

My colleague, Jane Smith, can also help you with any inquiries. You can contact her at jane.smith@example.com or (555) 555-1212.

Our company website is https://www.example-company.com and our phone number is (555) 555-5555. You can email us at info@example-company.com.

We also have offices in New York (212) 555-1234 and San Francisco (415) 555-5678.

Other team members include:

- Alice Johnson (alice.johnson@example.com)
- Bob Williams (bob.williams@example.com)
- Emily Davis (emily.davis@example.com)

Thank you for your interest in our company!
"""
pattern_phone_number = r'\(\d{3}\) \d{3}-\d{4}'
pattern_email = r'\b[\w\.]+@[\w\.]+\b'
pattern_name = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
pattern_url = r'https://[a-z\._]+'

# names = re.findall(pattern_name, text2)
# phone_numbers = re.findall(pattern_phone_number, text2)
# emails = re.findall(pattern_email, text2)
# urls = re.findall(pattern_url, text2)


import re

CSA_RE = r"(\w{8})(\w{8})(\w{6})(\w{2})(\w{2})(\w{2})(\w+)(\s)?"


def to_csa_msg(message):
    res = re.match(CSA_RE, message.lower())
    if not res:
        return None
    print('pattern -> r"(\w{8})(\w{8})(\w{6})(\w{2})(\w{2})(\w{2})(\w+)"')
    print('msg ->', msg)
    print('msg after fullmatch -> (00189ba7),(00000000), (90eb13), (00), (20), (1d), (050205025a0500050005000005210500189ba705000005000500000000050a0a1c73), None')
    print('res.group()  --> ', res.group())
    print(res.expand(r'\7,\1'))
    print('res.group(0)  --> ', res.group(0))
    print('res.group(1)  --> ', res.group(1))
    print('res.group(1,3,5)  --> ', res.group(1, 3, 5))
    print('res.group(1,8)  --> ', res.group(1, 8))
    print('res.group(1, 2, 3, 4, 5, 6, 7, 8)  --> ', res.group(1, 2, 3, 4, 5, 6, 7, 8))
    print('res.groups()  --> ', res.groups())
    print('res.groups("my_result")  --> ', res.groups('my_result'))


msg = "00189BA70000000090EB1300201D050205025A0500050005000005210500189BA705000005000500000000050A0A1C73@error"  # noqa: E501
to_csa_msg(msg)
