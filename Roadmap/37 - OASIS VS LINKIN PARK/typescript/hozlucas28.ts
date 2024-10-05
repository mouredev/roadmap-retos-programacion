/* -------------------------------------------------------------------------- */
/*                                SPOTIFY TYPES                               */
/* -------------------------------------------------------------------------- */

export interface ArtistTopTracks {
    readonly tracks: Track[]
}

export interface Track {
    readonly album: Album
    readonly artists: Artist[]
    readonly available_markets: string[]
    readonly disc_number: number
    readonly duration_ms: number
    readonly explicit: boolean
    readonly external_ids: ExternalIDS
    readonly external_urls: ExternalUrls
    readonly href: string
    readonly id: string
    readonly is_local: boolean
    readonly is_playable: boolean
    readonly name: string
    readonly popularity: number
    readonly preview_url: string
    readonly track_number: number
    readonly type: string
    readonly uri: string
}

export interface Album {
    readonly album_type: string
    readonly artists: Artist[]
    readonly available_markets: string[]
    readonly external_urls: ExternalUrls
    readonly href: string
    readonly id: string
    readonly images: Image[]
    readonly is_playable: boolean
    readonly name: string
    readonly release_date: Date
    readonly release_date_precision: string
    readonly total_tracks: number
    readonly type: string
    readonly uri: string
}

export interface Token {
    readonly access_token: string
    readonly token_type: string
    readonly expires_in: number
}

export interface TokenError {
    readonly error: string
    readonly error_description: string
}

export interface ArtistData {
    readonly external_urls: ExternalUrls
    readonly followers: Followers
    readonly genres: string[]
    readonly href: string
    readonly id: string
    readonly images: Image[]
    readonly name: string
    readonly popularity: number
    readonly type: string
    readonly uri: string
}

export interface ExternalUrls {
    readonly spotify: string
}

export interface Followers {
    readonly href: string
    readonly total: number
}

export interface Image {
    readonly url: string
    readonly height: number
    readonly width: number
}

export interface SearchData {
    readonly tracks: Tracks
    readonly artists: Artists
    readonly albums: Albums
    readonly playlists: Playlists
    readonly shows: Audiobooks
    readonly episodes: Episodes
    readonly audiobooks: Audiobooks
}

export interface DataError {
    readonly error: Error
}

export interface Error {
    readonly status: number
    readonly message: string
}

export interface Albums {
    readonly href: string
    readonly limit: number
    readonly next: string
    readonly offset: number
    readonly previous: string
    readonly total: number
    readonly items: AlbumElement[]
}

export interface AlbumElement {
    readonly album_type: string
    readonly total_tracks: number
    readonly available_markets: string[]
    readonly external_urls: ExternalUrls
    readonly href: string
    readonly id: string
    readonly images: Image[]
    readonly name: string
    readonly release_date: string
    readonly release_date_precision: string
    readonly restrictions: Restrictions
    readonly type: string
    readonly uri: string
    readonly artists: Artist[]
}

export interface Artist {
    readonly external_urls: ExternalUrls
    readonly href: string
    readonly id: string
    readonly name: string
    readonly type: string
    readonly uri: string
}

export interface Restrictions {
    readonly reason: string
}

export interface Artists {
    readonly href: string
    readonly limit: number
    readonly next: string
    readonly offset: number
    readonly previous: string
    readonly total: number
    readonly items: ArtistsItem[]
}

export interface ArtistsItem {
    readonly external_urls: ExternalUrls
    readonly followers: Followers
    readonly genres: string[]
    readonly href: string
    readonly id: string
    readonly images: Image[]
    readonly name: string
    readonly popularity: number
    readonly type: string
    readonly uri: string
}

export interface Audiobooks {
    readonly href: string
    readonly limit: number
    readonly next: string
    readonly offset: number
    readonly previous: string
    readonly total: number
    readonly items: AudiobooksItem[]
}

