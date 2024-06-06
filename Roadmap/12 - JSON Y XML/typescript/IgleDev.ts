//  1º Ejercicio
    let fs = require('fs')
    let readlineSync = require('readline-sync');
    let { DOMImplementation: ImplementationDOM, XMLSerializer: SerializeXML } = require('xmldom');

    // Para poder crear el archivo 

    interface Contenido {
      nombre: string,
      edad: number,
      fecha_nacimiento: string,
      lenguajes: Array<string>
    }

    let json: Contenido = {
      nombre: 'Adrián Iglesias', 
      edad: 19, 
      fecha_nacimiento: '03/11/2004',
      lenguajes: ['TypeScript', 'JavaScript', 'HTML', 'CSS']
    } 

    fs.writeFile(
      'info.json', 
      JSON.stringify(json), 
      (error:  NodeJS.ErrnoException | null) => {
      if(error) throw error
      console.log('JSON creado!')
    })

    //Leer contenido del fichero JSON
    fs.readFile('info.json', (error:  NodeJS.ErrnoException | null, data: any) => {
      if(error) throw error
      console.log(data.toString())
    })

    //Eliminar fichero JSON
    fs.unlink('info.json', (error:  NodeJS.ErrnoException | null) => {
      if(error) throw error
      console.log('JSON borrado!')
    })



    // PARA CREAR ARCHIVO XML

    // Crear un objeto DOMImplementation
    let domImplementation = new ImplementationDOM();

    //Crear un objeto XML Document
    let xmlBaseDoc: XMLDocument = domImplementation.createDocument(null, 'root');

    //Crear elementos y atributos
    let main: HTMLElement = xmlBaseDoc.createElement('main');
    let nombre: Attr = xmlBaseDoc.createAttribute('nombre');
    let edad: Attr = xmlBaseDoc.createAttribute('edad');
    let fecha_nacimiento: Attr = xmlBaseDoc.createAttribute('fecha_nacimiento');
    let lenguajes: Attr = xmlBaseDoc.createAttribute('lenguajes');

    //Agregamos los valores
    nombre.value = 'Adrián Iglesias'
    edad.value = '19'
    fecha_nacimiento.value = '03/11/2004'
    lenguajes.value = 'TypeScript, JavaScript, HTML, CSS'

    //Agregar elementos al documento
    main.setAttributeNode(nombre)
    main.setAttributeNode(edad)
    main.setAttributeNode(fecha_nacimiento)
    main.setAttributeNode(lenguajes)
    main.textContent = 'Informacion'
    xmlBaseDoc.documentElement.appendChild(main)

    //Convertir documento XML en cadena de texto
    let xmlString: string = new SerializeXML().serializeToString(xmlBaseDoc)


    //Crear fichero XML
    fs.writeFile(
      'info.xml', 
      xmlString, 
      (error:  NodeJS.ErrnoException | null) => {
      if(error) throw error
      console.log('XML creado!')
    })

    //Leer contenido del fichero XML
    fs.readFile('info.xml', (error:  NodeJS.ErrnoException | null, data: any) => {
      if(error) throw error
      let xmlString: string = data.toString()
      console.log(xmlString)
    })

    //Eliminar fichero XML
    fs.unlink('info.xml', (error:  NodeJS.ErrnoException | null) => {
      if(error) throw error
      console.log('JSON borrado')
    })