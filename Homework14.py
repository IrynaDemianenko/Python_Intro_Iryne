with open('in.txt', 'r') as file:
    file_contents = file.read()

file_new = file_contents.split()
newlist = list(filter(lambda x: len(x)>=5, file_new))
print(newlist)
newlist1 = ' '.join(map(str, newlist))
print(newlist1)
with open('out.txt', 'w') as file:
    file.write(newlist1)
