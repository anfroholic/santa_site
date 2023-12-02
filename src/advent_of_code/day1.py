values = []

with open('day1input.txt', 'r') as f:
    for line in f:
        numbers = list('0123456789')
        char_nums = {v:str(k) for k,v in enumerate("zero one two three four five six seven eight nine".split())}
        for word, num in char_nums.items():
            line = line.replace(word, num)
        print(line)
        nums = [num for num in list(line) if num in numbers]
        value = ''.join([nums[0], nums[-1]])
        values.append(int(value))

print(values)
print(sum(values))
        