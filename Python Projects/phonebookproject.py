Phonebook = {"James" : "+44 034587321",
              "Ali"   : "+44 094245287",
              }
PBList = []

counter = 0

for key in Phonebook.keys():
    print("Putting the key",key,"Into a list")
    PBList.append([])
    PBList[counter].append(key)
    counter = counter + 1

counter = 0

for values in Phonebook.values():
    print("Putting the value",values,"Into a list")
    PBList[counter].append(values)
    counter = counter + 1

print(PBList)

