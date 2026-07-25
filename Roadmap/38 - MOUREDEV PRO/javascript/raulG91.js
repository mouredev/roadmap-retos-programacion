const { stat } = require('fs')
const path = require('path')
const fs = require('fs').promises

async function readFile(filename){

    const filePath = path.join(__dirname,filename)

    let fileData =  await fs.readFile(filePath)
    //Generate a list with all rows in the file
    dataList =  fileData.toString().split("\n")
    //Remove header
    return dataList.slice(1,dataList.length)
}


async function main(){
    try{
        fileData =  await readFile('file.csv')
        let active_users = []
        for(element of fileData){
            let[id,email,status] = element.split("|")
            status = status.trim().toLowerCase()
            if(status == "activo"){
                active_users.push({"id":id,"email":email,"status":status})
            }
        }

        if(active_users.length >= 3){
            //Get subscription winner
            index = Math.floor(Math.random() * active_users.length)
            console.log("Subscription winner " + active_users[index].email + " with id: "+active_users[index].id)
            active_users.splice(index,1) //Remove selected user
            //Get discount winner

            index = Math.floor(Math.random() *active_users.length)
            console.log("Discount winner " + active_users[index].email + " with id: "+active_users[index].id)
            active_users.splice(index,1) //Remove selected user
            // Get book winner
            index = Math.floor(Math.random() *active_users.length)
            console.log("Book winner " + active_users[index].email + " with id: "+active_users[index].id)
            active_users.splice(index,1)
        }
        else{
            console.log("There are least than 3 active users")
        }

    
    }catch (error){
        console.log("Error opening the file: " + error.message)
    }
    


}

main()