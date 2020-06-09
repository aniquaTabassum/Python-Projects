import random

def assign_ingredients(list_of_people, list_of_ingredients):
    f = open("decision", "w")


    original_length = len(list_of_people)
    index = 1
    for j in range(original_length):
        if len(list_of_people) == 1:
            index1 = 0

        else:
            index1 = random.randint(0, len(list_of_people) - 1)
            index2 = random.randint(4,7)
        selection = (str(index)+". "+list_of_people[index1]+" has to cook with "+str(index2)+"\n")
        print(selection)
        f.write(selection)
        index = index+1
        list_of_people.pop(index1)

    f.close()

def createNameList(file_name):
    x = ""
    with open(file_name, "r") as names:
        for line in names:
            x = line
    finalList = x.split("\n")
    return finalList[0].split(" ")


nameList = createNameList("names")
ingredientList = [6,7,8,9,10]
assign_ingredients(nameList, ingredientList)