import re

input_raw = open('./input/day1.txt', 'r').read()

input = input_raw.strip().split('\n')

digit_mapping = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

converted_lines = []
sum = 0

for line in input:

    line_as_digits = ''

    for idx, _chara in enumerate(line):
        idx_start = idx
        end = idx_start + 1

        while end <= len(line):
            substr = line[idx_start:end]

            # print(f"current line: '{line}' | current substr: '{substr}' | start: {idx_start} | end: {end}")

            if substr.isdigit():
                # print(f"adding '{substr}' to '{line_as_digits}'")
                line_as_digits += substr
                break
            elif substr in digit_mapping.keys():
                # print(f"adding '{digit_mapping[substr]}' to '{line_as_digits}'")
                line_as_digits += digit_mapping[substr]
                break

            end += 1

    # print(line_as_digits)
    converted_lines.append(line_as_digits)

for line in converted_lines:
    combined = line[0] + line[-1]
    sum += int(combined)

print(f"sum: {sum}")