package main

import (
	"bytes"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"net/http"
	"net/url"
)

/* -------------------------------------------------------------------------- */
/*                                   STRUCTS                                  */
/* -------------------------------------------------------------------------- */

type Artist struct {
	ID   string `json:"id"`
	Name string `json:"name"`
	_    struct{}
}

type ArtistData struct {
	Followers  Followers `json:"followers"`
	Id         string    `json:"id"`
	Name       string    `json:"name"`
	Popularity int       `json:"popularity"`
	_          struct{}
}

type ArtistTopTracks struct {
	Tracks []Track `json:"tracks"`
}

type Followers struct {
	Total int `json:"total"`
	_     struct{}
}

type Search struct {
	Artists struct {
		Items []Artist `json:"Items"`
	} `json:"Artists"`
	_ struct{}
}

type Token struct {
	AccessToken string `json:"access_token"`
	TokenType   string `json:"token_type"`
	ExpiresIn   int    `json:"expires_in"`
	_           struct{}
}

type Track struct {
	Name       string `json:"name"`
	Popularity int    `json:"popularity"`
	_          struct{}
}

/* -------------------------------------------------------------------------- */
/*                                  FUNCTIONS                                 */
/* -------------------------------------------------------------------------- */

func SearchArtist(fullName string, accessToken string) (Artist, error) {
	var artist Artist

	queries := url.Values{
		"q":     {fullName},
		"type":  {"artist"},
		"limit": {"1"},
	}

	var endPoint string = "https://api.spotify.com/v1/search?" + queries.Encode()

	request, err := http.NewRequest("GET", endPoint, nil)
	if err != nil {
		return artist, err
	}

	request.Header = map[string][]string{
		"Authorization": {fmt.Sprintf("Bearer %s", accessToken)},
	}

	client := &http.Client{}
	response, err := client.Do(request)
	if err != nil {
		return artist, err
	}

	if response.StatusCode == http.StatusOK {
		body, err := io.ReadAll(response.Body)
		if err != nil {
			return artist, err
		}

		var search Search
		err = json.Unmarshal(body, &search)
		if err != nil {
			return artist, err
		}

		artist = search.Artists.Items[0]
	} else {
		var errMsg string = fmt.Sprintf("%s: %v", request.Response.Status, request.Response.Body)
		return artist, errors.New(errMsg)
	}

	return artist, nil
}

func GetArtistData(id string, accessToken string) (ArtistData, error) {
	var artistData ArtistData

	var url string = fmt.Sprintf("https://api.spotify.com/v1/artists/%s", id)

	request, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return artistData, err
	}

	request.Header = map[string][]string{
		"Authorization": {fmt.Sprintf("Bearer %s", accessToken)},
	}

	client := &http.Client{}
	response, err := client.Do(request)
	if err != nil {
		return artistData, err
	}

	if response.StatusCode == http.StatusOK {
		body, err := io.ReadAll(response.Body)
		if err != nil {
			return artistData, err
		}

		err = json.Unmarshal(body, &artistData)
		if err != nil {
			return artistData, err
		}
	} else {
		var errMsg string = fmt.Sprintf("%s: %v", request.Response.Status, request.Response.Body)
		return artistData, errors.New(errMsg)
	}

	return artistData, nil
}

func GetTopTrack(tracks []Track) Track {
	var topTrack Track = tracks[0]

	for _, track := range tracks[1:] {
		if track.Popularity > topTrack.Popularity {
			topTrack = track
		}
	}

	return topTrack
}

func GetArtistTopTracks(id string, accessToken string) (ArtistTopTracks, error) {
	var topTracks ArtistTopTracks

	var url string = fmt.Sprintf("https://api.spotify.com/v1/artists/%s/top-tracks", id)

	request, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return topTracks, err
	}

	request.Header = map[string][]string{
		"Authorization": {fmt.Sprintf("Bearer %s", accessToken)},
	}

	client := &http.Client{}
	response, err := client.Do(request)
	if err != nil {
		return topTracks, err
	}

	if response.StatusCode == http.StatusOK {
		body, err := io.ReadAll(response.Body)
		if err != nil {
			return topTracks, err
		}

		err = json.Unmarshal(body, &topTracks)
		if err != nil {
			return topTracks, err
		}
	} else {
		var errMsg string = fmt.Sprintf("%s: %v", request.Response.Status, request.Response.Body)
		return topTracks, errors.New(errMsg)
	}

	return topTracks, nil
}