export interface AudiobooksItem {
    readonly authors?: Author[]
    readonly available_markets: string[]
    readonly copyrights: Copyright[]
    readonly description: string
    readonly html_description: string
    readonly edition?: string
    readonly explicit: boolean
    readonly external_urls: ExternalUrls
    readonly href: string
    readonly id: string
    readonly images: Image[]
    readonly languages: string[]
    readonly media_type: string
    readonly name: string
    readonly narrators?: Author[]
    readonly publisher: string
    readonly type: string
    readonly uri: string
    readonly total_chapters?: number
    readonly is_externally_hosted?: boolean
    readonly total_episodes?: number
}

export interface Author {
    readonly name: string
}

export interface Copyright {
    readonly text: string
    readonly type: string
}

export interface Episodes {
    readonly href: string
    readonly limit: number
    readonly next: string
    readonly offset: number
    readonly previous: string
    readonly total: number
    readonly items: EpisodesItem[]
}

export interface EpisodesItem {
    readonly audio_preview_url: string
    readonly description: string
    readonly html_description: string
    readonly duration_ms: number
    readonly explicit: boolean
    readonly external_urls: ExternalUrls
    readonly href: string
    readonly id: string
    readonly images: Image[]
    readonly is_externally_hosted: boolean
    readonly is_playable: boolean
    readonly language: string
    readonly languages: string[]
    readonly name: string
    readonly release_date: Date
    readonly release_date_precision: string
    readonly resume_point: ResumePoint
    readonly type: string
    readonly uri: string
    readonly restrictions: Restrictions
}

export interface ResumePoint {
    readonly fully_played: boolean
    readonly resume_position_ms: number
}

export interface Playlists {
    readonly href: string
    readonly limit: number
    readonly next: string
    readonly offset: number
    readonly previous: string
    readonly total: number
    readonly items: PlaylistsItem[]
}

export interface PlaylistsItem {
    readonly collaborative: boolean
    readonly description: string
    readonly external_urls: ExternalUrls
    readonly href: string
    readonly id: string
    readonly images: Image[]
    readonly name: string
    readonly owner: Owner
    readonly public: boolean
    readonly snapshot_id: string
    readonly tracks: Followers
    readonly type: string
    readonly uri: string
}

export interface Owner {
    readonly external_urls: ExternalUrls
    readonly followers: Followers
    readonly href: string
    readonly id: string
    readonly type: string
    readonly uri: string
    readonly display_name: string
}

export interface Tracks {
    readonly href: string
    readonly limit: number
    readonly next: string
    readonly offset: number
    readonly previous: string
    readonly total: number
    readonly items: TracksItem[]
}

export interface TracksItem {
    readonly album: AlbumElement
    readonly artists: Artist[]
    readonly available_markets: string[]
    readonly disc_number: number
    readonly duration_ms: number
    readonly explicit: boolean
    readonly external_ids: ExternalIDS
    readonly external_urls: ExternalUrls
    readonly href: string
    readonly id: string
    readonly is_playable: boolean
    readonly linked_from: LinkedFrom
    readonly restrictions: Restrictions
    readonly name: string
    readonly popularity: number
    readonly preview_url: string
    readonly track_number: number
    readonly type: string
    readonly uri: string
    readonly is_local: boolean
}

export interface ExternalIDS {
    readonly isrc: string
}

export interface LinkedFrom {}

/* -------------------------------------------------------------------------- */
/*                                  FUNCTIONS                                 */
/* -------------------------------------------------------------------------- */

function getTopTrack(tracks: Track[]): Track {
    let topTrack: Track = tracks.splice(0, 1)[0]

    for (const track of tracks) {
        if (track.popularity > topTrack.popularity) topTrack = track
    }

    return topTrack
}

interface FetchArtistDataParams {
    artistID: string
    token: string
}

