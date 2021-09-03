from pprint import pprint

file_path = "recipes.txt"


def get_cook_book(recipe=file_path):
    cook_book = {}
    with open(recipe, "r", encoding="utf-8") as file:
        for line in file:
            name = line.strip()
            items_list = []
            total_items = int(file.readline())
            for items in range(total_items):
                ingredient_name, quantity, measure = file.readline().strip().split("|")
                items_list.append({"ingredient_name": ingredient_name.strip(), "quantity": int(quantity), "measure": measure.strip()})
            cook_book[name] = items_list
            file.readline()
    return cook_book


pprint(get_cook_book(), width=100)
