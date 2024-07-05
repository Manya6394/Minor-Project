const options = {
  method: 'GET',
  headers: {
    accept: 'application/json',
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiM2VlYTgxYWYwNDM4MjExYWVhZDRmOWI5YTA1ZWM3OCIsInN1YiI6IjY0ZjZjZjRkYThiMmNhMDBjNGFjNzc4ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.oeJ28_HU6_wCqlzsA5EbtAvZJ7uMxKVZoStRiXu7g4E'
  }
};

fetch('https://api.themoviedb.org/3/movie/popular?language=en-US&page=1', options)
  .then(response => response.json())
  .then(data => {

    for(var i=0;i<data.results.length;i++){
      var name=data.results[i].original_title;
      var rating=data.results[i].vote_average;
      var overview=data.results[i].overview;

      var id=data.results[i].id;

      var posterPath=data.results[i].poster_path;
      var imageURL='https://image.tmdb.org/t/p/original'+posterPath;
      var imgElement=document.createElement("img");
      imgElement.src=imageURL;

      const url = document.createElement("a")
      url.href="http://127.0.0.1:5500/Movie%20Project/movie%20page/index.html?id="+id


      const popularMoviesContainer=document.getElementById("popular-movies-container");

      const popularMoviesBox=createElementWithId("div","popular-movies-box");
      popularMoviesContainer.appendChild(url);
      url.appendChild(popularMoviesBox);

      const imageBox=createElementWithId("div","image-box");
      popularMoviesBox.appendChild(imageBox);
      imageBox.appendChild(imgElement);

      const textOverlay=createElementWithId("div","text-overlay");
      imageBox.appendChild(textOverlay);
      textOverlay.innerHTML=`
      <p id="overview">${overview.length>300?overview.substring(0,300) +"...":overview} </p>
      `

      const movieInfo= createElementWithId("div","movie-info");
      popularMoviesBox.appendChild(movieInfo);
      movieInfo.innerHTML=`
      <h3 id="name">${name}</h3>
      <p id="rating">⭐${rating} </p>
      `

    }
  })

  function createElementWithId(tag, id) {
    const element = document.createElement(tag);
    element.setAttribute("id", id);
    return element;
  }




fetch('https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1', options)
  .then(response => response.json())
  .then(data => {

    for(var i=0;i<data.results.length;i++){
      var name=data.results[i].original_title;
      var rating=data.results[i].vote_average;
      var overview=data.results[i].overview;
      var id=data.results[i].id;

      var posterPath=data.results[i].poster_path;
      var imageURL='https://image.tmdb.org/t/p/original'+posterPath;
      var imgElement=document.createElement("img");
      imgElement.src=imageURL;

      const url=document.createElement("a");
      url.href="http://127.0.0.1:5500/Movie%20Project/movie%20page/index.html?id="+id


      const nowPlayingMoviesContainer=document.getElementById("now-playing-movies-container");
      nowPlayingMoviesContainer.appendChild(url);

      const nowPlayingMoviesBox=createElementWithId("div","now-playing-movies-box");
      url.appendChild(nowPlayingMoviesBox);


      const imageBox=createElementWithId("div","image-box");
      nowPlayingMoviesBox.appendChild(imageBox);
      imageBox.appendChild(imgElement);

      const textOverlay=createElementWithId("div","text-overlay");
      imageBox.appendChild(textOverlay);
      textOverlay.innerHTML=`
      <p id="overview">${overview.length>300?overview.substring(0,300) +"...":overview} </p>
      `

      const movieInfo= createElementWithId("div","movie-info");
      nowPlayingMoviesBox.appendChild(movieInfo);
      movieInfo.innerHTML=`
      <h3 id="name">${name}</h3>
      <p id="rating">⭐${rating} </p>
      `

    }
  })


fetch('https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1', options)
  .then(response => response.json())
  .then(data => {

    for(var i=0;i<data.results.length;i++){
      var name=data.results[i].original_title;
      var rating=data.results[i].vote_average;
      var overview=data.results[i].overview;
      var id=data.results[i].id;
      var posterPath=data.results[i].poster_path;
      var imageURL='https://image.tmdb.org/t/p/original'+posterPath;
      var imgElement=document.createElement("img");
      imgElement.src=imageURL;

      const url = document.createElement("a")
      url.href="http://127.0.0.1:5500/Movie%20Project/movie%20page/index.html?id="+id


      const topRatedMoviesContainer=document.getElementById("top-rated-movies-container");
      topRatedMoviesContainer.appendChild(url);

      const topRatedMoviesBox=createElementWithId("div","top-rated-movies-box");
      url.appendChild(topRatedMoviesBox);




      const imageBox=createElementWithId("div","image-box");
      topRatedMoviesBox.appendChild(imageBox);
      imageBox.appendChild(imgElement);

      const textOverlay=createElementWithId("div","text-overlay");
      imageBox.appendChild(textOverlay);
      textOverlay.innerHTML=`
      <p id="overview">${overview.length>300?overview.substring(0,300) +"...":overview} </p>
      `

      const movieInfo= createElementWithId("div","movie-info");
      topRatedMoviesBox.appendChild(movieInfo);
      movieInfo.innerHTML=`
      <h3 id="name">${name}</h3>
      <p id="rating">⭐${rating} </p>
      `

    }
  })




fetch('https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1', options)
  .then(response => response.json())
  .then(data => {

    for(var i=0;i<data.results.length;i++){
      var name=data.results[i].original_title;
      var rating=data.results[i].vote_average;
      var overview=data.results[i].overview;
      var id=data.results[i].id;
      var posterPath=data.results[i].poster_path;
      var imageURL='https://image.tmdb.org/t/p/original'+posterPath;
      var imgElement=document.createElement("img");
      imgElement.src=imageURL;

      const url = document.createElement("a")
      url.href="http://127.0.0.1:5500/Movie%20Project/movie%20page/index.html?id="+id


      const upcomingMoviesContainer=document.getElementById("upcoming-movies-container");
      upcomingMoviesContainer.appendChild(url);

      const upcomingMoviesBox=createElementWithId("div","upcoming-movies-box");
      url.appendChild(upcomingMoviesBox);

      const imageBox=createElementWithId("div","image-box");
      upcomingMoviesBox.appendChild(imageBox);
      imageBox.appendChild(imgElement);


      const textOverlay=createElementWithId("div","text-overlay");
      imageBox.appendChild(textOverlay);

      var description = overview.length > 300 ? overview.substring(0, 300) + '...' : overview
      console.log(description)
      textOverlay.innerHTML=`
      <p id="overview">${description} </p>
      `

      const movieInfo= createElementWithId("div","movie-info");
      upcomingMoviesBox.appendChild(movieInfo);
      movieInfo.innerHTML=`
      <h3 id="name">${name}</h3>
      <p id="rating">⭐${rating} </p>
      `

    }
  })