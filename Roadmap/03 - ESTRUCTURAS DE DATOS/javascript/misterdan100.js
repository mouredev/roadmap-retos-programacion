const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

class ContactsAgenda {
    constructor() {
        this.contacts = [
            { name: 'daniel', number: 3107802775, id: 1 },
            { name: 'emma', number: 3123730300, id: 2 }
        ]
    }

    showMenu() {
        console.log('-------------')
        console.log('\x1b[33m%s\x1b[0m', 'Menu options:')
        console.log('1. Show agenda')
        console.log('2. Add new contact')
        console.log('3. Update a contact')
        console.log('4. Search a contact')
        console.log('5. Delete a contact')
        console.log('6. Exit')

        const options = {
            1: () => this.showAgenda(),
            2: () => this.addContact(),
            3: () => this.updateContact(),
            4: () => this.searchContact(),
            5: () => this.deleteContact(),
            6: () => this.exit(),
        }

        rl.question('Select an option: ', (opt) => {
            options[opt]()
            if(opt === '6') {
                rl.close()
            }

        })
    }

    showAgenda() {
        if(!this.contacts.length) {
            console.log('\x1b[31m%s\x1b[0m', 'The agenda is empty')
            this.showMenu()
            return
        }
        console.log('\x1b[32m%s\x1b[0m', `You have ${this.contacts.length} contact in the agenda.`)
        this.contacts.forEach(contact => console.log(contact))
        this.showMenu()
    }

    addContact() {
        const newContact = {}
        
        const askNumber = () => {
            rl.question('Input the contact number: ', (number) => {
                if(!isNaN(number) && number.trim() !== '' && number.length === 10) {
                    newContact.number = +number
                    newContact.id = this.contacts.length ? this.contacts.length + 1 : 1 
                    this.contacts.push(newContact)
                    console.log(this.contacts)
                    this.showMenu()
                } else {
                    console.log('Invalid number')
                    askNumber()
                }
            })
        }

        const askName = () => {

            rl.question('Input the new contact name: ', (name) => {
                if(name.trim().length > 0) {
                    newContact.name = name
                    askNumber()
                } else {
                    askName()
                }
            })
        }
        askName()
    }

    searchContact() {
        rl.question('Input the name or number to search contact: ', (data) => {
            let result 
            if(isNaN(data)) {
                result = this.contacts.filter( contact => contact.name.includes(data))
            } else {
                result = this.contacts.filter( contact => contact.number.toString().includes(data))
            }
            if(result.length > 0) {
                console.log('\x1b[32m%s\x1b[0m', 'Search result:')
                result.forEach(item => console.log(item))
                this.showMenu()
                return
            }
            console.log('\x1b[31m%s\x1b[0m', 'Any contact found')
            this.showMenu()
        })


    }

    updateContact() {
        console.log('\x1b[32m%s\x1b[0m', 'Contats in the agenda.')
        this.contacts.forEach(contact => console.log(contact))
        rl.question('Input contact ID to update: ', (contactId) => {
            const contactIDs = this.contacts.reduce((total, item) => [...total, item.id],[])
            if(!contactIDs.includes(+contactId)) {
                console.log('\x1b[32m%s\x1b[0m', 'ID not valid')
                this.updateContact()
                return
            }

            const newContactData = {}
            const askNumber = () => {
                rl.question('Input the contact number: ', (number) => {
                    if(!isNaN(number) && number.trim() !== '' && number.length === 10) {
                        newContactData.number = +number
                        this.contacts.map(currentContact => {
                            if(currentContact.id === contactId) {
                                currentContact.name = newContactData.name
                                currentContact.number = newContactData.number
                                return currentContact
                            }
                            return currentContact
                        })
                        console.log('\x1b[32m%s\x1b[0m', 'Contact updated successfully!')
                        console.log({...newContactData, id: +contactId})
                        this.showMenu()
                    } else {
                        console.log('Invalid number')
                        askNumber()
                    }
                })
            }
    
            const askName = () => {
    
                rl.question('Input the new contact name: ', (name) => {
                    if(name.trim().length > 0) {
                        newContactData.name = name
                        askNumber()
                    } else {
                        askName()
                    }
                })
            }
            askName()
        })
    }

    deleteContact() {
        console.log('\x1b[32m%s\x1b[0m', 'Contats in the agenda.')
        this.contacts.forEach(contact => console.log(contact))
        rl.question('Input contact ID to update: ', (contactId) => {
            const contactIDs = this.contacts.reduce((total, item) => [...total, item.id],[])
            if(!contactIDs.includes(+contactId)) {
                console.log('\x1b[32m%s\x1b[0m', 'ID not valid')
                this.deleteContact()
                return
            }

            const filteredContacts = this.contacts.filter( contact => contact.id !== +contactId)
            this.contacts = filteredContacts
            console.log('\x1b[32m%s\x1b[0m', 'Contact deleted successfully')
            this.showMenu()
        })

    }

    exit() {
        console.log('\n')
        console.log('App closed!')
    }
}

const newAgenda = new ContactsAgenda()
newAgenda.showMenu()