async function fetchArtistData({
    artistID,
    token,
}: FetchArtistDataParams): Promise<ArtistData> {
    const url: string = `https://api.spotify.com/v1/artists/${artistID}`

    const headers: Record<PropertyKey, string> = {
        Authorization: `Bearer ${token}`,
    }

    const response: Response = await fetch(url, {method: 'GET', headers})
    const data: ArtistData | DataError = await response.json()

    if ('error' in data)
        throw new Error(`${data.error.status}: ${data.error.message}`)

    return data
}

interface FetchArtistIDParams {
    fullName: string
    token: string
}

async function fetchArtistID({
    fullName,
    token,
}: FetchArtistIDParams): Promise<string> {
    const urlBase: string = 'https://api.spotify.com/v1/search'
    const urlSearchParams: URLSearchParams = new URLSearchParams({
        q: fullName,
        type: 'artist',
        limit: '1',
    })
    const url: string = `${urlBase}?${urlSearchParams}`

    const headers: Record<PropertyKey, string> = {
        Authorization: `Bearer ${token}`,
    }

    const response: Response = await fetch(url, {method: 'GET', headers})
    const data: SearchData | DataError = await response.json()

    if ('error' in data)
        throw new Error(`${data.error.status}: ${data.error.message}`)

    return data.artists.items[0].id
}

interface FetchArtistTopTracksParams {
    artistID: string
    token: string
}

async function fetchArtistTopTracks({
    artistID,
    token,
}: FetchArtistTopTracksParams): Promise<ArtistTopTracks> {
    const url: string = `https://api.spotify.com/v1/artists/${artistID}/top-tracks`

    const headers: Record<PropertyKey, string> = {
        Authorization: `Bearer ${token}`,
    }

    const response: Response = await fetch(url, {method: 'GET', headers})
    const data: ArtistTopTracks | DataError = await response.json()

    if ('error' in data)
        throw new Error(`${data.error.status}: ${data.error.message}`)

    return data
}

