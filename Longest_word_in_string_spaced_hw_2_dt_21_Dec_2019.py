string = str(input("Enter the strings: "))
length = len(string)
m = 0
index = 0
count = 0
for i in range(length):
    if string[i] != ' ':
        count += 1
    else:
        if count > m:
            m = count
            index = i - count
        count = 0

if count > m:
    m = count
    index = i - count + 1

print(f'The longest string is: "{string[index:index + m]}", length: "{len(string[index:index + m])}".')