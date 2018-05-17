def create_recipe_line(name, quantity, measure):
    return {'ingredients_name': name, 'quantity': int(quantity), 'measure': measure}


def get_cookbook_from_file(filename):
    cook_book = dict()
    with open(filename, "r", encoding="utf-8") as f:
        for recipe in f.read().split("\n\n"):
            name, count, *recipes = recipe.split("\n")
            name = name.lower()
            cook_book[name] = []
            for i in range(int(count)):
                line = recipes[i].split("|")
                cook_book[name].append(create_recipe_line(*line))

    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        for ingredients in cook_book[dish]:
            new_shop_list_item = dict(ingredients)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredients_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredients_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredients_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print(f"{shop_list_item['ingredients_name']} {shop_list_item['quantity']} {shop_list_item['measure']}")


def create_shop_list(cook_book):
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    print_shop_list(shop_list)


create_shop_list(get_cookbook_from_file("recipes.txt"))
