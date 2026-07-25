# 36- El sombrero selecionador
import random

questions = {}

for i in range(1, 11):
    questions[i] = ['a','b','c','d']

class SortingHat():

    def __init__(self, questions: dict):
        self.questions = questions

    def ask_questions(self) -> dict:
        frontend = 0
        backend = 0
        mobile = 0
        data = 0

        for quest in self.questions:
            print(f"Pregunta: {quest}")
            print(f"Opciones: ")
            for index, responses in enumerate(self.questions[quest]):
                print(f"{index+1}. {responses}")
            while True:
                response = input("Respuesta elegida: ")
                match response:
                    case '1':
                        frontend += 1
                        break
                    case '2':
                        backend += 1
                        break
                    case '3':
                        mobile += 1
                        break
                    case '4':
                        data += 1
                        break
                    case _:
                        print("Valor incorrecto, vuelve a intentar")
        return {
            'frontend': frontend,
            'backend' : backend,
            'mobile' :mobile,
            'data' : data
        }
    
    def election(self, results: dict, name):
        max_afinity = max([x for x in results.values()])
        afinity = {k: v for k, v in results.items() if v == max_afinity}
        if len(afinity) > 1:
            final_election = random.choice(list(afinity.keys()))
            print(
                f"""\nHmmmm... Ha sido una decisión muy complicada, {
                    name}.\n¡Pero finalmente tu casa será {final_election}!"""
                )
        else:
            final_election = list(afinity.keys())[0]
            print(f"\nEnhorabuena, {name}.\n¡Tu casa será {final_election}!")


print("\n¡Bienvenido a Hogwarts, la escuela de programación para magos y brujas del código!")
print("El sombrero seleccionador decidirá cuál es tu casa como programador.")

name = input("\n¿Cuál es tu nombre? ")

sortinghat = SortingHat(questions)

sortinghat.election(sortinghat.ask_questions(), name)