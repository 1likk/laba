import re

#1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
pattern = 'ab*'
test_strings = ['ab', 'abb', 'abbb', 'ac', 'abc']

for test_string in test_strings:
    if re.fullmatch(pattern, test_string):
        print(f"Match found: {test_string}")

#2.Match a string that has an 'a' followed by two to three 'b's:
pattern = 'ab{2,3}'
test_strings = ['ab', 'abb', 'abbb', 'abbbb', 'ac', 'abc']

for test_string in test_strings:
    if re.fullmatch(pattern, test_string):
        print(f"Match found: {test_string}")

#3.Find sequences of lowercase letters joined with an underscore:
pattern = '[a-z]+_[a-z]+'
test_string = 'hello_world is_a_test string_with_underscores but_notThis'
matches = re.findall(pattern, test_string)
print("Matches:", matches)

#4.
pattern = '[A-Z][a-z]+'
test_string = 'Hello World Is A Test But NotThis'
matches = re.findall(pattern, test_string)
print("Matches:", matches)

#5.
pattern = 'a.*b$'
test_strings = ['acb', 'aXXXb', 'ab', 'acbdefb', 'abc']

for test_string in test_strings:
    if re.fullmatch(pattern, test_string):
        print(f"Match found: {test_string}")

#6.
pattern = '[ ,.]'
test_string = 'This is, a test. String'
result = re.sub(pattern, ':', test_string)
print("Result:", result)

#7
snake_case_string = 'this_is_a_snake_case_string'
camel_case_string = ''.join(word.title() for word in snake_case_string.split('_'))
print("Camel Case:", camel_case_string)

#8
pattern = '[A-Z][a-z]*'
test_string = 'SplitAtUpperCaseLetters'
matches = re.findall(pattern, test_string)
print("Matches:", matches)

#9
pattern = r'(?<!^)(?=[A-Z])'
test_string = 'InsertSpacesBetweenWordsStartingWithCapitalLetters'
result = re.sub(pattern, ' ', test_string)
print("Result:", result)

#10
camel_case_string = 'convertCamelCaseStringToSnakeCase'
snake_case_string = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_string).lower()
print("Snake Case:", snake_case_string)
