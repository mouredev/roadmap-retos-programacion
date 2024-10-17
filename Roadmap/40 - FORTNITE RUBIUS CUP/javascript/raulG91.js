const https = require('node:https')

const CLIENT_ID = "Your Client ID "
const CLIENT_SECRET = "Your client secret"


async function getToken() {
    return new Promise(async function (resolve, reject) {

        const options = {
            hostname: 'id.twitch.tv',
            path: "/oauth2/token",
            method: "POST",
            headers: {
                'Content-type': "application/x-www-form-urlencoded"

            }
        };
        let body = {
            'grant_type': 'client_credentials',
            'client_secret': CLIENT_SECRET,
            'client_id': CLIENT_ID
        }

        // Encode body
        let form_body = []
        for (let element in body) {

            let encoded_prop = encodeURIComponent(element);
            let encoded_value = encodeURIComponent(body[element])
            form_body.push(encoded_prop + "=" + encoded_value);

        }
        form_body = form_body.join("&")

        let response_body = "";
        const req = https.request(options,res => {

            res.on('data', d => {
                response_body += d;
            });
            res.on('end', ()=>{
                let token = JSON.parse(response_body).access_token;
                resolve(token)
            });
            res.on('error',(e)=>{
                reject(e);
            })
        });

        req.on('error',(e) => {
            reject(e);
        });
        //Execute post request
        req.write(form_body);
        //End request
        req.end()
    })
}
async function getFollowers(token,id){

    return new Promise(function(resolve,reject){

        let query =`?broadcaster_id=${id}`;
        const header = {
            'Authorization': "Bearer "+ token,
            'Client-Id': CLIENT_ID
        };
        const options = {
            'hostname': 'api.twitch.tv',
            'path': `/helix/channels/followers${query}`,
            "method": "GET",
            "headers": header
        };
        let incoming_message = "";
        const req = https.get(options,(res)=>{
            if(res.statusCode == 200){
                res.on('data',(data)=>{
                    incoming_message += data
                })
                res.on("error",(error)=>{
                    reject(error.message)
                });
                res.on("end",()=>{
                    let user = JSON.parse(incoming_message)
                    resolve(user.total)
                })
            }
            else{
                reject("Error obteniendo seguidores")
            }
        })


    })
}
async function basicInfo(token,user){

    return new Promise(function(resolve,reject){

        let user_name = user.replace(" ","");
        let query = `?login=${user_name}`
        const header = {
            'Authorization': "Bearer "+ token,
            'Client-Id': CLIENT_ID
        };
        const options = {
            'hostname': 'api.twitch.tv',
            'path': `/helix/users${query}`,
            "method": "GET",
            "headers": header
        };
        let incoming_message = "";
        const req = https.get(options,(res)=>{

            if(res.statusCode == 200){

                res.on("data",(data)=>{
                    incoming_message+= data
                })
                res.on("error",(error)=>{
                    reject(error.message)
                })
                res.on("end",()=>{
                    let user = JSON.parse(incoming_message)
                    if(user.data[0]){
                        let create_at = user.data[0].created_at;
                        let id = user.data[0].id
                        resolve([id,create_at])

                    }
                    else{
                        reject()
                    }

         
                })
            }
            else{
                reject(`Error obteniendo usuario para ${user}`)
            }

        })

    })


}
async function getInfo(users){
    try{
        token = await getToken();

        let user_list = [];

        for(let user in users){
            try{

                let list = await basicInfo(token,users[user])
                let followers = await getFollowers(token,list[0])
    
                user_list.push( {
    
                    "username": users[user],
                    "created_at": list[1],
                    "followers": followers
                });
            }
            catch{
                console.log(`Error obteniendo datos para ${users[user]}`)
            }


        }
        return user_list
    }
    catch(Error){

        console.log("Error obteniendo token")

        }
}

function orderByFollowers(list){

    let new_list = list.sort((a,b)=>a.followers > b.followers?-1:1);

    return new_list; 
}

function orderByCreationDate(list){
    let new_list = list.sort((a,b)=>a.created_at < b.created_at?-1:1);

    return new_list; 

}

async function main(){
    let users = [
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
    let user_list = await getInfo(users)
    let odered_list_followers = orderByFollowers(user_list);

    for(let i=0; i< odered_list_followers.length; i++){

        console.log(`User: ${odered_list_followers[i].username}, followers: ${odered_list_followers[i].followers},`)
    }
    let odered_list_date = orderByCreationDate(user_list);

    for(let i=0; i< odered_list_date.length; i++){

        console.log(`User: ${odered_list_date[i].username}, fecha de creacion: ${odered_list_date[i].created_at},`)
    }


}

main()



