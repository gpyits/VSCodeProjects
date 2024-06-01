# Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti. 
# Il sistema dovrà essere capace di gestire una collezione di ricette e i loro ingredienti.

# Classe RecipeManager:
#     Gestisce tutte le operazioni legate alle ricette.
#     Metodi:
#     - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. 
#       Restituisce un dizionario con la ricetta appena creata o un messaggio di errore se la ricetta esiste già.
#
#     - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. 
#       Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.
#
#     - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. 
#       Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
#
#     - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. 
#       Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
#
#     - list_recipes(): Elenca tutte le ricette esistenti.
#
#     - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. 
#       Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.
#
#     - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. 
#       Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.
class RecipeManager:
    def __init__(self) -> None:
        self.recipes: dict[str, list[str]]={}
    def create_recipe(self, name: str, ingredients: list[str]) -> dict[str, list[str]]:
        if name not in self.recipes: self.recipes[name]=ingredients; return {name:self.recipes[name]}
        else: raise ValueError('Error: recipe already exists')
    def add_ingredient(self, recipe_name: str, ingredient: str) -> dict[str, list[str]]:
        if recipe_name in self.recipes: 
            if ingredient not in self.recipes[recipe_name]: self.recipes[recipe_name].append(ingredient); return {recipe_name:self.recipes[recipe_name]}
            else: raise ValueError('Error: ingredient already is among recipe ingredients')
        else: raise ValueError('Error: recipe does not exist')
    def remove_ingredient(self, recipe_name: str, ingredient: str) -> dict[str, list[str]]:
        if recipe_name in self.recipes: 
            if ingredient in self.recipes[recipe_name]: self.recipes[recipe_name].remove(ingredient); return {recipe_name:self.recipes[recipe_name]}
            else: raise ValueError('Error: ingredient is not among recipe ingredients')
        else: raise ValueError('Error: recipe does not exist')
    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str) -> dict[str, list[str]]:
        if recipe_name in self.recipes: 
            if old_ingredient in self.recipes[recipe_name]: self.recipes[recipe_name][self.recipes[recipe_name].index(old_ingredient)]=new_ingredient; return {recipe_name:self.recipes[recipe_name]}
            else: raise ValueError('Error: ingredient is not among recipe ingredients')
        else: raise ValueError('Error: recipe does not exist')
    def list_recipes(self) -> list[str]:
        return [k for k in self.recipes.keys()] #print(*[f'Recipe {k} with ingredients: {v}' for k, v in self.recipes.items()], sep='\n')
    def list_ingredients(self, recipe_name: str) -> list[str]:
        try: return self.recipes[recipe_name]
        except ValueError: raise ValueError('Error: recipe does not exist')
    def search_recipe_by_ingredient(self, ingredient: str) -> dict[str, list[str]]:
        searched_recipes=[{k:v} for k, v in self.recipes.items() if ingredient.lower() in [i.lower() for i in self.recipes[k]]][0]
        return searched_recipes if searched_recipes else f'Error: no valid recipe found for ingredient "{ingredient.title()}"'
    
manager = RecipeManager()
print(manager.create_recipe("Torta di mele", ["Farina", "Uova", "Mele"]))
print(manager.add_ingredient("Torta di mele", "Zucchero"))
print(manager.list_recipes()) # ['Torta di mele']
print(manager.list_ingredients("Torta di mele"))
print(manager.search_recipe_by_ingredient("Uova"))

# {'Torta di mele': ['Farina', 'Uova', 'Mele']}
# {'Torta di mele': ['Farina', 'Uova', 'Mele', 'Zucchero']}
# ['Torta di mele']
# ['Farina', 'Uova', 'Mele', 'Zucchero']
# {'Torta di mele': ['Farina', 'Uova', 'Mele', 'Zucchero']}