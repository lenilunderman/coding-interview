my_dict = {
    "song":'this is your song',
    "author": 'elton john',
    "year": 1998,
}

print(my_dict["song"])
my_dict["song"] = "Paradise"
print(my_dict)

# Merging dictionaries
dict1 = {'color': 'blue', 'shape': 'circle'}
dict2 = {'color': 'red', 'number': 42}
dict1.update(dict2)
print(dict1)

# Python dictionaries accession methods
ex_dict = {"a": "anteater", "b": "bumblebee", "c": "cheetah"}

# accessing the keys of a dictionary
print(ex_dict.keys())

# acessing the values of a dictionary
print(ex_dict.values())

# acessing keys and values in a dictionary
print(ex_dict.items())

# method to get something from a dictionary if it exists
print(ex_dict.get("c"))