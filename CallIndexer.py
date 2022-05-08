import subprocess
import time

numbers = {}
old_index = {}
file = ""

print("\n")
print("-CallIndexer-\n")
filename = input("Number-list Filename: ")
print("\n")
index_filename = input("Index Filename. To create a new index from scratch, link to empty .txt file: ")
print("\nLoading numbers...")

# Adds all numbers into dictionary
with open(filename) as f:
    number_string = f.readlines()

for line in number_string:
    line = line.replace("\n", "")
    print(line)
    numbers.update({f"{line}": ""})

print("Done.\n")

# Adds old index into dictionary
with open(index_filename) as g:
    old_index_string = g.readlines()

for index_line in old_index_string:
    index_line = index_line.replace("\n", "")
    index_line_list = index_line.split(":=")
    if len(index_line_list[1]) != 0:
        old_index.update({f"{index_line_list[0]}": f"{index_line_list[1]}"})

print("Printing old index")
print(old_index)
print("\n")

# update index
for i in numbers:
    if old_index.get(i) is None:
        print(f"{i} has no index")
        subprocess.call(['java', '-jar', 'copy.jar', f'{i}'])
        index_update = input("New index: ")
        if index_update != "":
            numbers.update({f"{i}": f"{index_update}"})

    else:
        preexisting_index = old_index.get(i)
        numbers.update({f"{i}": f"{preexisting_index}"})

print("Printing completed index")
print(numbers)
print("\n")

time.sleep(2)

save_filename = input("Save to file: ")

# save to file
h = open(save_filename, "w")
for key, index in numbers.items():
    key_existence = False

    if index == "":
        continue
    for k in numbers.keys():
        if k == f"04131{key}":
            key_existence = True

    if len(key) >= 8:
        file = file + f"{key}:={index}\n"
    elif key_existence:
        file = file + f"{key}:={index}\n"
    else:
        file = file + f"04131{key}:={index}\n"

h.write(file)
h.close()
