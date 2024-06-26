# Crea un context manager usando una classe
# Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.
# Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__
# Esempio di funzionamento:
# Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.
# with FileManager('example.txt', 'w') as f:
#     f.write('Hello, world!')
class FileManager:
    def __init__(self, filename: str, mode: str) -> None:
        self.filename: str='Esercizi/Lezione 15/'+filename
        self.mode: str=mode
    def __enter__(self) -> None:
        self.file = open(self.filename, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, traceback) -> None:
        if exc_type:
            self.file.close()
            print('Caught an exception')
            print(f'Exception type: {exc_type}')
            print(f'Exception value: {exc_val}')
            print(f'Traceback: {traceback}')
        else:
            self.file.close()
        return False

with FileManager('example.txt', 'w') as f:
    f.write('Hello, world!')

#decorator
def decorator(func) -> None:
    def wrapper(*args):
        try:
            print('File opened')
            func(*args)
            print('File closed')
        except Exception as e:
            print(f'Caught an exception: {e}')
    return wrapper

def file_manager(filename: str, mode: str) -> None:
    with open(filename, mode) as f:
        f.close()

file_manager=decorator(file_manager)
file_manager('example.txt', 'w')

# Crea un context manager che permette di calcolare il tempo che viene impiegato ad eseguire le istruzioni che si trovano nel with
# with Timer():
#     time.sleep(1)
# time elapsed: 1.00000
# in questo esempio il tempo passato non sarà mai uguale a 1
import time

class Timer:
    def __init__(self) -> None:
        self.time: float
    def __enter__(self) -> None:
        self.time: float=time.time()
    def __exit__(self, exc_type, exc_val, traceback) -> None:
        if exc_type:
            print('Caught an exception')
            print(f'Exception type: {exc_type}')
            print(f'Exception value: {exc_val}')
            print(f'Traceback: {traceback}')
        else:
            print(f'Elapsed time: {time.time()-self.time: .2f}')
        return False

with Timer():
    pass

#decorator
def timer(func) -> None:
    def wrapper():
        start=time.time()
        func()
        finish=time.time()
        print(round(finish-start, 2))
    return wrapper

def test_function():
    time.sleep(1)

test_function=timer(test_function)
test_function()