# pylint: disable=missing-module-docstring,missing-function-docstring,broad-exception-raised

from typing import Any
import requests as request


# ---------------------------------------------------------------------------- #
#                                      ENV                                     #
# ---------------------------------------------------------------------------- #


SPOTIFY_API_CLIENT_ID: str = "******"
SPOTIFY_API_CLIENT_SECRET: str = "******"


# ---------------------------------------------------------------------------- #
#                                   FUNCTIONS                                  #
# ---------------------------------------------------------------------------- #


def get_artist_data(*, _id: str, token: str) -> dict[Any, Any]:
    url: str = f"https://api.spotify.com/v1/artists/{_id}"

    headers: dict[str, str] = {
        "Authorization": f"Bearer {token}",
    }

    response: request.Response = request.get(url=url, headers=headers, timeout=10)
    data: dict[Any, Any] = response.json()

    if response.status_code != 200:
        raise Exception(data)

    return data


def search_artist(
    *,
    fullName: str,
    token: str,
) -> dict[Any, Any]:
    url: str = f"https://api.spotify.com/v1/search?q={fullName}&type=artist&limit=1"

    headers: dict[str, str] = {
        "Authorization": f"Bearer {token}",
    }

    response: request.Response = request.get(url=url, headers=headers, timeout=10)
    data: dict[Any, Any] = response.json()

    if response.status_code != 200:
        raise Exception(data)

    return data["artists"]["items"][0]


def get_artist(
    *,
    _id: str,
    token: str,
) -> dict[Any, Any]:
    url: str = f"https://api.spotify.com/v1/artists/{_id}"

    headers: dict[str, str] = {
        "Authorization": f"Bearer {token}",
    }

    response: request.Response = request.get(url=url, headers=headers, timeout=10)
    data: dict[Any, Any] = response.json()

    if response.status_code != 200:
        raise Exception(data)

    return data


def get_artist_top_tracks(
    *,
    _id: str,
    token: str,
) -> dict[Any, Any]:
    url: str = f"https://api.spotify.com/v1/artists/{_id}/top-tracks"

    headers: dict[str, str] = {
        "Authorization": f"Bearer {token}",
    }

    response: request.Response = request.get(url=url, headers=headers, timeout=10)
    data: dict[Any, Any] = response.json()

    if response.status_code != 200:
        raise Exception(data)

    return data


def get_spotify_token() -> dict[Any, Any]:
    url: str = "https://accounts.spotify.com/api/token"

    headers: dict[str, str] = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data: str = (
        f"grant_type=client_credentials"
        f"&client_id={SPOTIFY_API_CLIENT_ID}"
        f"&client_secret={SPOTIFY_API_CLIENT_SECRET}"
    )

    response: request.Response = request.post(
        url=url, headers=headers, data=data, timeout=10
    )

    if response.status_code != 200:
        raise Exception(response.json())

    return response.json()


# ---------------------------------------------------------------------------- #
#                                     MAIN                                     #
# ---------------------------------------------------------------------------- #


spotify_token: dict[Any, Any] = get_spotify_token()

band_names: dict[Any, Any] = {
    "first": "oasis",
    "second": "linkin park",
}

first_band: dict[Any, Any] = search_artist(
    fullName=band_names["first"],
    token=spotify_token["access_token"],
)

first_band_data: dict[Any, Any] = get_artist_data(
    _id=first_band["id"],
    token=spotify_token["access_token"],
)

first_band_top_tracks: dict[Any, Any] = get_artist_top_tracks(
    _id=first_band["id"],
    token=spotify_token["access_token"],
)

first_band_top_track: dict[Any, Any] = max(
    first_band_top_tracks["tracks"], key=lambda track: track["popularity"]
)

second_band: dict[Any, Any] = search_artist(
    fullName=band_names["second"],
    token=spotify_token["access_token"],
)

