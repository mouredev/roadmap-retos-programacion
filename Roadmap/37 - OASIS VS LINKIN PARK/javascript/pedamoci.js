import readline from "readline"

const colors = {
  red: "\x1b[31m",
  green: "\x1b[32m",
  yellow: "\x1b[33m",
  cyan: "\x1b[34m",
  reset: "\x1b[0m",
}

class Asks {
  constructor() {
    this.readline = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    })
  }

  #ask(question) {
    return new Promise(resolve => {
      this.readline.question(question, (answer) => resolve(answer))
    })
  }

  close() {
    this.readline.close()
  }

  async askLabel(label) {
    const response = await this.#ask(colors.cyan + `Enter the ${label}: ` + colors.reset)
    return response
  }
}

class Renderer {
  static error(message) {
    console.log(colors.red + "Error: " + message + colors.reset)
  }

  static success(message) {
    console.log(colors.green + "Success: " + message + colors.reset)
  }

  static info(info) {
    console.log(colors.yellow + info + colors.reset)
  }
}

const asks = new Asks()

class APISpotify {
  constructor() {
    this.token = 'undefined';
  }

  async fetchWebApi(endpoint, method) {
    const res = await fetch(`https://api.spotify.com/v1/${endpoint}`, {
      headers: {
        Authorization: `Bearer ${this.token}`,
      },
      method
    });
    return await res.json();
  }

  async searchArtist(name) {
    const res = await this.fetchWebApi(
      `search?q=${encodeURIComponent(name)}&type=artist&limit=10`, 
      "GET"
    );
    return res.artists.items;
  }

  async searchSongsArtist(id) {
    const res = await this.fetchWebApi(
      `artists/${id}/top-tracks?market=AR`, 
      "GET"
    );
    return res.tracks;
  }
}

class GetInfo {
  constructor(apiSpotify){
    this.apiSpotify = apiSpotify
  }

  async getArtist(name) {
    let artists = await this.apiSpotify.searchArtist(name)

    for (const artist of artists) {
      if (artist.name.toLowerCase() === name.toLowerCase()){
        return artist
      }
    }
    return artists[0]
  }

  async songMostPopular(id) {
    let songs = await this.apiSpotify.searchSongsArtist(id)

    const maxPopularity = Math.max(...songs.map(s => s.popularity))

    const song = songs.filter(s => s.popularity === maxPopularity)

    return song[0]
  }

  async artistData(name) {
    const artist = await this.getArtist(name)
    const popularity = artist.popularity
    const followers = artist.followers.total

    const song = await this.songMostPopular(artist.id)
    const songName = song.name
    const songPopularity = song.popularity

    const artistData = {name: artist.name, popularity: popularity, followers: followers, songName: songName, songPopularity: songPopularity}

    return artistData
  }
}

class Comparator {
  constructor() {
    this.winner = {}
    this.countArtistOne = 0
    this.countArtistTwo = 0
  }

  popularity(artistOne, artistTwo) {
    if (artistOne.popularity > artistTwo.popularity) {
      this.winner.popularity = {name: artistOne.name, popularity: artistOne.popularity}
      this.countArtistOne++
    }

    if (artistOne.popularity < artistTwo.popularity) {
      this.winner.popularity = {name: artistTwo.name, popularity: artistTwo.popularity}
      this.countArtistTwo++
    }
  }

  followers(artistOne, artistTwo){
    if (artistOne.followers > artistTwo.followers) {
      this.winner.followers = {name: artistOne.name, followers: artistOne.followers}
      this.countArtistOne++
    }

    if (artistOne.followers < artistTwo.followers) {
      this.winner.followers = {name: artistTwo.name, followers: artistTwo.followers}
      this.countArtistTwo++
    }
  }

  songPopularity(artistOne, artistTwo) {
    if (artistOne.songPopularity > artistTwo.songPopularity) {
      this.winner.song = {name: artistOne.name, songName: artistOne.songName, songPopularity: artistOne.songPopularity}
      this.countArtistOne++
    }

    if (artistOne.songPopularity < artistTwo.songPopularity) {
      this.winner.song = {name: artistTwo.name, songName: artistTwo.songName, songPopularity: artistTwo.songPopularity}
      this.countArtistTwo++
    }
  }

  artist(artistOne, artistTwo) {
    this.popularity(artistOne, artistTwo)
    this.followers(artistOne, artistTwo)
    this.songPopularity(artistOne, artistTwo)

    if (this.countArtistOne > this.countArtistTwo) this.winner.winnerName = artistOne.name
    if (this.countArtistOne < this.countArtistTwo) this.winner.winnerName = artistTwo.name

    return this.winner
  }
}

class CreatorTXT {
  constructor() {
    this.info = ""
  }

  txt(data) {
    if (!!data.winnerName) {
      this.info += `\nWINNER: ${data.winnerName}`
    } else {
      this.info += "\nDRAW"
    }

    if (!!data.popularity) {
      this.info += `\n${data.popularity.name} wins by popularity with ${data.popularity.popularity} points`
    } else {
      this.info += "\nThe two artists tied in popularity"
    }

    if (!!data.followers) {
      this.info += `\n${data.followers.name} wins by followers with ${data.followers.followers}`
    } else {
      this.info += "\nThe two artists tied in followers"
    }

    if (!!data.song) {
      this.info += `\nThe artist ${data.song.name} won with the song "${data.song.songName}", with a popularity rating of ${data.song.songPopularity}`
    } else {
      this.info += "\nThe two artists tied in popularity with their songs"
    }

    return this.info
  }
}

class Controller {
  constructor(creatorTXT, comparator, getInfo) {
    this.creatorTXT = creatorTXT
    this.comparator = comparator
    this.getInfo = getInfo
    this.artistOne
    this.artistTwo
  }

  async start() {
    const nameArtistOne = await asks.askLabel("artist's name")

    this.artistOne = await this.getInfo.artistData(nameArtistOne)

    while (true) {
      const nameArtistTwo = await asks.askLabel("second artist's name")
      if (nameArtistTwo !== nameArtistOne && nameArtistTwo !== this.artistOne.name){
        this.artistTwo = await this.getInfo.artistData(nameArtistTwo)
        break
      }

      Renderer.error("The artist's name must be different from the first one")
    }

    const winner = this.comparator.artist(this.artistOne, this.artistTwo)

    const info = this.creatorTXT.txt(winner)

    Renderer.info(info)

    asks.close()
  }
}

const controller = new Controller(new CreatorTXT(), new Comparator(), new GetInfo(new APISpotify))
controller.start()