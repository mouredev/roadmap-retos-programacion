# -- exercise
# incorrect
class HeroI:
    def __init__(self, name, primary_attribute, base_damage, health):
        self.name = name;
        self.primary_attribute = primary_attribute;
        self.base_damage = base_damage;
        self.health = health;

    def calculate_damage(self, additional_damage):
        return self.base_damage + additional_damage;

    def display_info(self):
        info = f"Hero: {self.name}\n";
        info += f"Primary Attribute: {self.primary_attribute}\n";
        info += f"Base Damage: {self.base_damage}\n";
        info += f"Health: {self.health}";
        return info;

hero = HeroI("Axe", "Strength", 50, 1000);
print(hero.display_info());
print(f"Damage: {hero.calculate_damage(20)}");

# correct
class HeroC:
    def __init__(self, name, primary_attribute, base_damage, health):
        self.name = name;
        self.primary_attribute = primary_attribute;
        self.base_damage = base_damage;
        self.health = health;

class DamageCalculator:
    def calculate_damage(self, hero, additional_damage):
        return hero.base_damage + additional_damage;

class HeroDisplay:
    def display_info(self, hero):
        info = f"Hero: {hero.name}\n"
        info += f"Primary Attribute: {hero.primary_attribute}\n";
        info += f"Base Damage: {hero.base_damage}\n";
        info += f"Health: {hero.health}";
        return info;

print("------------------------------------------------")
hero = HeroC("Axe", "Strength", 50, 1000);
damage_calculator = DamageCalculator();
hero_display = HeroDisplay();

print(hero_display.display_info(hero))
print(f"Damage: {damage_calculator.calculate_damage(hero, 20)}");

# -- extra challenge
# incorrect
class Library:
    def __init__(self):
        self.books = [];
        self.users = [];
        self.loans = [];

    def add_book(self, title, author, copies):
        book = {"title": title, "author": author, "copies": copies};
        self.books.append(book);

    def add_user(self, name, user_id, email):
        user = {"name": name, "user_id": user_id, "email": email};
        self.users.append(user);

    def loan_book(self, user_id, book_title):
        for book in self.books:
            if book["title"] == book_title and book["copies"] > 0:
                self.loans.append({"user_id": user_id, "book_title": book_title});
                book["copies"] -= 1;
                return True;
        return False;

    def return_book(self, user_id, book_title):
        for loan in self.loans:
            if loan["user_id"] == user_id and loan["book_title"] == book_title:
                self.loans.remove(loan);
                for book in self.books:
                    if book["title"] == book_title:
                        book["copies"] += 1;
                        return True;
        return False;

library = Library()
library.add_book("1996", "Ahmed Khedr", 4);
library.add_user("Legion Commander", 1, "legioncommander@gmail.com");
library.loan_book(1, "1996");
library.return_book(1, "1996");


# correct
class BookManager:
    def __init__(self):
        self.books = [];

    def add_book(self, title, author, copies):
        book = {"title": title, "author": author, "copies": copies};
        self.books.append(book);

    def update_copies(self, book_title, copies):
        for book in self.books:
            if book["title"] == book_title:
                book["copies"] += copies;
                return True;
        return False;

    def get_book(self, book_title):
        for book in self.books:
            if book["title"] == book_title:
                return book;
        return None;

class UserManager:
    def __init__(self):
        self.users = [];

    def add_user(self, name, user_id, email):
        user = {"name": name, "user_id": user_id, "email": email};
        self.users.append(user);

    def get_user(self, user_id):
        for user in self.users:
            if user["user_id"] == user_id:
                return user;
        return None;

class LoanManager:
    def __init__(self, book_manager):
        self.loans = [];
        self.book_manager = book_manager;

    def loan_book(self, user_id, book_title):
        book = self.book_manager.get_book(book_title);
        if book and book["copies"] > 0:
            self.loans.append({"user_id": user_id, "book_title": book_title});
            self.book_manager.update_copies(book_title, -1);
            return True;
        return False;

    def return_book(self, user_id, book_title):
        for loan in self.loans:
            if loan["user_id"] == user_id and loan["book_title"] == book_title:
                self.loans.remove(loan);
                self.book_manager.update_copies(book_title, 1);
                return True;
        return False;

# Uso correcto
book_manager = BookManager();
user_manager = UserManager();
loan_manager = LoanManager(book_manager);

book_manager.add_book("1996", "Ahmed Khedr", 4);
user_manager.add_user("Legion Commander", 1, "legioncommander@gmail.com");
loan_manager.loan_book(1, "1996");
loan_manager.return_book(1, "1996");