second_band_data: dict[Any, Any] = get_artist_data(
    _id=second_band["id"],
    token=spotify_token["access_token"],
)

second_band_top_tracks: dict[Any, Any] = get_artist_top_tracks(
    _id=second_band["id"],
    token=spotify_token["access_token"],
)

second_band_top_track: dict[Any, Any] = max(
    second_band_top_tracks["tracks"], key=lambda track: track["popularity"]
)

points_per_band: dict[str, int] = {
    "first": 0,
    "second": 0,
}

print(
    f"> Which band is more popular ({first_band_data['name']}, or {second_band_data['name']})?"
)

print("\n> Comparison of popularity...")
print(
    f"\n> Popularity of {first_band_data['name']}: {first_band_data['popularity']} "
    f"points of popularity."
)
print(
    f"> Popularity of {second_band_data['name']}: {second_band_data['popularity']} "
    f"points of popularity."
)

if first_band_data["popularity"] > second_band_data["popularity"]:
    print(
        f"> {first_band_data['name']} has more popularity points than {second_band_data['name']}."
    )
    points_per_band["first"] += 1
elif first_band_data["popularity"] < second_band_data["popularity"]:
    print(
        f"> {second_band_data['name']} has more popularity points than {first_band_data['name']}."
    )
    points_per_band["second"] += 1
else:
    print(
        f"> {first_band_data['name']} has the same popularity points than "
        f"{second_band_data['name']}."
    )


print("\n> Comparison of followers...")
print(
    f"\n> Followers of {first_band_data['name']}: {first_band_data['followers']['total']} "
    f"followers."
)
print(
    f"> Followers of {second_band_data['name']}: {second_band_data['followers']['total']} "
    f"followers."
)

if first_band_data["followers"]["total"] > second_band_data["followers"]["total"]:
    print(
        f"> {first_band_data['name']} has more followers than {second_band_data['name']}."
    )
    points_per_band["first"] += 1
elif first_band_data["followers"]["total"] < second_band_data["followers"]["total"]:
    print(
        f"> {second_band_data['name']} has more followers than {first_band_data['name']}."
    )
    points_per_band["second"] += 1
else:
    print(
        f"> {first_band_data['name']} has the same number of followers than "
        f"{second_band_data['name']}."
    )


print("\n> Comparison of top track of each band...")
print(
    f"\n> Top track of {first_band_data['name']} (name, and popularity): "
    f"{first_band_top_track['name']} "
    f"(${first_band_top_track['popularity']} points of popularity)."
)
print(
    f"> Top track of {second_band_data['name']} (name, and popularity): "
    f"{second_band_top_track['name']} (${second_band_top_track['popularity']} "
    f"points of popularity)."
)

if first_band_top_track["popularity"] > second_band_top_track["popularity"]:
    print(
        f"> {first_band_top_track['name']} of {first_band_data['name']} band is more popular "
        f"than {second_band_top_track['name']} of {second_band_data['name']} band."
    )
    points_per_band["first"] += 1
elif first_band_top_track["popularity"] < second_band_top_track["popularity"]:
    print(
        f"> {second_band_top_track['name']} of {second_band_data['name']} band is more "
        f"popular than {first_band_top_track['name']} of {first_band_data['name']} band."
    )
    points_per_band["second"] += 1
else:
    print(
        f"> {second_band_top_track['name']} of {second_band_data['name']} band has the same "
        f"popularity points than {first_band_top_track['name']} of {first_band_data['name']} band."
    )


print("\n> In conclusion...")

if points_per_band["first"] > points_per_band["second"]:
    print(
        f"\n> {first_band_data['name']} band is more popular than {second_band_data['name']} band"
    )
elif points_per_band["first"] < points_per_band["second"]:
    print(
        f"\n> {second_band_data['name']} band is more popular than {first_band_data['name']} band"
    )
else:
    print(
        f"\n> {first_band_data['name']} band is as popular as {second_band_data['name']} band."
    )
