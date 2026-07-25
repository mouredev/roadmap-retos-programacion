// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

// NOTES: You need to install the following dependencies
// - vcpkg install cpr
// - vcpkg install nlohmann-json

// For compiling the code:
// g++ -std=c++17 -Ipath_to_nlohmann_json -Ipath_to_cpr_include main.cpp -Lpath_to_cpr_library -lcpr -o github_report

#include <nlohmann/json.hpp>
#include <unordered_map>
#include <algorithm>
#include <cpr/cpr.h>
#include <iostream>
#include <string>
#include <vector>

using json = nlohmann::json;

class GitHubUserReport {
public:
    explicit GitHubUserReport(const std::string& username) : username(username), base_url("https://api.github.com") {}

    void generateReport() {
        try {
            auto user_info = fetchData("users/" + username);
            auto repos = fetchData("users/" + username + "/repos");

            // Metric 1: Most used language
            std::unordered_map<std::string, int> language_count;
            for (const auto& repo : repos) {
                if (!repo["language"].is_null()) {
                    std::string language = repo["language"];
                    language_count[language]++;
                }
            }
            std::string most_used_language = "Unknown";
            if (!language_count.empty()) {
                most_used_language = std::max_element(language_count.begin(), language_count.end(),
                                                      [](const auto& a, const auto& b) {
                                                          return a.second < b.second;
                                                      })->first;
            }

            // Metric 2: Total repositories
            int total_repos = repos.size();

            // Metric 3: Total stars
            int total_stars = 0;
            for (const auto& repo : repos) {
                total_stars += repo["stargazers_count"];
            }

            // Metric 4: Followers
            int followers = user_info["followers"];

            // Metric 5: Following
            int following = user_info["following"];

            // Print the report
            std::cout << "GitHub User Report for: " << username << "\n";
            std::cout << "------------------------------------\n";
            std::cout << "Most Used Language: " << most_used_language << "\n";
            std::cout << "Total Repositories: " << total_repos << "\n";
            std::cout << "Total Stars: " << total_stars << "\n";
            std::cout << "Followers: " << followers << "\n";
            std::cout << "Following: " << following << "\n";

        } catch (const std::exception& ex) {
            std::cerr << "Error: " << ex.what() << std::endl;
        }
    }

private:
    std::string username;
    std::string base_url;

    json fetchData(const std::string& endpoint) {
        auto response = cpr::Get(cpr::Url{base_url + "/" + endpoint},
                                 cpr::Header{{"User-Agent", "GitHub-User-Report"}});
        if (response.status_code != 200) {
            throw std::runtime_error("Failed to fetch data from " + endpoint + ": " + response.error.message);
        }
        return json::parse(response.text);
    }
};

int main() {
    std::string username;
    std::cout << "Enter the GitHub username: ";
    std::cin >> username;

    GitHubUserReport report(username);
    report.generateReport();

    return 0;
}
