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


def get_shop_list_by_dishes(dishes, person_count=1):
    shop_list = {}
    for name in dishes:
        for ingredients in get_cook_book()[name]:
            if ingredients['ingredient_name'] in shop_list:
                shop_list[ingredients['ingredient_name']]['quantity'] += ingredients['quantity'] * person_count
            else:
                shop_list[ingredients['ingredient_name']] = {'quantity': ingredients['quantity'] * person_count, 'measure': ingredients['measure']}
    return shop_list


dishes = ["Омлет", "Фахитос"]

pprint(get_shop_list_by_dishes(dishes, 2), width=100)
