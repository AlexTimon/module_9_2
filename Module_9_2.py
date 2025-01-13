first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [str(len(x)) for x in first_strings if len(x) >= 5]

second_result = [(z, y) for z in first_strings for y in second_strings if len(z) == len(y)]

combined_string = first_strings + second_strings

third_result = {a: len(a) for a in combined_string if len(a) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)

