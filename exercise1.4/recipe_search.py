import pickle

def display_recipe(recipe):
    print('Name: ', recipe['name'])
    print('Cooking time in minutes: ', recipe['cooking_time'])
    print('Ingredients: ', ', '.join(recipe['ingredients']))
    print('Difficulty: ', recipe['difficulty'])

def search_ingredient(data):
    ingredients_list = data['all_ingredients']
    indexed_ingredients_list = list(enumerate(ingredients_list, 1))

    for ingredient in indexed_ingredients_list:
        print('No.', ingredient[0], ' - ', ingredient[1])

    try:
        chosen_num = int(input('Enter the number that corresponds to your chosen ingredient: '))
        index = chosen_num - 1
        ingredient_searched = ingredients_list[index]
        ingredient_searched = ingredient_searched.lower()
    except IndexError:
        print('The number you entered is not on the list.')
    except:
        print('An error occured while finding your ingredient.')
    else: 
        for recipe in data['recipes_list']:
            for recipe_ing in recipe['ingredients']:
                if (recipe_ing == ingredient_searched):
                    print('\nThe following recipe includes the searched ingredient: ')
                    print('------------------------------------------------')
                    display_recipe(recipe)


file_name = str(input('Enter the file where you have stored your recipes: '))
try:
    recipes_file = open(file_name, 'rb')
    data = pickle.load(recipes_file)

except FileNotFoundError:
    print('File does not exist in the current directory')
    data = {'recipes_list': [], 'all_ingredients': []}

except:
    print('An unexpected error occured')
    data = {'recipes_list': [], 'all_ingredients': []}

else:
    search_ingredient(data)