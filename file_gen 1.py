#3 Use Generators to read the file And Print all the words in a file.


filename = "D:\\Javascript\\function\\python\\file01.txt"

lines = (line for line in open(filename, "r"))

li_lines = (li.splitlines() for li in lines)

print(type(lines))
print(type(li_lines))
print(type(filename))
for li in lines:
        print(li)
