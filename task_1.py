from pprint import pprint

file_path = "recipes.txt"

def get_dict(path):
    recipe_dict = {}
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            name = line.strip()
            items_list = []
            total_items = int(file.readline())
            for items in range(total_items):
                ingredient_name, quantity, measure = file.readline().strip().split("|")
                items_list.append({"ingredient_name": ingredient_name.strip(), "quantity" : int(quantity), "measure": measure.strip()})
            recipe_dict[name] = items_list
            file.readline()
    return recipe_dict

pprint(get_dict(file_path), width=100)