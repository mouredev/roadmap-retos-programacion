const rubiusCupParticipants = ['abby_', 'Ache', 'AdriContreras4', 'agustin51', 'Alexby11', 'Ampeterby7', 'tvandeR', 'AriGameplays', 'Arigeli_', 'auronplay', 'aXoZer', 'BENIJU03', 'bycalitos', 'byViruZz', 'Carreraaa', 'Celopan', 'srcheeto', 'CrystalMolly', 'darioemehache', 'Dheylo', 'DjMaRiiO', 'Doble', 'ElvisaYomastercard', 'elyas360', 'FolagorLives', 'TheGrefg', 'GUANYAR', 'Hika', 'Hiperop', 'ibai', 'ibelky_', 'IlloJuan', 'imantado', 'Irina Isaia', 'Jesskiu', 'JOPA', 'JordiWild', 'kenaivsouza', 'MrKeroro10', 'TheKiddKeo95', 'KikoRivera', 'knekro', 'koko', 'KronnoZomberOficial', 'Leviathan', 'LITkillah', 'lolalolita', 'LOLITOFDEZ', 'Luh', 'Luzu', 'Mangel', 'Mayichi', 'melo', 'MissaSinfonia', 'Mixwell', 'JaggerPrincesa', 'NateGentile7', 'Nexxuz', 'LakshartNia', 'nilojeda', 'Nissaxter', 'OllieGamerz', 'orslok', 'Outconsumer', 'PapiGaviTV', 'paracetamor', 'patica1999', 'paulagonu', 'PauSenpaii', 'Perxitaa', 'NoSoyPlex',  'polispol1', 'Quackity', 'Recuerd0p', 'REVENANT', 'rivers_gg', 'robertpg', 'Roier', 'Rojuu', 'Rubius', 'Shadoune666', 'Silithur', 'spok_sponha', 'ElSpreen', 'Spursito', 'bysTaXx', 'Suzyroxx', 'Vicens', 'vituber', 'Werlyb', 'Xavi', 'xCry', 'elxokas', 'zZarcort', 'Zeling', 'ZormanWorld']

const colors = {
  red: "\x1b[31m",
  green: "\x1b[32m",
  yellow: "\x1b[33m",
  cyan: "\x1b[34m",
  reset: "\x1b[0m",
}

class Renderer {
  static error(message) {
    console.log(colors.red + "Error: " + message + colors.reset)
  }

  static success(message) {
    console.log(colors.green + "Success: " + message + colors.reset)
  }

  static table(info, columns) {
    console.table(info, columns)
  }
}

class APITwitch {
  constructor() {
    this.client_id = "undefined"
    this.client_secret = "undefined"
    this.access_token = "undefined"
  }

  async  getToken() {
    const res = await fetch("https://id.twitch.tv/oauth2/token", {
      method: "POST",
      body: new URLSearchParams({
        client_id: this.client_id,
        client_secret: this.client_secret,
        grant_type: "client_credentials"
      })
    })
  
    const data = await res.json();

    this.access_token = data.access_token 
  }

  async fetchWebApi(endpoint, method) {
    const res = await fetch(`https://api.twitch.tv/helix/${endpoint}`, {
      method,
      headers: {
        "Client-ID": this.client_id,
        "Authorization": `Bearer ${this.access_token}`
      }
    })

    return await res.json();
  }

  async searchStreamer(name) {
    const res = await this.fetchWebApi(
      `users?login=${encodeURIComponent(name)}`, 
      "GET"
    )

    return res.data
  }

  async searchFollowers(streamerID) {
    const res = await this.fetchWebApi(
      `channels/followers?broadcaster_id=${streamerID}`, 
      "GET"
    )

    return res.total
  }
}

class Order {
  constructor() {
    this.participantsOrderByFollowers = []
    this.participantsOrderBySeniority = []
  }

  byFollowers(participants) {
    let nonTwitch = participants.filter(participant => !participant.followers)

    this.participantsOrderByFollowers = participants.filter(participant => !!participant.followers)

    this.participantsOrderByFollowers.sort((a, b) => {
      return b.followers - a.followers
    })

    for (let i = 0; i < nonTwitch.length; i++) {
      nonTwitch[i].followers = "doesn't have a Twitch channel"
    }

    this.participantsOrderByFollowers = this.participantsOrderByFollowers.concat(nonTwitch)

    return this.participantsOrderByFollowers
  }

  bySeniority(participants) {
    let nonTwitch = participants.filter(participant => !participant.created_at)

    this.participantsOrderBySeniority = participants.filter(participant => !!participant.created_at)

    this.participantsOrderBySeniority.sort((a, b) => {
      const dateA = a.created_at.split('-')
      const yearA = parseInt(dateA[0])
      const monthA = parseInt(dateA[1])
      const dayA = parseInt(dateA[2])

      const dateB = b.created_at.split('-')
      const yearB = parseInt(dateB[0])
      const monthB = parseInt(dateB[1])
      const dayB = parseInt(dateB[2])

      return (yearA - yearB) ||
            (monthA - monthB) ||
            (dayA - dayB)
    })

    for (let i = 0; i < nonTwitch.length; i++) {
      nonTwitch[i].created_at = "doesn't have a Twitch channel"
    }

    this.participantsOrderBySeniority = this.participantsOrderBySeniority.concat(nonTwitch)

    return this.participantsOrderBySeniority
  }
}

class Controller {
  constructor(apiTwitch, order) {
    this.apiTwitch = apiTwitch
    this.order = order
    this.participants = []
  }

  async start(participants) {
    for (let i = 0; i < participants.length; i++) {
      const participantData = await this.apiTwitch.searchStreamer(participants[i])

      if (!participantData || participantData[0] === undefined) {
        this.participants.push({name: participants[i]})
      } else {
        const participantID = participantData[0].id
        const participantDate = participantData[0].created_at.split('T')[0]

        const followers = await this.apiTwitch.searchFollowers(participantID)

        this.participants.push({id: participantID, name: participants[i], created_at: participantDate, followers: followers})
      }

      Renderer.success(`The information from streamer no. ${i} was collected correctly`)
    }

    const participantsOrderByFollowers = this.order.byFollowers(this.participants)
    Renderer.table(participantsOrderByFollowers, ['name', 'followers'])

    const participantsOrderBySeniority = this.order.bySeniority(this.participants)
    Renderer.table(participantsOrderBySeniority, ['name', 'created_at'])
  }
}

const controller = new Controller(new APITwitch(), new Order())
controller.start(rubiusCupParticipants)