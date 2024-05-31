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
    pass

manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))

#Expected:
# {'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella']}
# {'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella', 'Basilico']}
# {'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}
# {'Pizza Margherita': ['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}
# ['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']