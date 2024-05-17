import requests


def main():
    url = "https://isilanes.org"
    response = requests.get(url)
    assert response.status_code == 200
    print(response.text)


if __name__ == "__main__":
    main()