func GetSpotifyToken() (Token, error) {
	var token Token

	var clientID string = "*****"
	var clientSecret string = "*****"

	var url string = "https://accounts.spotify.com/api/token"
	var contentType string = "application/x-www-form-urlencoded"
	var body string = fmt.Sprintf("grant_type=client_credentials&client_id=%s&client_secret=%s", clientID, clientSecret)

	response, err := http.Post(url, contentType, bytes.NewBufferString(body))
	if err != nil {
		return token, err
	}

	if response.StatusCode == http.StatusOK {
		body, err := io.ReadAll(response.Body)
		if err != nil {
			return token, err
		}

		err = json.Unmarshal(body, &token)
		if err != nil {
			return token, err
		}
	} else {
		var errMsg string = fmt.Sprintf("%s: %v", response.Status, response.Body)
		return token, errors.New(errMsg)
	}

	return token, nil
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	spotifyToken, err := GetSpotifyToken()
	if err != nil {
		panic(err)
	}

	var bandNames map[string]string = map[string]string{"first": "oasis", "second": "linkin park"}

	firstBand, err := SearchArtist(bandNames["first"], spotifyToken.AccessToken)
	if err != nil {
		panic(err)
	}

	firstBandData, err := GetArtistData(firstBand.ID, spotifyToken.AccessToken)
	if err != nil {
		panic(err)
	}

	firstBandTopTracks, err := GetArtistTopTracks(firstBand.ID, spotifyToken.AccessToken)
	if err != nil {
		panic(err)
	}

	var firstBandTopTrack Track = GetTopTrack(firstBandTopTracks.Tracks)

	secondBand, err := SearchArtist(bandNames["second"], spotifyToken.AccessToken)
	if err != nil {
		panic(err)
	}

	secondBandData, err := GetArtistData(secondBand.ID, spotifyToken.AccessToken)
	if err != nil {
		panic(err)
	}

	secondBandTopTracks, err := GetArtistTopTracks(secondBand.ID, spotifyToken.AccessToken)
	if err != nil {
		panic(err)
	}

	var secondBandTopTrack Track = GetTopTrack(secondBandTopTracks.Tracks)

	var pointsPerBand map[string]int = map[string]int{"first": 0, "second": 0}

	fmt.Printf("> Which band is more popular (%s, or %s)?\n", firstBandData.Name, secondBandData.Name)

	fmt.Println("\n> Comparison of popularity...")
	fmt.Printf("\n> Popularity of %s: %d points of popularity.\n", firstBandData.Name, firstBandData.Popularity)
	fmt.Printf("> Popularity of %s: %d points of popularity.\n", secondBandData.Name, secondBandData.Popularity)

	if firstBandData.Popularity > secondBandData.Popularity {
		fmt.Printf("> %s has more popularity points than %s.\n", firstBandData.Name, secondBandData.Name)
		pointsPerBand["first"]++
	} else if firstBandData.Popularity < secondBandData.Popularity {
		fmt.Printf("> %s has more popularity points than %s.\n", secondBandData.Name, firstBandData.Name)
		pointsPerBand["second"]++
	} else {
		fmt.Printf("> %s has the same popularity points than %s.\n", firstBandData.Name, secondBandData.Name)
	}

	fmt.Println("\n> Comparison of followers...")
	fmt.Printf("\n> Followers of %s: %d followers.\n", firstBandData.Name, firstBandData.Followers.Total)
	fmt.Printf("> Followers of %s: %d followers.\n", secondBandData.Name, secondBandData.Followers.Total)

	if firstBandData.Followers.Total > secondBandData.Followers.Total {
		fmt.Printf("> %s has more followers than %s.\n", firstBandData.Name, secondBandData.Name)
		pointsPerBand["first"]++
	} else if firstBandData.Followers.Total < secondBandData.Followers.Total {
		fmt.Printf("> %s has more followers than %s.\n", secondBandData.Name, firstBandData.Name)
		pointsPerBand["second"]++
	} else {
		fmt.Printf("> %s has the same number of followers than %s.\n", firstBandData.Name, secondBandData.Name)
	}

	fmt.Println("\n> Comparison of top track of each band...")
	fmt.Printf("\n> Top track of %s (name, and popularity): %s (%d points of popularity).\n", firstBandData.Name, firstBandTopTrack.Name, firstBandTopTrack.Popularity)
	fmt.Printf("> Top track of %s (name, and popularity): %s (%d points of popularity).\n", secondBandData.Name, secondBandTopTrack.Name, secondBandTopTrack.Popularity)

	if firstBandTopTrack.Popularity > secondBandTopTrack.Popularity {
		fmt.Printf(
			"> %s of %s band is more popular than %s of %s band.\n", firstBandTopTrack.Name, firstBandData.Name, secondBandTopTrack.Name, secondBandData.Name)
		pointsPerBand["first"]++
	} else if firstBandTopTrack.Popularity < secondBandTopTrack.Popularity {
		fmt.Printf(
			"> %s of %s band is more popular than %s of %s band.\n", secondBandTopTrack.Name, secondBandData.Name, firstBandTopTrack.Name, firstBandData.Name)
		pointsPerBand["second"]++
	} else {
		fmt.Printf(
			"> %s of %s band has the same popularity points than %s of %s band.\n", secondBandTopTrack.Name, secondBandData.Name, firstBandTopTrack.Name, firstBandData.Name)
	}

	fmt.Println("\n> In conclusion...")

	if pointsPerBand["first"] > pointsPerBand["second"] {
		fmt.Printf("\n> %s band is more popular than %s band.\n", firstBandData.Name, secondBandData.Name)
	} else if pointsPerBand["first"] < pointsPerBand["second"] {
		fmt.Printf("\n> %s band is more popular than %s band.\n", secondBandData.Name, firstBandData.Name)
	} else {
		fmt.Printf("\n> %s band is as popular as %s band.\n", firstBandData.Name, secondBandData.Name)
	}
}
