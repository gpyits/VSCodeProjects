# Progettare un semplice sistema di gestione di studenti e corsi con i seguenti requisiti:
#  
# 1. Classe Student:
# Attributi:
#     student_id: str - identificatore univoco per lo studente.
#     courses: list[str] - la lista dei corsi ai quali lo studente è iscritto.
# Metodi:
#     enroll(course: str) - aggiunge il corso specificato alla lista dei corsi dello studente oppure stampa il messaggio "Lo studente è già iscritto al corso {course}."
#     get_courses(): restituisce la lista dei corsi ai quali lo studente è iscritto.

# 2. Classe School:
# Attributi:
#     students: dict[str, Student] - un dizionario per memorizzare gli studenti, in cui la chiave è una stringa ID mentre il valore è un oggetto di tipo Studente.
# Metodi:
#     create_student(student_id: str): crea un nuovo studente con l'ID specificato e una lista di corsi vuota oppure stampa il messaggio "Lo studente con ID {student_id} esiste già."
#     enroll_student(student_id: str, course: str): se lo studente esiste viene iscritto al corso specificato, altrimenti  stampa il messaggio "Studente non trovato."
#     get_student_courses(student_id: str): se lo studente esiste restituisce la lista dei corsi dello studente con l'ID specificato, 
#                                           altrimenti ritorna il messaggio "Studente non trovato."
#     get_student_list(): Ritorna una lista di tutte le chiavi all'interno del dizionario students.
#     search_by_course(self, course: str): Trova e restituisce tutti gli ID degli studenti iscritti ad un determinato corso. 
#                                          Restituisce una lista di tutte le chiavi all'interno del dizionario students che hanno il corso specificato tra i valori oppure 
#                                          il messaggio di errore "Nessuno studente è iscritto al corso {course}." se non ci sono studenti che frequentano il corso specificato.
class Student:
    def __init__(self, student_id: str) -> None:
        self.student_id: str=student_id
        self.courses: list[str]=[]
    def enroll(self, course: str) -> None:
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"Lo studente è già iscritto al corso {course}.")
    def get_courses(self) -> list[str]:
        return self.courses

class School:
    def __init__(self) -> None:
        self.students: dict[str, Student]={}
    def create_student(self, student_id: str) -> None:
        if student_id not in self.students:
            self.students[student_id]=Student(student_id)
        else:
            print(f"Lo studente con ID {student_id} esiste già.")
    def enroll_student(self, student_id: str, course: str) -> None:
        try:
            self.students[student_id].enroll(course)
        except:
            print("Studente non trovato.")
    def get_student_courses(self, student_id: str) -> list[str]:
        try:
            return self.students[student_id].get_courses()
        except:
            return "Studente non trovato."
    def get_student_list(self) -> list[str]:
        return [i for i in self.students.keys()]
    def search_by_course(self, course: str) -> list[str]:
        students: list[str]=[i for i in self.students.keys() if course in self.students[i].courses]
        return students if students else f"Nessuno studente è iscritto al corso {course}."
    
# Creazione di una nuova scuola
scuola = School()

# Creazione di nuovi studenti
scuola.create_student("1001")

# Iscrizione degli studenti ai corsi
scuola.enroll_student("1001", "Matematica")
scuola.enroll_student("1001", "Matematica")

# Tentativo di iscrizione di un corso per uno studente non esistente
scuola.enroll_student("1004", "Fisica")

# Verifica dei corsi degli studenti
print(scuola.get_student_courses("1001"))
print(scuola.get_student_courses("1004"))