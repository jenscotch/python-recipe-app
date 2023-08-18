recipes_list = []
ingredients_list = []

n = int(input("Input the number of recipes you would like to enter: "))

def make_recipe():
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter how long it takes to cook in minutes: "))
    ingredients = input("Enter all ingredients: ")
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients.split(', '),
        'difficulty': difficulty
    }
    return recipe

for i in range(n):
    recipe = make_recipe()
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

for recipe in recipes_list:
    if int(recipe['cooking_time']) < 10 and len(recipe['ingredients']) < 4:
        difficulty = 'Easy'
    elif int(recipe['cooking_time']) < 10 and len(recipe['ingredients']) >= 4:
        difficulty = 'Medium'
    elif int(recipe['cooking_time']) >= 10 and len(recipe['ingredients']) < 4:
        difficulty = 'Intermediate'
    elif int(recipe['cooking_time']) >= 10 and len(recipe['ingredients']) >= 4:
        difficulty = 'Hard'

        print('Recipe: ', recipe['name'])
        print('Cooking time (min): ', recipe['cooking_time'])
        print('Ingredients: ')
        for ingredient in recipe['ingredients']:
            print(ingredient)
        print('Difficulty level: ', difficulty)

print('''Ingredients available across all recipes
      ----------------------------------------- ''')
ingredients_list = []
for recipe in recipes_list:
    for ingredient in recipe['ingredients']:
        ingredients_list.append(ingredient)
sorted_list = [i for i in sorted(ingredients_list)]
for i in sorted_list:
    print(i)