import random

class Game:
    def __init__(self) -> None:
        with open('Games/dictionary_en.txt', 'r') as f:
            lines=[line[:-1] for line in f.readlines()]
        self.__letters=random.sample('abcdefghijklmnopqrstuvwxyz', 6)
        self.__words=[line for line in lines if all(letter in [self.letters] for letter in line)]
    def getLetters(self) -> list[str]:
        return self.__letters
    def getWords(self) -> list[str]:
        return self.__words
    def removeWord(self) -> None:
        pass #####
    def printGame(self) -> None:
        pass

class User:
    def __init__(self, name: str) -> None:
        self.name: str=name
        self.guessed_words_count: int=0
    def raise_count(self) -> None:
        self.guessed_words_count+=1
    def getName(self) -> str:
        return self.name
    def getCount(self) -> int:
        return self.guessed_words_count
    def guess(self, game: Game) -> None:
        guess=input("Enter your guess: ")