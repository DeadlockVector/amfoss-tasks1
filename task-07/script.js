const API_KEY = '';

fetch(`https://api.openweathermap.org/data/2.5/weather?q=bengaluru&units=metric&appid=${API_KEY}`).then((data) => data.json())
    .then(( jsonData ) => {
        document.getElementById("text_location").innerHTML = jsonData.name
        document.getElementById("text_location_country").innerHTML = jsonData.sys.country
        document.getElementById("text_temp").innerHTML = jsonData.main.temp
        document.getElementById("text_desc").innerHTML = jsonData.weather[0].description
        document.getElementById("text_feels_like").innerHTML = jsonData.wind.speed
})

const cityInput = document.getElementById("cityInput");
const searchButton = document.getElementById("searchButton");

searchButton.addEventListener("click", () =>  {
    const cityName = cityInput.value;
    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${cityName}&units=metric&appid=${API_KEY}`).then((data) => data.json())
    .then(( jsonData ) => { 

        console.log(jsonData)
        
        if (jsonData.cod == '404') {

            document.getElementById("text_location").innerHTML = "City Not Found"
            document.getElementById("text_location_country").innerHTML = ""

            document.getElementById("text_temp").innerHTML = ""

            document.getElementById("text_desc").innerHTML = ""

            document.getElementById("text_feels_like").innerHTML = ""

        }
        else {
            
            document.getElementById("text_location").innerHTML = jsonData.name
            document.getElementById("text_location_country").innerHTML = jsonData.sys.country

            document.getElementById("text_temp").innerHTML = jsonData.main.temp

            document.getElementById("text_desc").innerHTML = jsonData.weather[0].description

            document.getElementById("text_feels_like").innerHTML = jsonData.wind.speed
        }
    })
})

