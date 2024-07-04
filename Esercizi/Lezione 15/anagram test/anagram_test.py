# Si richiede di sviluppare dei casi di test per funzioni date prendendo gli input da file.

# Prendere le soluzioni ottenute del test Moodle della lezione 9 (esercizi vari)
#   Creare dei nuovi casi di test utilizzando unittest
#   Gli input per ogni caso di test deve essere preso da un file dedicato con un formato bene definito scelto a piacere.
#   Scrivere l'output della funzione un file di output dedicato.

# Ed esempio: 
# Creare 5 nuovi casi di test per la funzione anagram(s, t) dove s e t sono anagrammi da comparare. 
# Gli input di ogni caso di test, quindi s e t, devono essere estrapolati da un file di input dedicato.

# Ogni caso di test deve avere un file di input separato che rispetti il formato scelto.
import unittest

from anagram import *
class AnagramTest(unittest.TestCase):
    def setUp(self) -> None:
        self.s='fried'
        self.t='fired'
        self.notAnAnagram='freud'
        self.notAnAnagramAnagram='dreuf'
    def test_anagram(self) -> None:
        self.assertEqual(anagram(self.s, self.t), True)
        self.assertEqual(anagram(self.s, self.t), True)
        self.assertEqual(anagram(self.s, self.notAnAnagram), False)
        self.assertEqual(anagram(self.t, self.notAnAnagram), False)
        self.assertEqual(anagram(self.notAnAnagram, self.notAnAnagramAnagram), True)

if __name__=='__main__':
    unittest.main()
