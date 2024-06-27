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
    def removeWord(self, word: str) -> None:
        self.__words.remove(word)
    def printGame(self) -> None:
        print(' ', self.getLetters()[0], ' ')
        print(self.getLetters()[1], self.getLetters()[2], self.getLetters()[3], sep=' ')
        print('', self.getLetters()[4], ' ', self.getLetters()[5], '')

class User:
    def __init__(self, name: str) -> None:
        self.name: str=name
        self.guessed_words_count: int=0
        self.score=0
    def raise_count(self) -> None:
        self.guessed_words_count+=1
    def getName(self) -> str:
        return self.name
    def getCount(self) -> int:
        return self.guessed_words_count
    def guess(self, game: Game) -> None:
        guess=input("Enter your guess: ")
        if guess in game.getWords():
            self.score+=len(guess)*2
            game.removeWord(guess)
    def addProfile(self) -> None:
        with open('leaderboard.txt', 'rw') as f:
            lines=f.readlines()
            f.seek(0)
            lines.append(f'User: {self.name}\nTotal score: 0\n\n')
            f.write(lines)
    def profileUpdate(self) -> None:
        with open('leaderboard.txt', 'rw') as f:
            lines=f.readlines()
            f.seek(0)
            if self.name in lines:
                score=int(lines[lines.index(self.name)+1][13:-2])+self.score
                lines[lines.index(self.name)+1]=f'Total score: {score}\n\n'
            else:
                self.addProfile()
                self.profileUpdate()

game=Game()
user=User(input("Enter your name: "))