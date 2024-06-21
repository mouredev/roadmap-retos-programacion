import logging

FORMAT = '%(asctime)s %(message)s'
logger = logging.getLogger(__name__)
logging.basicConfig(format=FORMAT,level=logging.INFO)

logger.info("Info %s","message")
logger.debug("Debug %s","message")
logger.warning("Warning %s","message")
logger.error("Error %s","message")
logger.critical("Critical %s", "message")
logger.exception("Exception %s","message")

#Extra

class Task:
    def __init__(self):
        self.tasks = []
    def add_task(self,name,description):
        logger.info("%s","Starting adding task")
        object ={
            'name':name,
            'description':description
        }
        self.tasks.append(object) 
        logger.info("%s","Ending adding task")
    def remove_task(self,name):
        logger.info("%s","Starting removing task")
        for element in self.tasks:
            if element["name"]==name:
                self.tasks.remove(element)
        logger.info("%s","Ending removing task")    
    def list_tasks(self):
        logger.info("%s","Starting listing task")
        for element in self.tasks:
            print(f'Task {element["name"]} with description {element["description"]}')
        logger.info("%s","Ending listing task")



myTaskObj = Task()
myTaskObj.add_task("Program","Create a program")
myTaskObj.add_task("Sleep","Sleep for 8 hours")
myTaskObj.add_task("Game","Playing videogames")
myTaskObj.list_tasks()
myTaskObj.remove_task("Game")
myTaskObj.remove_task("Sleep")
myTaskObj.add_task("Game","Playing videogames")



