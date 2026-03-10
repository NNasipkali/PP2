import re

# 1. 'a' followed by zero or more 'b'
pattern = r"ab*"
print(re.findall(pattern, "ab abb abbb a"))

# 2. 'a' followed by two to three 'b'
pattern = r"ab{2,3}"
print(re.findall(pattern, "ab abb abbb abbbb"))

# 3. lowercase letters joined with underscore
pattern = r"[a-z]+_[a-z]+"
print(re.findall(pattern, "hello_world test_case my_var"))

# 4. uppercase followed by lowercase letters
pattern = r"[A-Z][a-z]+"
print(re.findall(pattern, "Hello World Python Regex"))

# 5. 'a' followed by anything ending in 'b'
pattern = r"a.*b"
print(re.findall(pattern, "aab axxb acccb"))

# 6. replace space, comma or dot with colon
text = "Hello, world. Python regex"
print(re.sub(r"[ ,\.]", ":", text))

# 7. snake_case → camelCase
def snake_to_camel(text):
    return re.sub(r"_([a-z])", lambda x: x.group(1).upper(), text)

print(snake_to_camel("hello_world_python"))

# 8. split string at uppercase letters
text = "HelloWorldPythonRegex"
print(re.split(r"(?=[A-Z])", text))

# 9. insert spaces between capital words
text = "HelloWorldPython"
print(re.sub(r"([A-Z])", r" \1", text).strip())

# 10. camelCase → snake_case
def camel_to_snake(text):
    return re.sub(r"([A-Z])", r"_\1", text).lower()

print(camel_to_snake("helloWorldPython"))