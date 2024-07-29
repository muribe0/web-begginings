
document.addEventListener('DOMContentLoaded', function() {
    fetch('https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_mdjGNqSuM4yRlDlO2VzeW4dKtkHLcEMUSPofGmEl') /*Fetch the data*/
    .then(response => response.json()) /*Turn the response to json*/
    .then(data => {
       /* Inside of data, there is another object called data
            'data' {
                'AUD' : 1.41
                ...
       *    }
       */
       const rate = data.data.EUR /*Get the data*/
       document.querySelector("body").innerHTML = `1 USD is equal to ${rate.toFixed(3)} EUR`; /*Display the data*/
    })
    .catch(error => {
       console.log('Error:', error);
    })
});