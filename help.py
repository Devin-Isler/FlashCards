data = []
with open("tr", "r") as file:
    lines = file.readlines()
    for line in lines:
        word, _ = line.split()
        data.append(word)

with open("new","w") as file:
    for d in data:
        file.write(f"{d.title()}\n")