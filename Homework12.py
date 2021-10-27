with open('in.txt', 'r') as file:
    file_contents = file.read()


newlist = []
newlist=file_contents.split()
print(newlist)
newlist.sort()
print(newlist)
newlist1 = ''.join(str(e) for e in newlist)

with open('out.txt', 'w') as file:
    file.write(newlist1)
