main();

function main(): void {

    let contacts: { [key: string]: string } = {};
    let exit: boolean = false;
    let option: string | null = "";
    let phone: string | null = "";

    while (!exit) {

        option = prompt("\nSelect an option\n1) Search contact\n2) Create contact\n3) Update a contact\n4) Delete contact\n0) Exit\n>> ");

        switch (option) {
            case "1":
                if (Object.keys(contacts).length > 0) {
                    option = prompt("\nEnter the name of the contact\n>> ");
                    if (typeof option === "string" && option in contacts) {
                        console.log("\n>> Contact " + option +  " - " + contacts[option]);
                    } else {
                        console.log("\n>> Contact not found...");
                    }
                } else {
                    console.log("\n>> You have no contacts in your address book...")
                }
                break;

            case "2":
                option = prompt("\nType the name of the new contact\n>> ");
                if (typeof option === "string") {
                    do {
                        phone = prompt("\nType the phone number of the new contact\n>> ");
                    } while (typeof phone === "string" && (!/^\d+$/.test(phone) || phone.length < 9 || phone.length > 11));
                    if (option && phone) {
                        contacts[option] = phone;
                    }
                }
                break;

            case "3":
                if (Object.keys(contacts).length > 0) {
                    option = prompt("\nType the name of the contact you want to update\n>> ");
                    if (typeof option === "string" && option in contacts) {
                        do {
                            phone = prompt("\nType the new contact's phone number\n>> ");
                        } while (typeof phone === "string" && (!/^\d+$/.test(phone) || phone.length < 9 || phone.length > 11));
                        if (option && phone) {
                            contacts[option] = phone;
                        }
                        console.log("\n>> Contact " + option +  " - " + contacts[option]);
                    } else {
                        console.log("\n>> Contact not found...");
                    }
                } else {
                    console.log("\n>> You have no contacts in your address book...")
                }
                break;

            case "4":
                if (Object.keys(contacts).length > 0) {
                    option = prompt("\nType the name of the contact you want to delete\n>> ");
                    if (typeof option === "string" && option in contacts) {
                        delete contacts[option];
                        console.log("\n>> Contact " + option + " deleted");
                    } else {
                        console.log("\n>> Contact not found...");
                    }
                } else {
                    console.log("\n>> You have no contacts in your address book...")
                }
                break;

            case "0":
                exit = true;
                console.log("\n>> Leaving...");
                break;
        
            default:
                console.log("\n>> Invalid option...");
                break;
        }

    }

}
