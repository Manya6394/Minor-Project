fetch("https://imdb8.p.rapidapi.com/auto-complete?q=movie", {
    "method": "GET",
    "headers": {
        "x-rapidapi-key" : "c366a40f51msh11fd12e46306d31p1334a2jsnd5430e30799c"
    }
})
.then(response => response.json())
.then(data => {
    const list = data.d;

    list.map((item) => {
        const name = item.l;
        const poster = item.i.imageUrl;
        const movie = `<li><img src = "${poster}"> <h2>${name}</h2> </li>`
        document.querySelector('.movies').innerHTML += movie;
    })
})
.catch(err => {
    console.log(err);
})