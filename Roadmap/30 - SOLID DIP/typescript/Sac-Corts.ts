// Wrong way
class UserService {
    private database: MySQLDatabase;

    constructor() {
        this.database = new MySQLDatabase();
    }

    getUser(id: number) {
        return this.database.findUserById(id);
    }
}

class MySQLDatabase {
    findUserById(id: number) {
        return { id, name: 'Isaac Cortés', db: 'MySQL' };
    }
}

const userService = new UserService();
console.log(userService.getUser(1));

// Correct way
class UserService2 {
    private database: Database;

    constructor(database: Database) {
        this.database = database;
    }

    getUser(id: number) {
        return this.database.findUserById(id);
    }
}

abstract class Database {
    abstract findUserById(id: number): { id: number; name: string; db: string };
}

class MySQLDatabase2 extends Database {
    findUserById(id: number) {
        return { id, name: 'Isaac Cortés', db: 'MySQL' };
    }
}

class MongoDBDatabase extends Database {
    findUserById(id: number) {
        return { id, name: 'Isaac Cortés', db: 'MongoDB' };
    }
}

const mysqlService = new UserService2(new MySQLDatabase2());
console.log(mysqlService.getUser(1));

const mongoService = new UserService2(new MongoDBDatabase());
console.log(mongoService.getUser(2));

// ** Extra Exercise ** //
abstract class NotificationService {
    abstract sendNotification(message: string, recipient: string): void;
}

class EmailNotification extends NotificationService {
    sendNotification(message: string, recipient: string): void {
        console.log(`Sending email to ${recipient}: ${message}`);
    }
}

class PushNotification extends NotificationService {
    sendNotification(message: string, recipient: string): void {
        console.log(`Sending push to ${recipient}: ${message}`);
    }
}

class SMSNotification extends NotificationService {
    sendNotification(message: string, recipient: string): void {
        console.log(`Sending SMS to ${recipient}: ${message}`);
    }
}

class NotificationManager {
    private notificationService: NotificationService;

    constructor(notificationService: NotificationService) {
        this.notificationService = notificationService;
    }

    send(message: string, recipient: string): void {
        this.notificationService.sendNotification(message, recipient);
    }
}

const emailService = new EmailNotification();
const pushService = new PushNotification();
const smsService = new SMSNotification();

const emailManager = new NotificationManager(emailService);
const pushManager = new NotificationManager(pushService);
const smsManager = new NotificationManager(smsService);

emailManager.send('Hello, Isaac!', 'isaac@gmail.com');
pushManager.send('Hello, Isaac!', 'sac');
smsManager.send('Hello, Isaac!', '8992584897');
