def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name, set(dish_ingredients))

def check_drinks(drink_name, drink_ingredients):
    from sets_categories_data import ALCOHOLS
    if set(drink_ingredients).isdisjoint(ALCOHOLS):
        return f"{drink_name} Mocktail"
    return f"{drink_name} Cocktail"

def categorize_dish(dish_name, dish_ingredients):
    from sets_categories_data import VEGAN, VEGETARIAN, PALEO, KETO, OMNIVORE
    names = ["VEGAN", "VEGETARIAN", "PALEO", "KETO", "OMNIVORE"]
    categories = [VEGAN, VEGETARIAN, PALEO, KETO, OMNIVORE]
    for index, category in enumerate(categories):
        if category >= set(dish_ingredients):
            return f"{dish_name}: {names[index]}"

def tag_special_ingredients(dish):
    from sets_categories_data import SPECIAL_INGREDIENTS
    print_ingredients = SPECIAL_INGREDIENTS.intersection(dish[1])
    return (dish[0], print_ingredients)

def compile_ingredients(dishes):
    ingredients = set()
    for dish in dishes:
        ingredients = ingredients.union(dish)
    return ingredients

def separate_appetizers(dishes, appetizers):
    return set(dishes).difference(set(appetizers))

def singleton_ingredients(dishes, INTERSECTION):
    singleton_set = set()
    for dish in dishes:
        singleton_set = dish.symmetric_difference(singleton_set)
    return singleton_set.difference(INTERSECTION)