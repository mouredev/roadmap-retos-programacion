import requests
import urllib.parse

def obtener_token_oauth(client_id, client_secret):
    url = 'https://id.twitch.tv/oauth2/token'
    
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }

    response = requests.post(url, data=data)

    if response.status_code != 200:
        raise Exception('Error al obtener el token OAuth')

    result = response.json()
    return result['access_token']

def obtener_info_usuario_twitch(access_token, client_id, username):
    username = ''.join([c for c in username if c.isalnum() or c == '_'])
    url = f"https://api.twitch.tv/helix/users?login={urllib.parse.quote(username)}"
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Client-ID': client_id
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    result = response.json()
    return result['data'][0] if 'data' in result and result['data'] else None

def obtener_numero_seguidores_twitch(access_token, client_id, user_id):
    url = f"https://api.twitch.tv/helix/channels/followers?broadcaster_id={user_id}"

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Client-ID': client_id
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return 0

    result = response.json()
    return result.get('total', 0)

def main():
    participantes = [
        'Abby', 'Ache', 'Adri Contreras', 'Agustin', 'Alexby', 'Ampeter', 'Ander', 'Ari Gameplays',
        'Arigely', 'Auronplay', 'Axozer', 'Beniju', 'By Calitos', 'Byviruzz', 'Carrera', 'Celopan',
        'Cheto', 'CrystalMolly', 'Dario Eme Hache', 'Dheyo', 'DjMariio', 'Doble', 'Elvisa', 'Elyas360',
        'Folagor', 'Grefg', 'Guanyar', 'Hika', 'Hiper', 'Ibai', 'Ibelky', 'Illojuan', 'Imantado',
        'Irina Isasia', 'JessKiu', 'Jopa', 'JordiWild', 'Kenai Souza', 'Keroro', 'Kidd Keo', 'Kiko Rivera',
        'Knekro', 'Koko', 'KronnoZomber', 'Leviathan', 'Lit Killah', 'Lola Lolita', 'Lolito', 'Luh',
        'Luzu', 'Mangel', 'Mayichi', 'Melo', 'MissaSinfonia', 'Mixwell', 'Mr. Jagger', 'Nate Gentile',
        'Nexxuz', 'Nia', 'Nil Ojeda', 'NissaXter', 'Ollie', 'Orslok', 'Outconsumer', 'Papi Gavi',
        'Paracetamor', 'Patica', 'Paula Gonu', 'Pausenpaii', 'Perxitaa', 'Plex', 'Polispol', 'Quackity',
        'RecueroDP', 'Reven', 'Rivers', 'RobertPG', 'Roier', 'Rojuu', 'Rubius', 'Shadoune', 'Silithur',
        'SpokSponha', 'Spreen', 'Spursito', 'Staxx', 'SuzyRoxx', 'Vicens', 'Vituber', 'Werlyb', 'Xavi',
        'Xcry', 'Xokas', 'Zarcort', 'Zeling', 'Zorman'
    ]

    client_id = 'TU_ID_DE_CLIENTE'
    client_secret = 'TU_SECRETO_DE_CLIENTE'

    try:
        access_token = obtener_token_oauth(client_id, client_secret)
        
        info_usuarios = []
        errores = []

        for participante in participantes:
            usuario = obtener_info_usuario_twitch(access_token, client_id, participante)

            if usuario:
                seguidores = obtener_numero_seguidores_twitch(access_token, client_id, usuario['id'])

                info_usuarios.append({
                    'username': usuario['display_name'],
                    'followers': seguidores,
                    'creation_date': usuario['created_at']
                })
            else:
                errores.append(f"El participante {participante} no tiene usuario en Twitch.")

        # Ordenar por número de seguidores
        ranking_por_seguidores = sorted(info_usuarios, key=lambda u: u['followers'], reverse=True)

        print("Ranking por número de seguidores:")
        for usuario in ranking_por_seguidores:
            print(f"{usuario['username']} - {usuario['followers']} seguidores")

        # Ordenar por antigüedad
        ranking_por_antiguedad = sorted(info_usuarios, key=lambda u: u['creation_date'])

        print("\nRanking por antigüedad de la cuenta:")
        for usuario in ranking_por_antiguedad:
            print(f"{usuario['username']} - Cuenta creada el {usuario['creation_date']}")

        if errores:
            print("\nErrores:")
            for error in errores:
                print(error)

    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == "__main__":
    main()
