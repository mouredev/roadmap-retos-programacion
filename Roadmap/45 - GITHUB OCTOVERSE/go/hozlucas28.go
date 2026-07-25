package main

import (
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"net/http"
	"os"
	"os/exec"
)

/* -------------------------------------------------------------------------- */
/*                                   STRUCTS                                  */
/* -------------------------------------------------------------------------- */

/* -------------------------------- Adapters -------------------------------- */

type Adapter struct{}

func (_ *Adapter) UserData(userData *User) *UserData {
	var forks uint = 0
	for _, publicRepo := range userData.PublicRepositoriesData {
		if publicRepo.Fork {
			forks++
		}
	}

	return &UserData{
		Followers:          userData.Followers,
		Following:          userData.Following,
		Forks:              forks,
		Name:               userData.Name,
		PublicRepositories: userData.PublicRepositories,
		Stars:              uint(len(userData.Stars)),
		UserName:           userData.Login,
	}

}

/* ------------------------------- GitHub API ------------------------------- */

type PublicRepositories struct {
	Fork bool `json:"fork"`
}

type Stars struct {
	Url string `json:"url"`
}

type User struct {
	Followers              uint                 `json:"followers"`
	Following              uint                 `json:"following"`
	Login                  string               `json:"login"`
	Name                   string               `json:"name"`
	PublicRepositories     uint                 `json:"public_repos"`
	ReposUrl               string               `json:"repos_url"`
	PublicRepositoriesData []PublicRepositories `json:"public_repos_data"`
	Stars                  []Stars              `json:"stars"`
}

type GitHubAPI struct {
	User User
}

/* ------------------------------ GitHubService ----------------------------- */

type UserData struct {
	Followers          uint   `json:"followers"`
	Following          uint   `json:"following"`
	Forks              uint   `json:"forks"`
	Name               string `json:"name"`
	PublicRepositories uint   `json:"public_repositories"`
	Stars              uint   `json:"stars"`
	UserName           string `json:"userName"`
}

type GitHubService interface {
	GetUserData(userName string) (*UserData, error)
}

type githubService struct {
	accessToken string
	_           struct{}
}

func NewGitHubService(accessToken string) GitHubService {
	var githubService githubService = githubService{accessToken: accessToken}
	return &githubService
}

func (githubService *githubService) GetUserData(userName string) (*UserData, error) {
	var userData User
	var adapter Adapter

	var err error
	var errMsg string

	var client *http.Client = &http.Client{}
	var request *http.Request

	var headers map[string][]string = map[string][]string{
		"Authorization":        {fmt.Sprintf("Bearer %s", githubService.accessToken)},
		"Accept":               {"application/vnd.github+json"},
		"X-GitHub-Api-Version": {"2022-11-28"},
	}

	var response *http.Response
	var starsData []Stars
	var publicReposData []PublicRepositories

	request, err = http.NewRequest("GET", fmt.Sprintf("https://api.github.com/users/%s", userName), nil)
	if err != nil {
		return &UserData{}, err
	}

	request.Header = headers

	response, err = client.Do(request)
	if err != nil {
		return &UserData{}, err
	}

	if response.StatusCode == http.StatusOK {
		body, err := io.ReadAll(response.Body)
		if err != nil {
			return &UserData{}, err
		}

		err = json.Unmarshal(body, &userData)
		if err != nil {
			return &UserData{}, err
		}

	} else {
		errMsg = fmt.Sprintf("%s: %v", request.Response.Status, request.Response.Body)
		return &UserData{}, errors.New(errMsg)
	}

	request, err = http.NewRequest("GET", fmt.Sprintf("https://api.github.com/users/%s/starred", userName), nil)
	if err != nil {
		return &UserData{}, err
	}

	request.Header = headers

	response, err = client.Do(request)
	if err != nil {
		return &UserData{}, err
	}

	if response.StatusCode == http.StatusOK {
		body, err := io.ReadAll(response.Body)
		if err != nil {
			return &UserData{}, err
		}

		err = json.Unmarshal(body, &starsData)
		if err != nil {
			return &UserData{}, err
		}

		userData.Stars = starsData
	} else {
		errMsg = fmt.Sprintf("%s: %v", request.Response.Status, request.Response.Body)
		return &UserData{}, errors.New(errMsg)
	}

	request, err = http.NewRequest("GET", userData.ReposUrl, nil)
	if err != nil {
		return &UserData{}, err
	}

	request.Header = headers

	response, err = client.Do(request)
	if err != nil {
		return &UserData{}, err
	}

	if response.StatusCode == http.StatusOK {
		body, err := io.ReadAll(response.Body)
		if err != nil {
			return &UserData{}, err
		}

		err = json.Unmarshal(body, &publicReposData)
		if err != nil {
			return &UserData{}, err
		}

		userData.PublicRepositoriesData = publicReposData
	} else {
		errMsg = fmt.Sprintf("%s: %v", request.Response.Status, request.Response.Body)
		return &UserData{}, errors.New(errMsg)
	}

	return adapter.UserData(&userData), err
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	const accessToken string = "XXX" // Complete with your personal GitHub Access Token.
	var githubService GitHubService = NewGitHubService(accessToken)

	var userInput string

	var userData *UserData
	var err error

	var cmd *exec.Cmd

	var i int
	var padding int

	fmt.Print("> Enter a GitHub username (-1 to exit): ")
	fmt.Scanf("%s\n", &userInput)

	for userInput != "-1" {
		userData, err = githubService.GetUserData(userInput)

		if err == nil {
			cmd = exec.Command("clear")
			cmd.Stdout = os.Stdout
			cmd.Run()

			fmt.Print("+ ")
			for i = 0; i < 52; i++ {
				fmt.Print("-")
			}
			fmt.Print(" +\n")

			padding = len(userData.UserName) - 52
			fmt.Printf("+ %-*s%s%*s +\n", padding/2, "", userData.UserName, padding/2+padding%2, "")

			fmt.Print("+ ")
			for i = 0; i < 52; i++ {
				fmt.Print("-")
			}
			fmt.Print(" +\n")

			fmt.Printf("+ %-52s +\n", fmt.Sprintf("%s: %s.", "Name", userData.Name))
			fmt.Printf("+ %-52s +\n", fmt.Sprintf("%s: %d.", "Public repositories", userData.PublicRepositories))
			fmt.Printf("+ %-52s +\n", fmt.Sprintf("%s: %d.", "Repositories stared", userData.Stars))
			fmt.Printf("+ %-52s +\n", fmt.Sprintf("%s: %d.", "Number of repositories forked", userData.Forks))
			fmt.Printf("+ %-52s +\n", fmt.Sprintf("%s: %d.", "Following", userData.Following))
			fmt.Printf("+ %-52s +\n", fmt.Sprintf("%s: %d.", "Followers", userData.Followers))

			fmt.Print("+ ")
			for i = 0; i < 52; i++ {
				fmt.Print("-")
			}
			fmt.Print(" +\n")
		} else {
			fmt.Println("\n> An error occurred on fetch '{user_input}' username! Try again...")
		}

		fmt.Print("\n> Enter a GitHub username (-1 to exit): ")
		fmt.Scanf("%s\n", &userInput)
	}
}
