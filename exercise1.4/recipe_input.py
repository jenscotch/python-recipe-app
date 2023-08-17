import pickle

def take_recipe():
    name = str(input("Enter the name of the recipe: "))
    cooking_time = int(input("Enter the cooking time for the recipe in minutes: "))
    ingredients = input("Enter the ingredients for the recipe: ")
    ingredients = ingredients.split()
    ingredients = [ingredient.lower() for ingredient in ingredients]
    recipe = {
        'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients
        }
    difficulty = calc_difficulty(recipe)
    return recipe

def calc_difficulty(recipe):
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = "Easy"

    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = "Medium"

    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = "Intermediate"

    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = "Hard"

recipes_list = []
all_ingredients = []

file_name = str(input("Enter a file name for the recipes: "))
try:
    recipes_file = open(file_name, 'rb')
    data = pickle.load(recipes_file)
except FileNotFoundError:
    print("File not found. Creating new file.")
    data = {'recipes_list': [], 'all_ingredients': []}
except:
    print("Unexpected error. Creating new file.")
    data = {'recipes_list': [], 'all_ingredients': []}
else:
    recipes_file.close()
finally:
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']

num = int(input("Input the number of recipes you would like to add: "))

for i in range(num):
    recipe = take_recipe()
    print(recipe)

    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)
    
    recipes_list.append(recipe)

data = {
    'recipes_list': recipes_list,
    'all_ingredients': all_ingredients
    }

new_file_name = str(input("Enter a name for your new file."))
new_file_name = open(new_file_name, 'wb')
pickle.dump(data, new_file_name)