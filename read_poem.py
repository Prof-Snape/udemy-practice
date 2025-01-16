# jabber = open("Jabberwocky.txt", "r")
# for i in jabber:
#     print(i.rstrip())
#
# jabber.close()

with open("Jabberwocky.txt", "r") as jabber:
    for i in jabber:
        print(i.rstrip())
