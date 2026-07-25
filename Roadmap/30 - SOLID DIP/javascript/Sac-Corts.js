// Wrong way 
class UserService {
    constructor() {
        this.database = new MySQLDatabase();
    }

    getUser(id) {
        return this.database.findUserById(id);
    }
}

class MySQLDatabase {
    findUserById(id) {
        return { id, name: 'Isaac Cortés', db: 'MySQL' };
    }
}

const userService = new UserService();
console.log(userService.getUser(1));

// Correct way
class UserService2 {
    constructor(database) {
        this.database = database;
    }

    getUser(id) {
        return this.database.findUserById(id);
    }
}

class Database {
    findUserById(id) {
        throw new Error("Method not implemented");
    }
}

class MySQLDatabase2 extends Database {
    findUserById(id) {
        return { id, name: 'Isaac Cortés', db: 'MySQL' };
    }
}

class MongoDBDatabase extends Database {
    findUserById(id) {
        return { id, name: 'Isaac Cortés', db: 'MongoDB' };
    }
}

const mysqlService = new UserService2(new MySQLDatabase2());
console.log(mysqlService.getUser(1));

const mongoService = new UserService2(new MongoDBDatabase());
console.log(mongoService.getUser(2));

// Extra Exercise //
class NotificationService {
    sendNotification(message, recipient) {
        throw new Error('Method not implemented');
    }
}

class EmailNotification extends NotificationService {
    sendNotification(message, recipient) {
        console.log(`Sending email to ${recipient}: ${message}`);
    }
}

class PushNotification extends NotificationService {
    sendNotification(message, recipient) {
        console.log(`Sending push to ${recipient}: ${message}`);
    }
}

class SMSNotification extends NotificationService {
    sendNotification(message, recipient) {
        console.log(`Sending SMS to ${recipient}: ${message}`)
    }
}

class NotificationManager {
    constructor(notificationService) {
        this.notificationService = notificationService;
    }

    send(message, recipient) {
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