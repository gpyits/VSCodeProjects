# Progettare un semplice sistema di gestione di studenti e corsi con i seguenti requisiti:

# 1. Classe Student:
#   Attributi:
#       student_id: str - identificatore univoco per lo studente.
#       courses: list[str] - la lista dei corsi ai quali lo studente è iscritto.
#   Metodi:
#       enroll(course: str) - aggiunge il corso specificato alla lista dei corsi dello studente oppure stampa il messaggio "Lo studente è già iscritto al corso {course}."
#       get_courses(): restituisce la lista dei corsi ai quali lo studente è iscritto.

# 2. Classe School:
#   Attributi:
#       students: dict[str, Student] - un dizionario per memorizzare gli studenti, in cui la chiave è una stringa ID mentre il valore è un oggetto di tipo Studente.
#   Metodi:
#       create_student(student_id: str): 
#           crea un nuovo studente con l'ID specificato e una lista di corsi vuota oppure stampa il messaggio "Lo studente con ID {student_id} esiste già."
#       enroll_student(student_id: str, course: str): 
#           se lo studente esiste viene iscritto al corso specificato, altrimenti  stampa il messaggio "Studente non trovato."
#       get_student_courses(student_id: str): 
#           se lo studente esiste restituisce la lista dei corsi dello studente con l'ID specificato, altrimenti ritorna il messaggio "Studente non trovato."
#       get_stundent_list(): 
#           Ritorna una lista di tutte le chiavi all'interno del dizionario students.
#       search_by_course(self, course: str): 
#           Trova e restituisce tutti gli ID degli studenti iscritti ad un determinato corso. 
#           Restituisce una lista di tutte le chiavi all'interno del dizionario students che hanno il corso specificato tra i valori 
#           oppure il messaggio di errore "Nessuno studente è iscritto al corso {course}." se non ci sono studenti che frequentano il corso specificato.
class Student:
    def __init__(self, student_id: str) -> None:
        self.student_id: str=student_id
        self.courses: list[str] = []
    def enroll(self, course: str) -> None:
        if course in self.courses:
            print(f"Lo studente è già iscritto al corso {course}.")
        else:
            self.courses.append(course)
    def get_courses(self) -> list[str]:
        return self.courses

class School:
    def __init__(self) -> None:
        self.students: dict[str, Student] = {}
    def create_student(self, student_id: str) -> None:
        if student_id in self.students:
            return f"Lo studente con ID {student_id} esiste già."
        else:
            self.students[student_id] = Student(student_id)
    def enroll_student(self, student_id: str, course: str) -> None:
        if student_id in self.students:
            self.students[student_id].enroll(course)
        else:
            print("Studente non trovato.")
    def get_student_courses(self, student_id: str) -> list[str]:
        if student_id in self.students:
            return self.students[student_id].get_courses()
        else:
            return "Studente non trovato."
    def get_student_list(self) -> list[str]:
        return list(self.students.keys())
    def search_by_course(self, course: str) -> list[str]:
        student_ids = [student_id for student_id, student in self.students.items() if course in student.courses]
        if not student_ids:
            return f"Nessuno studente è iscritto al corso {course}."
        else:
            return student_ids