from random import sample
class Participant:
    def __init__(self,name:str,country:str):
        self.name = name.lower()
        self.country = country.lower()
    def getName(self):
        return self.name
    def getCountry(self):
        return self.country    
class Event:
    def __init__(self,name:str):
        self.name = name.lower()
        self.participants = []
        self.winners = []
        
    def getName(self):
        return self.name
    def getParticipants(self):
        return self.participants    
    def addParticipant(self,participant:Participant):
        self.participants.append(participant)
    def simulateWinners(self):
        if len(self.participants) < 3:
            print("We need at least 3 participant")    
        else:
            #Get 3 random participants, Gold, silver and bronze
            self.winners = sample(self.participants,k=3)
    def getWinners(self):
        return self.winners        
    def printWinners(self):
        if len(self.winners) > 0:
            print(f'Gold medal: {self.winners[0].getName()} nationality: {self.winners[0].getCountry()}')
            print(f'Silver medal: {self.winners[1].getName()} nationality: {self.winners[1].getCountry()}')
            print(f'Bronze medal: {self.winners[2].getName()} nationality: {self.winners[2].getCountry()}')
        else:
            print("Event not simulated yet")


class JJOO: 
    def __init__(self):
        self.competitions = []
    def addCompetition(self,competition:Event):
        self.competitions.append(competition)
    def getCompetitionByName(self,name)->Event:
        found = False
        for element in self.competitions:
            if element.getName() == name:
                found = True
                return element
        if not(found):
            return None
    def getStats(self):
        countryMedals = {}

        for competition in self.competitions:
            winners = competition.getWinners()
            for winner in winners:
                if countryMedals.__contains__(winner.getCountry()):
                    countryMedals[winner.getCountry()] += 1
                else:
                    countryMedals[winner.getCountry()]  =  1    
        return countryMedals 
paris = JJOO()

while(True):
    print(" Press 1 to add an event")
    print(" Press 2 to add participant to event")
    print(" Press 3 to simulate an event")
    print(" Press 4 to create reports")
    print(" Press 5 to exit the program")

    option = int(input())

    if option == 1:
        print("Enter event game")
        name = str(input())
        if not(paris.getCompetitionByName(name)):
            event = Event(name)
            paris.addCompetition(event)
        else: 
            print("Event already exist")    
    elif option == 2:
        print("Enter event name to add participant ")
        name = str(input())
        event = paris.getCompetitionByName(name)
        if event:
            print("Enter participant name ")
            participant_name = str(input())
            print("Enter participant country ")
            particpant_nationality = str(input())
            participant = Participant(participant_name,particpant_nationality)
            event.addParticipant(participant)
        else:
            print("Event doesn't exist")
    elif option == 3:
        print("Enter event name to simulate ")
        name = str(input())
        event = paris.getCompetitionByName(name)
        if event:
            event.simulateWinners()
            winners = event.printWinners()

        else:
            print("Event doesn' exist")
    elif option == 4:
        print(paris.getStats())
    elif option == 5: 
        break