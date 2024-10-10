// Autor: Héctor Adán 
// GitHub: https://github.com/hectorio23

#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <stdexcept>
#include <algorithm>

using namespace std;

class Person {
public:
    int id;
    string name;
    Person* partner;
    vector<Person*> children;

    Person(int id, string name) : id(id), name(name), partner(nullptr) {}

    void setPartner(Person* p) {
        if (partner == nullptr) {
            partner = p;
            p->partner = this;  // Ensure both partners are connected
        } else {
            throw runtime_error(name + " already has a partner.");
        }
    }

    void addChild(Person* child) {
        if (child->parents().size() < 2) {
            children.push_back(child);
        } else {
            throw runtime_error(child->name + " already has two parents.");
        }
    }

    vector<Person*> parents() {
        // Find parents by searching who has this person as a child
        vector<Person*> parents;
        for (Person* p : allPersons) {
            if (find(p->children.begin(), p->children.end(), this) != p->children.end()) {
                parents.push_back(p);
            }
        }
        return parents;
    }

    static void displayTree(Person* p, int level = 0) {
        if (p->partner) {
            cout << string(level * 2, ' ') << p->partner->name << endl;
        }
        cout << string(level * 2, ' ') << p->name << endl;
        for (Person* child : p->children) {
            displayTree(child, level + 1);
        }
    }

    static vector<Person*> allPersons;
};

vector<Person*> Person::allPersons;

// Sample usage
int main() {
    Person* alice = new Person(1, "Andrea");
    Person::allPersons.push_back(alice);
    Person* bob = new Person(2, "Adán");
    Person::allPersons.push_back(bob);
    alice->setPartner(bob);
    Person* alejandro = new Person(3, "Alejandro");
    Person::allPersons.push_back(alejandro);
    alice->addChild(alejandro);
    Person::displayTree(alice);
         
    return EXIT_SUCCESS;
}
