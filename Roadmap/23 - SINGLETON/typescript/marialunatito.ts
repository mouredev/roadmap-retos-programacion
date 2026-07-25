// Dominio
interface IUser {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
  birthday: Date;
}

// Entidad inmutable
class User implements IUser {
  readonly id: number;
  readonly first_name: string;
  readonly last_name: string;
  readonly email: string;
  readonly birthday: Date;

  constructor(props: IUser) {
    this.id = props.id;
    this.first_name = props.first_name;
    this.last_name = props.last_name;
    this.email = props.email;
    this.birthday = new Date(props.birthday); // defensivo
    Object.freeze(this); // inmutabilidad superficial
  }
}

// Singleton: único gestor de sesiones en el proceso
class SessionManager {
  private static instance?: SessionManager;
  private store = new Map<number, User>();

  private constructor() {}

  static getInstance(): SessionManager {
    if (!this.instance) this.instance = new SessionManager();
    return this.instance;
  }

  // Crea o retorna sesión existente para el user.id
  login(userData: IUser): User {
    const existing = this.store.get(userData.id);
    if (existing) return existing;

    const user = new User(userData);
    this.store.set(user.id, user);
    return user;
  }

  getById(userId: number): User | undefined {
    return this.store.get(userId);
  }

  // true si removió, false si no existía
  logout(userId: number): boolean {
    return this.store.delete(userId);
  }

  // lectura segura
  list(): ReadonlyArray<User> {
    return [...this.store.values()];
  }

  clear(): void {
    this.store.clear();
  }
}

// ================== DEMO ==================
const session = SessionManager.getInstance();

const user1: IUser = {
  id: 1,
  first_name: "Maria",
  last_name: "Luna",
  birthday: new Date("2020-01-02"),
  email: "maria@example.com",
};

const user2: IUser = {
  id: 2,
  first_name: "Carmen",
  last_name: "Luna",
  birthday: new Date("2022-04-10"),
  email: "carmen@example.com",
};

const s1 = session.login(user1);
const s2 = session.login(user2);
const s3 = session.login(user1);

console.log("s1 === s2 ?", s1 === s2); // false
console.log("s1 === s3 ?", s1 === s3); // true
console.log("list before logout:", session.list());

session.logout(2);
console.log("list after logout:", session.list());

// script for run
// npx ts-node "Roadmap/23 - SINGLETON/typescript/marialunatito.ts"
