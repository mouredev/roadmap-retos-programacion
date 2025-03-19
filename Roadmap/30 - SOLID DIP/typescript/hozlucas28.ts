/*
    Dependency Inversion Principle (DIP)...
*/

console.log('Dependency Inversion Principle (DIP)...')

console.log('\nBad implementation of Dependency Inversion Principle (DIP)...')

interface IUserRepository {
    getUsers: () => string[]
}

class UserRepository implements IUserRepository {
    public getUsers(): string[] {
        return ['User N°1', 'User N°2', 'User N°3']
    }
}

interface IBadUserService {
    getUsers: () => string[]
}

class BadUserService implements IUserRepository {
    private userRepository: UserRepository

    public constructor() {
        this.userRepository = new UserRepository()
    }

    public getUsers(): string[] {
        return this.userRepository.getUsers()
    }
}

console.log(`\n\`\`\`\ninterface IUserRepository {
    getUsers: () => string[]
}

class UserRepository implements IUserRepository {
    public getUsers(): string[] {
        return ['User N°1', 'User N°2', 'User N°3']
    }
}

interface IBadUserService {
    getUsers: () => string[]
}

class BadUserService implements IUserRepository {
    private userRepository: UserRepository

    public constructor() {
        this.userRepository = new UserRepository()
    }

    public getUsers(): string[] {
        return this.userRepository.getUsers()
    }
}\n\`\`\``)

console.log(
    '\nThis is a bad implementation of Dependency Inversion Principle (DIP),\n' +
        '"BadUserService" class depends directly on the "UserRepository" class \n' +
        'rather than on an abstract class or an interface. So, if the "userRepository"\n' +
        'attribute in the "BadUserService" class needs to be changed, the constructor must\n' +
        'also be modified.'
)

console.log('\nGood implementation of Dependency Inversion Principle (DIP)...')

class UserLocalRepository implements IUserRepository {
    public getUsers(): string[] {
        return ['Local user N°1', 'Local user N°2', 'Local user N°3']
    }
}

class UserRemoteRepository implements IUserRepository {
    public getUsers(): string[] {
        return ['Remote user N°1', 'Remote user N°2', 'Remote user N°3']
    }
}

interface IGoodUserService {
    getUsers: () => string[]
}

class GoodUserService implements IGoodUserService {
    private userRepository: IUserRepository

    public constructor(userRepository: IUserRepository) {
        this.userRepository = userRepository
    }

    public getUsers(): string[] {
        return this.userRepository.getUsers()
    }
}

console.log(`\n\`\`\`\ninterface IUserRepository {
    getUsers: () => string[]
}

class UserLocalRepository implements IUserRepository {
    public getUsers(): string[] {
        return ['Local user N°1', 'Local user N°2', 'Local user N°3']
    }
}

class UserRemoteRepository implements IUserRepository {
    public getUsers(): string[] {
        return ['Remote user N°1', 'Remote user N°2', 'Remote user N°3']
    }
}

interface IGoodUserService {
    getUsers: () => string[]
}

class GoodUserService implements IGoodUserService {
    private userRepository: IUserRepository

    public constructor(userRepository: IUserRepository) {
        this.userRepository = userRepository
    }

    public getUsers(): string[] {
        return this.userRepository.getUsers()
    }
}\n\`\`\``)

console.log(
    '\nThis is a good implementation of Dependency Inversion Principle (DIP),\n' +
        'because "GoodUserService" class depends solely on injected dependencies\n' +
        'that implement the "IUserRepository" interface. So, if the "userRepository"\n' +
        'attribute in the "GoodUserService" class needs to be changed, the constructor\n' +
        'does not require modification (only the class call needs to be updated). For example,\n' +
        'I could inject inside the "userRepository" attribute an instance of "UserLocalRepository"\n' +
        'or "UserRemoteRepository" classes.'
)

console.log(
    '\n# ---------------------------------------------------------------------------------- #\n'
)

/*
    Additional challenge...
*/

console.log('Additional challenge...')

interface INotificationService {
    send: () => void
}

class EmailService implements INotificationService {
    public constructor() {}

    public send(): void {
        console.log('Email sent!')
    }
}

class PushService implements INotificationService {
    public constructor() {}

    public send(): void {
        console.log('Push sent!')
    }
}

class SMSService implements INotificationService {
    public constructor() {}

    public send(): void {
        console.log('SMS sent!')
    }
}

interface INotificationSystem {
    sendNotification: () => void
}

class NotificationSystem implements INotificationSystem {
    private notificationService: INotificationService

    public constructor(notificationService: INotificationService) {
        this.notificationService = notificationService
    }

    public sendNotification(): void {
        this.notificationService.send()
    }
}

const emailService: EmailService = new EmailService()
const pushService: PushService = new PushService()
const smsService: SMSService = new SMSService()

const emailNotificationSystem: NotificationSystem = new NotificationSystem(
    emailService
)

const pushNotificationSystem: NotificationSystem = new NotificationSystem(
    pushService
)

const smsNotificationSystem: NotificationSystem = new NotificationSystem(
    smsService
)

console.log()
emailNotificationSystem.sendNotification()

console.log()
pushNotificationSystem.sendNotification()

console.log()
smsNotificationSystem.sendNotification()
