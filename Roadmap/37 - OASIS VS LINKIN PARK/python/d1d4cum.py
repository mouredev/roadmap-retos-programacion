import requests
from requests.adapters import Response


ACCESS_TOKEN = 'BQDskkWetddthiddwtbTTkJS_H5lg-LgNAxs82vlR1rP9tQVusdakSVPLY_DjisoPASLrXZrYhPc0eNR3GSTsU2-2XCXxmCPk03MvpFJQ1atgp9n3GY'
OASIS_ID = '2DaxqgrOhkeH0fpeiQq2f4'
LININ_PARK_ID = '6XyY86QOPPrYVGvF9ch6wz'
URL = 'https://api.spotify.com/v1/artists/'
HEADERS = {
    'Authorization': f"Bearer {ACCESS_TOKEN}"
}


def get_data(artist_id):

    response = requests.get(f"{URL}{artist_id}", headers=HEADERS)

    if response.status_code == 200:
        data = response.json()

        return data

    else:
        print(f"Error: {response.status_code}")

def main():
    oasis_data = get_data(OASIS_ID)
    linkin_park_data = get_data(LININ_PARK_ID)

    oasis_followers = oasis_data["followers"]["total"]
    linkin_park_followers = linkin_park_data["followers"]["total"]

    oasis_popularity = oasis_data["popularity"]
    linkin_park_popularity = linkin_park_data["popularity"]

    print("> Oasis")
    print(f"- Followers: {oasis_followers}")
    print(f"- Popularity: {oasis_popularity}")
    print("\n> Linkin Park")
    print(f"- Followers: {linkin_park_followers}")
    print(f"- Popularity: {linkin_park_popularity}")

    if oasis_popularity > linkin_park_popularity:
        print("\nOasis es más popular")
    elif oasis_popularity < linkin_park_popularity:
        print("\nLinkin Park es más popular")
    else:
        if oasis_followers > linkin_park_followers:
            print("\nOasis es más popular")
        elif oasis_followers < linkin_park_followers:
            print("\nLinkin Park es más popular")
        else:
            print("\nSon igual de populares")

if __name__ == '__main__':
    main()
