with open("my_file.txt") as file:
    content = file.read()
    print(content)

with open("my_file.txt", mode="a") as file:
    file.write("\nMy name is Minnie")

with open("new_file.txt", mode="a") as file:
    file.write("\nMy name is Pluto!")





