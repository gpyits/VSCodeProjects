'''
###RENDERING GRAFICO###

Si vuole sviluppare un sistema in Python per gestire il rendering di diverse forme geometriche. 
Il sistema dovrà supportare almeno tre tipi di forme: quadrati, rettangoli, e triangoli rettangoli.

Definire la classe astratta Forma che sarà utilizzata per definire l'attributo corrispondente al nome della forma e le funzionalità base di ogni forma, 
come i metodi astratti getArea() per calcolare l'area e render() per disegnare su schermo la forma.

Definire la classe Quadrato che estende la classe Forma e aggiunge specifiche circa la lunghezza di un suo lato.
Il costruttore della classe deve ricevere come argomento solo il lato del quadrato, ed impostare il nome della forma su "Quadrato".
Il metodo getArea() deve calcolare l'area del quadrato.
Il metodo render() deve stamapre su schermo un quadrato avente lato pari al valore passato nel costruttore. 
Il quadrato da stampare deve essere un quadrato vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)

Definire la classe Rettangolo che estende la classe Forma e aggiunge specifiche circa la lunghezza della sua base e della sua altezza.
Il costruttore della classe deve ricevere come argomento solo la base e l'altezza del rettangolo, ed impostare il nome della forma su "Rettangolo".
Il metodo getArea() deve calcolare l'area del rettangolo.
Il metodo render() deve stampare su schermo un rettangolo avente base ed altezza pari ai valori passati nel costruttore. 
Il rettangolo da stampare deve essere un rettangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)

Definire la classe Triangolo che estende la classe Forma e aggiunge specifiche circa la dimensione di un lato del trinagolo (per semplicità, 
si suppone che il triangolo in questione sia un triangolo rettangolo).
Il costruttore della classe deve ricevere come argomento solo il lato del triangolo, ed impostare il nome della forma su "Triangolo".
Il metodo getArea() deve calcolare l'area del triangolo.
Il metodo render() deve stamapre su schermo un triangolo rettangolo avente i due cateti di lunghezza pari ai valori passati nel costruttore. 
Il traingolo da stampare deve essere un traingolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)
 
Hint: per il disegno utilizzare print("*", end=" "), dato che l'argomento end = " " permette di controllare come termina ogni chiamata a print, 
e impostandolo a uno spazio si può fare in modo che tutte le stampe successive siano sulla stessa riga, separate da uno spazio.

Esempi di output:
Ecco un Quadrato di lato 4!

* * * *
*     *
*     *
* * * *
L'area di questo quadrato vale: 16

Ecco un Rettangolo avente base 8 ed altezza 4!
* * * * * * * *
*             *
*             *
* * * * * * * *
L'area di questo rettangolo vale: 32

Ecco un Triangolo avente base 4 ed altezza 4!
*      
* *    
*   *  
* * * *
L'area di questo triangolo vale: 8.0
'''
from abc import *

class Shape(ABC):
    @abstractmethod
    def getArea(self) -> int:
        '''Returns shape area'''
        pass
    @abstractmethod
    def render(self) -> None:
        '''Prints  a graphic rendering of the shape'''
        pass
    def describeShape(self) -> None:
        '''Renders shape and gives a brief description'''
        print(f'\n{self.name} with height={self.height} and width={self.width}')
        self.render()
        print(f'The area of this {self.name.lower()} is: {self.getArea()}\n')

class Rectangle(Shape):
    def __init__(self, height: int, width: int) -> None:
        super().__init__()
        self.height: int=height
        self.width: int=width
        self.name: str='Rectangle'
        if not (height and width): raise ValueError('Rectangle sides can\'t be 0')
    def getArea(self) -> int:
        return self.height*self.width
    def render(self) -> None:
        if self.width!=1:
            for i in range(self.height): print('*', *[' ' for i in range(self.width-2)], '*') if i not in (0, self.height-1) else print(*['*' for i in range(self.width)])
        else: print(*['*' for i in range(self.height)], sep='\n')

class Square(Rectangle):
    def __init__(self, side: int) -> None:
        height, width=side, side
        super().__init__(height, width)
        self.name: str='Square'
        if not side: raise ValueError('Square side can\'t be 0')

class Triangle(Shape):
    def __init__(self, height: int, width: int) -> None:
        super().__init__()
        self.height: int=height
        self.width: int=width
        self.name: str='Triangle'
        if not (height and width): raise ValueError('Triangle sides can\'t be 0')
    def getArea(self) -> int:
        return (self.height*self.width)//2
    def render(self) -> None:
        for i in range(self.height): print('*', *[' ' for i in range(i-1)], '*') if i not in (0, self.height-1) else print('*') if i==0 else print(*['*' for i in range(self.width)])

Square(4).describeShape()
Rectangle(4, 8).describeShape()
Triangle(5, 5).describeShape()