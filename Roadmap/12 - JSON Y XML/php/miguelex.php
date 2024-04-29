<?php 

$datos = array(
    'nombre' => 'Miguelex',
    'edad' => 48,
    'fechanacimiento' => '1975-09-13',
    'Lenguajes' => ['php', 'javascript', 'python', 'c#', 'java', 'pascal']
);

echo "\n\n";

echo "json" . "\n\n";

$json = json_encode($datos, JSON_PRETTY_PRINT);

file_put_contents('miguelex.json', $json);

$datos_json = file_get_contents('miguelex.json');

echo $datos_json;

echo "\n\n";

echo "xml" . "\n\n";

$xml = new SimpleXMLElement('<root/>');

foreach($datos as $key => $value){
    if(is_array($value)){
        $subnode = $xml->addChild($key);
        foreach($value as $k => $v){
            $subnode->addChild("lenguaje", $v);
        }
    } else {
        $xml->addChild($key, $value);
    }
}

$dom = dom_import_simplexml($xml)->ownerDocument;
$dom->formatOutput = true; 

file_put_contents('miguelex.xml', $dom->saveXML());

echo $dom->saveXML();

// Extra

class Miguelex {
    public $nombre;
    public $edad;
    public $fecha_nacimiento;
    public $lenguajes;

    public function fromJson(){
        $datos = json_decode(file_get_contents('miguelex.json'), true);
        $this->nombre = $datos['nombre'];
        $this->edad = $datos['edad'];
        $this->fecha_nacimiento = $datos['fecha nacimiento'];
        $this->lenguajes = $datos['Lenguajes'];

        unlink('miguelex.json');
    }

    public function fromXml(){
        $xml_content = file_get_contents('miguelex.xml');
    
    // Verificamos si se cargó correctamente
    if ($xml_content !== false) {
        // Intentamos convertir la cadena XML en un objeto SimpleXMLElement
        $xml = simplexml_load_string($xml_content);
        
        // Verificamos si se pudo cargar correctamente
        if ($xml !== false) {
            // Asignamos los valores de los elementos XML a los atributos de la clase
            $this->nombre = (string) $xml->nombre;
            $this->edad = (int) $xml->edad;
            $this->fecha_nacimiento = (string) $xml->{'fecha nacimiento'};

            // Recorremos los elementos 'lenguaje' dentro de 'Lenguajes'
            $this->lenguajes = [];
            foreach ($xml->Lenguajes->lenguaje as $lenguaje) {
                $this->lenguajes[] = (string) $lenguaje;
            }

            // Eliminamos el archivo XML después de leerlo
            unlink('miguelex.xml');
        } else {
            // Manejar el caso en que ocurra un error al cargar el archivo XML
            echo "Error: No se pudo cargar el archivo XML.";
        }
    } else {
        // Manejar el caso en que ocurra un error al leer el contenido del archivo XML
        echo "Error: No se pudo leer el contenido del archivo XML.";
    }
    }

    public function __toString(){
        return "Nombre: $this->nombre\nEdad: $this->edad\nFecha de nacimiento: $this->fecha_nacimiento\nLenguajes: " . implode(', ', $this->lenguajes);
    }
}

echo "\n\n";

echo "De json a clase\n";

$miguelex = new Miguelex();

$miguelex->fromJson();

echo $miguelex;

echo "\n\n";

echo "De xml a clase\n";

$miguelex2 = new Miguelex();

$miguelex2->fromXml();

echo $miguelex2;






