// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <fstream>
#include <memory>
#include <stdexcept>
#include <uuid/uuid.h>

// NOTE: COMPILE the program useing the following instruction:
// g++ -o run hectorio23.cpp -luuid


// Goal class represents a single goal with all necessary attributes.
class Goal {
private:
    std::string id;
    std::string description;
    int amount;
    int monthsLimit;
    std::string units;

    std::string generateUUID() {
        uuid_t uuid;
        char uuidStr[37];
        uuid_generate(uuid);
        uuid_unparse(uuid, uuidStr);
        return std::string(uuidStr);
    }

public:
    Goal(const std::string& desc, int amt, int months, const std::string& unit)
        : description(desc), amount(amt), monthsLimit(months), units(unit), id(generateUUID()) {
        if (monthsLimit < 1 || monthsLimit > 12) {
            throw std::out_of_range("Months limit must be between 1 and 12.");
        }
    }

    const std::string& getId() const { return id; }
    const std::string& getDescription() const { return description; }
    int getAmount() const { return amount; }
    int getMonthsLimit() const { return monthsLimit; }
    const std::string& getUnits() const { return units; }
};

// YearGoals manages a collection of goals and their monthly plans.
class YearGoals {
private:
    std::vector<std::shared_ptr<Goal>> goals;
    std::map<std::string, std::vector<std::pair<std::shared_ptr<Goal>, int>>> plan;

    const std::vector<std::string> months = {
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"};

    void initializePlan() {
        for (const auto& month : months) {
            plan[month] = {};
        }
    }

public:
    YearGoals() {
        initializePlan();
    }

    bool addGoal(const std::shared_ptr<Goal>& goal) {
        if (goals.size() >= 10) {
            std::cerr << "Maximum number of goals reached." << std::endl;
            return false;
        }

        goals.push_back(goal);
        distributeGoalAcrossMonths(goal);
        return true;
    }

    void distributeGoalAcrossMonths(const std::shared_ptr<Goal>& goal) {
        int remainingAmount = goal->getAmount();
        int monthsLimit = goal->getMonthsLimit();
        for (size_t i = 0; i < months.size() && remainingAmount > 0 && monthsLimit > 0; ++i, --monthsLimit) {
            int monthlyAmount = std::min(remainingAmount, 1);
            plan[months[i]].emplace_back(goal, monthlyAmount);
            remainingAmount -= monthlyAmount;
        }
    }

    void displayGoals() const {
        if (goals.empty()) {
            std::cout << "No goals added yet.\n";
            return;
        }

        for (const auto& goal : goals) {
            std::cout << "ID: " << goal->getId() << "\n"
                      << "Description: " << goal->getDescription() << "\n"
                      << "Amount: " << goal->getAmount() << "\n"
                      << "Units: " << goal->getUnits() << "\n"
                      << "Months Limit: " << goal->getMonthsLimit() << "\n\n";
        }
    }

    void displayPlan() const {
        for (const auto& month : months) {
            std::cout << month << ":\n";
            const auto& goalsForMonth = plan.at(month);
            for (size_t i = 0; i < goalsForMonth.size(); ++i) {
                const auto& [goal, amount] = goalsForMonth[i];
                std::cout << "  [ ] " << i + 1 << ". " << goal->getDescription()
                          << " (" << amount << " " << goal->getUnits() << "/month). Total: "
                          << goal->getAmount() << ".\n";
            }
            std::cout << "\n";
        }
    }

    void savePlanToFile(const std::string& filePath) const {
        std::ofstream file(filePath);
        if (!file.is_open()) {
            std::cerr << "Failed to open file: " << filePath << std::endl;
            return;
        }

        for (const auto& month : months) {
            file << month << ":\n";
            const auto& goalsForMonth = plan.at(month);
            for (size_t i = 0; i < goalsForMonth.size(); ++i) {
                const auto& [goal, amount] = goalsForMonth[i];
                file << "  [ ] " << i + 1 << ". " << goal->getDescription()
                     << " (" << amount << " " << goal->getUnits() << "/month). Total: "
                     << goal->getAmount() << ".\n";
            }
            file << "\n";
        }

        file.close();
        std::cout << "Plan saved to " << filePath << "\n";
    }
};

void displayMenu() {
    std::cout << "\nNew Year Goals Manager\n"
              << "========================\n"
              << "1. Add a Goal\n"
              << "2. View Goals\n"
              << "3. View Detailed Plan\n"
              << "4. Save Plan to File\n"
              << "0. Exit\n"
              << "Select an option: ";
}

int main() {
    YearGoals yearGoals;
    int option;

    do {
        displayMenu();
        std::cin >> option;
        std::cin.ignore();

        switch (option) {
        case 1: {
            std::string description, units;
            int amount, monthsLimit;

            std::cout << "Enter description: ";
            std::getline(std::cin, description);

            std::cout << "Enter amount: ";
            std::cin >> amount;

            std::cout << "Enter months limit (1-12): ";
            std::cin >> monthsLimit;
            while (monthsLimit < 1 || monthsLimit > 12) {
                std::cout << "Invalid input. Enter months limit (1-12): ";
                std::cin >> monthsLimit;
            }

            std::cout << "Enter units: ";
            std::cin.ignore();
            std::getline(std::cin, units);

            try {
                auto goal = std::make_shared<Goal>(description, amount, monthsLimit, units);
                if (yearGoals.addGoal(goal)) {
                    std::cout << "Goal added successfully.\n";
                } else {
                    std::cout << "Failed to add goal. Maximum limit reached.\n";
                }
            } catch (const std::exception& e) {
                std::cerr << e.what() << "\n";
            }

            break;
        }
        case 2:
            yearGoals.displayGoals();
            break;
        case 3:
            yearGoals.displayPlan();
            break;
        case 4: {
            std::string filePath;
            std::cout << "Enter file path to save plan: ";
            std::cin.ignore();
            std::getline(std::cin, filePath);
            yearGoals.savePlanToFile(filePath);
            break;
        }
        case 0:
            std::cout << "Exiting program. Goodbye!\n";
            break;
        default:
            std::cout << "Invalid option. Please try again.\n";
        }
    } while (option != 0);

    return 0;
}
