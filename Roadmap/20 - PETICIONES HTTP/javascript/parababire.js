fetch('https://api.coindesk.com/v1/bpi/currentprice.json')
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
    }
  )
  .then(data => console.log(`La cotización del bitcoin es: ${data.bpi.USD.rate_float}$`))
  .catch(error=> console.log(error));