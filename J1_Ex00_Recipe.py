#Recipe.py

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type): 
        self.name = name                                #name (str): name of the recipe,
        self.cooking_lvl = cooking_lvl                   #= {1,2,3,4,5}     #(int): range from 1 to 5,
        self.cooking_time = cooking_time                 #(int): in minutes (no negative numbers),
        self.ingredients = ingredients 
        self.description = description                 #(str): description of the recipe,
        self.recipe_type = recipe_type #= {'starter[], lunch[], dessert[]'}              #(str): can be "starter", "lunch" or "dessert".

        cooking_lvl = {"1","2","3","4","5"} 
        recipe_type = {"starter", "lunch", "dessert"} 
        ingredients  = []


    def __str__(self):
        str(self.cooking_lvl)
        txt ="Receipte Name" +self.name + "\nCooking level: " + str(self.cooking_lvl) + "\nIngredients: " + str(self.ingredients)
        + "\nDescription: " + str(self.description) 
        print(str.name, str.desc)

Ex2 = Recipe('Pie', '2', '15', 'butter', 'large', 'dessert')
print(f'{Ex2.name} is level {Ex2.cooking_lvl}, is made in {Ex2.cooking_time} min, with {Ex2.ingredients}, using a {Ex2.description} recipe and is a {Ex2.recipe_type}.')
