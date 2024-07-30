from abc import ABC,abstractmethod

#Incorrect example
class FrontEnd:
    def __init__(self,back_end):
        self.back_end = back_end
    def display_data(self):
        data = self.back_end.get_data_from_database()
        print(f'Data is: {data}')

class BackEnd:
    def get_data_from_database(self):
        return "Data from databse"
    def gat_data_from_api(self):
        return "Data from API"
'''
back = BackEnd()
front = FrontEnd(back)
front.display_data()
'''

#Correct example

class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass
class Database(DataSource):
    def get_data(self):
        return "Data from database"

class API(DataSource):
    def get_data(self):
        return "Data from API"

class FrontEndV2:
    def __init__(self,datasource) -> None:
        self.source = datasource
    def  display_data(self):
        data = self.source.get_data()
        print(f'Data extracted: {data}')                  

databsae_backend = Database()
front = FrontEndV2(databsae_backend) 
front.display_data()       
api_backend = API()
front = FrontEndV2(api_backend)
front.display_data()

#Extra

class Notification(ABC):
    @abstractmethod
    def send_notfication(self):
        pass

class EmailNotification(Notification):
    def send_notfication(self):
        print ("Email Notification")

class PushNotification(Notification):
    def send_notfication(self):
         print("Push Notification")

class SMSNotification(Notification):
    def send_notfication(self):
        print("SMS Notification")

class Service:
    def __init__(self,notification) -> None:
        self.notification = notification

    def send(self):
        self.notification.send_notfication()

service = Service(EmailNotification())
service.send()

service = Service(PushNotification())
service.send()

service = Service(SMSNotification())
service.send()