// Utilizando fetch para realizar una petición HTTP
fetch("https://jsonplaceholder.typicode.com/posts/5")
  .then((response) => {
    // Verifica si la respuesta fue exitosa
    if (!response.ok) {
      throw new Error("Network response was not ok " + response.statusText);
    }
    return response.text(); // Convierte la respuesta a texto
  })
  .then((data) => {
    console.log("Contenido de la web:", data); // Muestra el contenido en la consola
  })
  .catch((error) => {
    console.error("Hubo un problema con la petición fetch:", error); // Muestra el error en caso de que ocurra
  });
