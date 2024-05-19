# Si immagini una funzione che comprime i file all'80% e li salva su un supporto di memorizzazione. 
# Prima che il file compresso venga memorizzato, deve essere diviso in blocchi da 512 byte ciascuno.

# Si sviluppi in Python un algoritmo per questa funzione che prende in input una lista di valori interi, 
# dove ogni valore intero della lista rappresenta la dimensione non compressa di un singolo file espressa in byte.

# Tale funzione deve utilizzare un ciclo per iterare la lista e, per ogni dimensione non compressa, 
# deve calcolare la dimensione compressa di tale file espressa come float (ovvero deve calcolare l' 80% della dimensione non compressa), 
# calcolare il numero di blocchi (arrotondato al numero intero più vicino) da 512 byte necessari per la memorizzazione, 
# al fine di determinare se il file compresso può essere salvato nello spazio rimanente nel supporto di memorizzazione o meno.

# In caso affermativo, il programma memorizza il file. 
# In tal caso, la funzione deve stampare la dimensione originale del file, la dimensione compressa, 
# i blocchi utilizzati per memorizzare il file in questione e i blocchi disponibili rimasti sul supporto di memorizzazione. 
# Ad esempio, se è possibile salvare sul supporto di memorizzazione un file avente dimensione pari a 1100 byte, la funzione stamperà:

# "File di 1100 byte compresso in 880.0 byte e memorizzato. Blocchi usati: 2. Blocchi rimanenti: 998."

# Il ciclo continua finché non viene riscontrato un file della lista 
# la cui dimensione compressa occupa un numero di blocchi più grande di quelli rimasti disponibili sul supporto di memorizzazione. 
# In tal caso, la funzione deve avvisare l'utente che lo spazio disponibile sul supporto di memorizzazione non è sufficiente per salvare il file. 
# Ad esempio, se non è possibile salvare sul supporto di memorizzazione un file avente dimensione pari a 1048576 byte, la funzione stamperà:

# "Non è possibile memorizzare il file di 1048576 byte. Spazio insufficiente."
# Inizialmente, il numero totale di blocchi disponibili sul supporto di memorizzazione per il salvataggio dei file è un numero intero pari a 1000 blocchi. 

def memorizza_file(files: list[int]) -> None:
    remaining_blocks=1000
    for file in files:
        compressed_file=file*80/100
        used_blocks=round(compressed_file/512)
        remaining_blocks-=used_blocks
        if remaining_blocks>0:
            print(f'File di {file} byte compresso in {compressed_file} byte e memorizzato. Blocchi usati: {used_blocks}. Blocchi rimanenti: {remaining_blocks}.')
        else:
            print(f'Non è possibile memorizzare il file di {file} byte. Spazio insufficiente.')
            break

memorizza_file([1100, 20000, 1048576, 512, 5000])

# File di 1100 byte compresso in 880.0 byte e memorizzato. Blocchi usati: 2. Blocchi rimanenti: 998.
# File di 20000 byte compresso in 16000.0 byte e memorizzato. Blocchi usati: 31. Blocchi rimanenti: 967.
# Non è possibile memorizzare il file di 1048576 byte. Spazio insufficiente.