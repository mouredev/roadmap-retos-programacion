class Singleton {
    constructor() {
        if (Singleton.instance) {
            return Singleton.instance;
        }
        this.data = "Singleton instance data";
        Singleton.instance = this;
        return this;
    }

    getData() {
        return this.data;
    }

    static getInstance() {
        if(!Singleton.instance) {
            Singleton.instance = new Singleton();
        }
        return Singleton.instance;
    }
}

const instance1 = Singleton.getInstance();
console.log(instance1.getData());

const instance2 = new Singleton();
console.log(instance1 === instance2);

// Extra Exercise //

class UserSession {
    constructor() {
        if (UserSession.instance) {
            return UserSession.instance;
        }
        this.user = null;
        UserSession.instance = this;
        return this;
    }

    static getInstance() {
        if (!UserSession.instance) {
            UserSession.instance = new UserSession();
        }
        return UserSession.instance;
    }

    setUser(id, username, name, email) {
        this.user = { id, username, name, email };
    }
    
    getUser() {
        if (!this.user) {
            return "There is no user in the session"
        }
        return this.user;
    }

    clearSession() {
        this.user = null;
    }
}

const session1 = UserSession.getInstance();
session1.setUser(1, "Sac", "Isaac", "isaac@gmail.com");
console.log(session1.getUser());

const session2 = UserSession.getInstance();
console.log(session1 === session2);

session2.clearSession();
console.log(session1.getUser());
