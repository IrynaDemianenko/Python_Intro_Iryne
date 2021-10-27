with open('in.txt', 'r') as file:
    file_contents = file.read()


newlist = []
file_contents.split()
print(file_contents)
newlist=list(filter(lambda x: len(x)>5, file_contents))
newlist1 = ''.join(str(e) for e in newlist)
print(newlist1)
with open('out.txt', 'w') as file:
    file.write(newlist1)
