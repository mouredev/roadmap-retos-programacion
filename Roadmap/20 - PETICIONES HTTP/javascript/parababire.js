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