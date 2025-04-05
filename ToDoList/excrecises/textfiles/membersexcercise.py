file = open('files/members.txt', 'r')
members = file.readlines()
file.close()

member = input('Enter a new member')

members.append(member)
file = open('files/members.txt', 'w')
file.writelines(members)
file.close()


# altneratively you can append directly to existing file by file.write(str)