async function fetchSpotifyToken(): Promise<Token> {
    if (!process.env.SPOTIFY_API_CLIENT_ID)
        throw new Error(
            '`SPOTIFY_API_CLIENT_ID` (environment variable) is not defined'
        )

    if (!process.env.SPOTIFY_API_CLIENT_SECRET)
        throw new Error(
            '`SPOTIFY_API_CLIENT_SECRET` (environment variable) is not defined'
        )

    const url: string = 'https://accounts.spotify.com/api/token'

    const headers: Record<PropertyKey, string> = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    const clientID: string = process.env.SPOTIFY_API_CLIENT_ID
    const clientSecret: string = process.env.SPOTIFY_API_CLIENT_SECRET
    const body: string = `grant_type=client_credentials&client_id=${clientID}&client_secret=${clientSecret}`

    const response: Response = await fetch(url, {method: 'POST', headers, body})
    const data: Token | TokenError = await response.json()

    if ('error' in data)
        throw new Error(`${data.error}: ${data.error_description}`)

    return data
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

;(async () => {
    const spotifyToken: Token = await fetchSpotifyToken()

    const bandNames = {
        first: 'oasis',
        second: 'linkin park',
    }

    const firstBandID: string = await fetchArtistID({
        fullName: bandNames.first,
        token: spotifyToken.access_token,
    })

    const firstBandData: ArtistData = await fetchArtistData({
        artistID: firstBandID,
        token: spotifyToken.access_token,
    })

    const firstBandTopTracks: ArtistTopTracks = await fetchArtistTopTracks({
        artistID: firstBandID,
        token: spotifyToken.access_token,
    })

    const firstBandTopTrack: Track = getTopTrack(firstBandTopTracks.tracks)

    const secondBandID: string = await fetchArtistID({
        fullName: bandNames.second,
        token: spotifyToken.access_token,
    })

    const secondBandData: ArtistData = await fetchArtistData({
        artistID: secondBandID,
        token: spotifyToken.access_token,
    })

    const secondBandTopTracks: ArtistTopTracks = await fetchArtistTopTracks({
        artistID: secondBandID,
        token: spotifyToken.access_token,
    })

    const secondBandTopTrack: Track = getTopTrack(secondBandTopTracks.tracks)

    const pointsPerBand: Record<keyof typeof bandNames, number> = {
        first: 0,
        second: 0,
    }

    console.log(
        `> Which band is more popular (${firstBandData.name}, or ${secondBandData.name})?`
    )

    console.log('\n> Comparison of popularity...')
    console.log(
        `\n> Popularity of ${firstBandData.name}: ${firstBandData.popularity} points of popularity.`
    )
    console.log(
        `> Popularity of ${secondBandData.name}: ${secondBandData.popularity} points of popularity.`
    )

    if (firstBandData.popularity > secondBandData.popularity) {
        console.log(
            `> ${firstBandData.name} has more popularity points than ${secondBandData.name}.`
        )
        pointsPerBand.first++
    } else if (firstBandData.popularity < secondBandData.popularity) {
        console.log(
            `> ${secondBandData.name} has more popularity points than ${firstBandData.name}.`
        )
        pointsPerBand.second++
    } else {
        console.log(
            `> ${firstBandData.name} has the same popularity points than ${secondBandData.name}.`
        )
    }

    console.log('\n> Comparison of followers...')
    console.log(
        `\n> Followers of ${firstBandData.name}: ${firstBandData.followers.total} followers.`
    )
    console.log(
        `> Followers of ${secondBandData.name}: ${secondBandData.followers.total} followers.`
    )

    if (firstBandData.followers.total > secondBandData.followers.total) {
        console.log(
            `> ${firstBandData.name} has more followers than ${secondBandData.name}.`
        )
        pointsPerBand.first++
    } else if (firstBandData.followers.total < secondBandData.followers.total) {
        console.log(
            `> ${secondBandData.name} has more followers than ${firstBandData.name}.`
        )
        pointsPerBand.second++
    } else {
        console.log(
            `> ${firstBandData.name} has the same number of followers than ${secondBandData.name}.`
        )
    }

    console.log('\n> Comparison of top track of each band...')
    console.log(
        `\n> Top track of ${firstBandData.name} (name, and popularity): ${firstBandTopTrack.name} (${firstBandTopTrack.popularity} points of popularity).`
    )
    console.log(
        `> Top track of ${secondBandData.name} (name, and popularity): ${secondBandTopTrack.name} (${secondBandTopTrack.popularity} points of popularity).`
    )

    if (firstBandTopTrack.popularity > secondBandTopTrack.popularity) {
        console.log(
            `> ${firstBandTopTrack.name} of ${firstBandData.name} band is more popular than ${secondBandTopTrack.name} of ${secondBandData.name} band.`
        )
        pointsPerBand.first++
    } else if (firstBandTopTrack.popularity < secondBandTopTrack.popularity) {
        console.log(
            `> ${secondBandTopTrack.name} of ${secondBandData.name} band is more popular than ${firstBandTopTrack.name} of ${firstBandData.name} band.`
        )
        pointsPerBand.second++
    } else {
        console.log(
            `> ${secondBandTopTrack.name} of ${secondBandData.name} band has the same popularity points than ${firstBandTopTrack.name} of ${firstBandData.name} band.`
        )
    }

    console.log('\n> In conclusion...')

    if (pointsPerBand.first > pointsPerBand.second) {
        console.log(
            `\n> ${firstBandData.name} band is more popular than ${secondBandData.name} band`
        )
    } else if (pointsPerBand.first < pointsPerBand.second) {
        console.log(
            `\n> ${secondBandData.name} band is more popular than ${firstBandData.name} band`
        )
    } else {
        console.log(
            `\n> ${firstBandData.name} band is as popular as ${secondBandData.name} band`
        )
    }
})()
