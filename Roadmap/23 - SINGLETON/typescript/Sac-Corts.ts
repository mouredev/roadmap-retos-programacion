class Singleton {
    private static instance: Singleton | null = null;
    private data: string;

    private constructor() {
        this.data = "Singleton instance data";
    }

    public static getInstance(): Singleton {
        if (!Singleton.instance) {
            Singleton.instance = new Singleton();
        }
        return Singleton.instance;
    }

    public getData(): string {
        return this.data;
    }
}

const instance1 = Singleton.getInstance();
console.log(instance1.getData());

const instance2 = Singleton.getInstance();
console.log(instance1 === instance2);


// ** Extra Exercise ** //

class UserSession {
    private static instance: UserSession | null = null;
    private user: { id: number; username: string; name: string; email: string } | null;

    private constructor() {
        this.user = null;
    }

    public static getInstance(): UserSession {
        if (!UserSession.instance) {
            UserSession.instance = new UserSession();
        }
        return UserSession.instance;
    }

    public setUser(id: number, username: string, name: string, email: string): void {
        this.user = { id, username, name, email };
    }

    public getUser(): { id: number; username: string; name: string; email: string } | string {
        if (!this.user) {
            return "There is no user in the session";
        }
        return this.user;
    }

    public clearSession(): void {
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
