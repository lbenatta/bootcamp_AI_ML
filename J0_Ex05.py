


#-----------Part 1: Nested Dictionaries
Create a dictionary called cookbook. You will use this cookbook to store recipe.
A recipe is a dictionary that stores (at least) 3 couples key-value:
• ”ingredients": a list of string representing the list of ingredients
• "meal": a string representing the type of meal
• "prep_time": a non-negative integer representing a time in minutes
In the cookbook, the key to a recipe is the recipe name.
Initialize your cookbook with 3 recipes:
• The Sandwich’s ingredients are ham, bread, cheese and tomatoes. It is a lunch and
it takes 10 minutes of preparation.
• The Cake’s ingredients are flour, sugar and eggs. It is a dessert and it takes 60
minutes of preparation.
• The Salad’s ingredients are avocado, arugula, tomatoes and spinach. It is a lunch
and it takes 15 minutes of preparation.

cookbook = {'ingredients': {'key_1': 'value_1'},
            'meal': {'key_2': 'value_2'}
            'prep_time': {'key_3': 'value_3'}

cookbook = {'Sandwitch': {'ingredients':{'ham, bread, cheese, tomatoes', 'meal': 'Sandwitch', 'prep_time':'10 min'},
            'Cake’: 'ingredients':{'flour, sugar , eggs', 'meal':'dessert', 'prep_time': '60'},
            'Salad': 'ingredients':{'avocado, arugula, tomatoes, spinach',  'meal':Salad, 'prep_time': '15'}
print(cookbook)