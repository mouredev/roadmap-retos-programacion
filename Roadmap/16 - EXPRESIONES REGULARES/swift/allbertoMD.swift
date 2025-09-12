import Foundation

// Texto que contiene números.
let text = """
    El chef preparaba la receta con precisión, midiendo cada ingrediente con cuidado. 1.25 La cocina estaba llena de aromas tentadores que  inundaban el aire, despertando el apetito de cualquiera que pasara cerca. 2 Con un toque de sal y una pizca de pimienta, el sabor de la salsa comenzaba a tomar forma. 3.75

    Mientras tanto, en el horno, el pan se doraba lentamente, emitiendo un delicioso olor a hogar. 4 El chef sonrió satisfecho al ver que la masa había crecido de manera perfecta, alcanzando su punto justo de cocción. 5.5 Era un espectáculo para los sentidos, donde cada aroma, cada textura, se combinaba en armonía. 6.8

    Con habilidad experta, el chef emplató cada porción con elegancia, creando una presentación digna de un restaurante de alta cocina. 7.3 Cada plato era una obra de arte comestible, lista para deleitar a los comensales más exigentes. 8 El chef sabía que la comida no solo se disfrutaba con el paladar, sino también con la vista y el olfato. 9.25

    Al finalizar su obra maestra culinaria, el chef observó con orgullo la mesa preparada para recibir a los invitados. 10 Todo estaba listo para una velada inolvidable, llena de conversaciones animadas y sabores exquisitos. 11.75 Con una sonrisa, el chef se dispuso a dar la bienvenida a sus comensales, ansioso por compartir su pasión por la cocina con quienes apreciaban el arte de la gastronomía. 12.9
"""

// Lanza la 
do {
    // Lanza el inicializador de la structura Regex() y lo almacena en la variable regex.
    let regex = try Regex(#"[0-9]+(.[0-9]+)?"#)
    
    // Busca los todos los matches proporcionados en la expresion regular proporcionada por la variable reges.
    let matches = text.matches(of: regex)

    // Array String donde se almacenaaran los matches conseguidos por el metodo matches(of: ).
    var extractedNumbers = ""

    // Itera por el array que devuelve el metodo matches(of: )
    for m in matches {
        // Añade uno a uno los matches y extrae el string de cada match haciendo uso de .0.
        extractedNumbers.append("\(m.0), ")
    }
    // Elimina los dos ultimos caracteres del String extractedNumber que es ", ".
    extractedNumbers.removeLast(2)

    // Imprime el String con los matches.
    print("Estos son los números que contiene el texto:")
    print(extractedNumbers)
} catch {
    // Captura el error y lo imprime en caso de haberlo.
    print("ERROR ---> \(error.localizedDescription)")
}
// Espera 5 segundos antes de ejecutar la DIFICULTAD EXTRA.
sleep(5)






// DIFICULTAD EXTRA
print("\nDIFICULTAD EXTRA.")



// Pide por consola el valor de la variable email o imprime el error si algo falla.
print("\nIntroduce la dirección de correo electronico:")
guard let email = readLine() else {
    fatalError()
}

do {
    // Lanza el inicializador de la structura Regex() y lo almacena en la variable emailRegex.
    let emailRegex = try Regex(#"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"#)

    // Compara los matches con todo el contenido de la variiable email que coincida con la expresion regular proporcionada por emailRegex.
    if let emailWholeMatch = email.wholeMatch(of: emailRegex) {
        // Si la expresion regular a coincidido con todo el contenido de la variable email imprime "Dirección de correo correcta.".
        // La variable emailWholeMatch contiene el contenido de la variable email.
        print("La diirección de correo: \(emailWholeMatch.0) es correcta.\n")
    } else {
        // Si la expresion regular no ha coincidido con todo el contenido de la variable email se imprime "Correo no valido.".
        // La Variable emailWholeMatch esta vacia.
        print("Dirección de correo: \(email) no es valida.\n")
    }
} catch {
    // Captura el error y lo imprime en caso de haberlo.
    print("ERROR ---> \(error.localizedDescription)")
}


// Pide por consola el valor de la variable telephoneNumber o imprime el error si algo falla.
print("Introduce el número de telefono, con el siguiente formato: +prefijo 111 111 111:")
guard let telephoneNumber = readLine() else {
    fatalError()
}

do {
    // Lanza el inicializador de la structura Regex() y lo almacena en la variable telephoneNumbeeRegex.
    let telephoneNumberRegex = try Regex(#"^\+\d{1,3}\s\d{3}\s\d{3}\s\d{3}$"#)

    // Compara el match con todo el contenido de la variiable email que coincida con la expresion regular proporcionada por telephonoNumberRegex.
    if let telephoneNumberWholeMatch = telephoneNumber.wholeMatch(of: telephoneNumberRegex) {
        // Si la expresion regular a coincidido con todo el contenido de la variable email imprime "Dirección de correo correcta.".
        // La variable telephoneNumberWleMatch contiene el contenido de la variable email.
        print("El número de telefono: \(telephoneNumberWholeMatch.0) es correcto.\n")
    } else {
        // Si la expresion regular no ha coincidido con todo el contenido de la variable email se imprime "Correo no valido.".
        // La Variable telephoneNumberWholeMatch esta vacia.
        print("El número de telefono: \(telephoneNumber) no es valido.\n")
    }
} catch {
    // Captura el error y lo imprime en caso de haberlo.
    print("ERROR ---> \(error.localizedDescription)")
}


// Pide por consola el valor de la variable url o imprime el error si algo falla.
print("Introduce la URL:")
guard let url = readLine() else {
    fatalError()
}

do {
    // Lanza el inicializador de la structura Regex() con la expresion regular y lo almacena en la variable urlRegex.
    let urlRegex = try Regex(#"^(https?|ftp):\/\/[^\s\/$.?#]+\.[a-zA-Z]{2,}(\/[^\s\/$.?#]*)?$"#)

    // Compara el match con todo el contenido de la variiable email que coincida con la expresion regular proporcionada por urlrRegex.
    if let urlWholeMatch = url.wholeMatch(of: urlRegex) {
            // Si la expresion regular no ha coincidido con todo el contenido de la variable email se imprime "Correo no valido.".
        // La Variable urlWholeMatch tiene el contenido del la variable url.
        print("La URL: \(urlWholeMatch.0) es correcta.\n")
    } else {
        // Si la expresion regular no ha coincidido con todo el contenido de la varible email se imprime "Correo no valido.".
        // La Variable telephoneNumberWholeMatch esta vacia.
        print("La URL: \(url) no es valida.\n")
    }
} catch {
    // Captura el error y lo imprime en caso de haberlo.
    print("ERROR ---> \(error.localizedDescription)")
}

