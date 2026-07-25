/*
*  Solución mixta con html y javascript para poder ser testeada en local
*/
<input type='file' onchange='openFile(event)'>

<script>
var openFile = function(event) {
	var input  = event.target;
	var reader = new FileReader();
	reader.onload = function() {

    		// Leer archivo
    		var file = reader.result.split("\n");
    		file.splice(0,1);	// quitamos cabecera

    		// Sólo queremos los activos
    		var activos = ''.split('');	// nuevo array
    		file=file.filter(function(cv,i){
    			if( cv.split(',')[2]=='activo' )
    				activos.push(cv);
    		});

    		// Barajamos el array 3 veces
		    for (let i = activos.length-1; i >activos.length-4; i--) { 
    		  const j = Math.floor(Math.random() * (i + 1)); 
          [activos[i], activos[j]] = [activos[j], activos[i]]; // intercambiar elemento del array
  		  } 

  		  // Nos quedamos con los tres primeros
  		  activos=activos.splice(0,3);

  		  // Mostramos el id y el email por consola
  		  for(var k in activos){
  			  console.log("Winner %d: %s (%d)", (k*1+1), activos[k].split(',')[1], activos[k].split(',')[0] );
  		  }
  };
  reader.readAsText(input.files[0]);
};
</script>
