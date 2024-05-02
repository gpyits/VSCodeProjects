# Nel gioco del blackjack, il valore di una mano è determinato dalla somma dei valori delle carte. 
# Ogni carta ha un valore compreso tra 2 e 11 compresi. 
# Tuttavia, se una mano contiene un asso, il valore dell'asso può essere 1 o 11, a seconda di quale sia più favorevole al giocatore in quel momento. 
# Dato un elenco di valori delle carte che rappresentano una mano di blackjack, scrivi una funzione per determinare il valore totale della mano.

cards=[2, 5, 11, 11]
def blackjack_hand_total(cards: list[int]) -> int:
    aces=0
    for r in range(len(cards)):
        if cards[r]==11 and sum(cards)>21:
            cards[r]=1
    if sum(cards)>21:
        return 0
    else:
        return sum(cards)
            
print(blackjack_hand_total(cards))