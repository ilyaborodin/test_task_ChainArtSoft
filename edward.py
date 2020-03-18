import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'), help='Path to txt file')
file = parser.parse_args().file

with file:
    text = file.readline()

counter = 0
pre_char = ""
result = ""
for char in text:
    if char == pre_char:
        counter += 1
        continue
    elif counter % 2 == 0:
        result += ""
    elif counter % 2 == 1:
        result += pre_char
    pre_char = char
    counter = 1

print(result)
