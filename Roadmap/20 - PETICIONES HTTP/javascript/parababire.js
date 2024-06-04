async function extraerCotizacion() {
  try {
    const URL = "https://api.coindesk.com/v1/bpi/currentprice.json";
    const RES_API = await fetch(URL);
    const JSON = await RES_API.json();
    console.log(`La cotización del bitcoin es: ${JSON.bpi.USD.rate_float} $`);
  } catch (error) {
    console.error("TypeError");
  }
}

extraerCotizacion();

fetch('https://api.coindesk .com/v1/bpi/currentprice.json')
  .then(response => {
      if (response.status === 200) {
        return response.json();
      } else {
        console.log(error);
      }
    }
  )
  .then(data => console.log(`La cotización del bitcoin es: ${data.bpi.USD.rate_float}$`))
  .catch(error=> console.log("Hay un error que no está entre 200 y 50x"));