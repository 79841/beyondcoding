import config from "./config.js";

const imgSliderBox = document.querySelector(".img-slider");
const genreSection = document.querySelector(".genre");

const makeImgSlider = async () => {
  const { results } = await (
    await fetch(
      config.trending_list_url +
        new URLSearchParams({
          api_key: config.api_key,
        })
    )
  ).json();
  console.log(results);
  results.forEach((item) => {
    imgSliderBox.innerHTML += `
    <a href="#">
    <img src="${config.img_url}${item.poster_path}" alt="">
    </a>
    `;
  });

  let leftGap = 0;

  setInterval(() => {
    const img = document.querySelector(".home .img-slider a img");
    const numOfImg = Math.round(document.body.offsetWidth / img.offsetWidth);
    imgSliderBox.style.left = `-${leftGap * 100}%`;
    if (leftGap >= results.length / numOfImg - 1) {
      leftGap = 0;
    } else {
      leftGap += 1;
    }
  }, 3000);
};
makeImgSlider();

const makeGenreSection = async () => {
  const { genres } = await (
    await fetch(
      config.genres_list_url +
        new URLSearchParams({
          api_key: config.api_key,
        })
    )
  ).json();

  genres.forEach();
};
makeGenreSection();

// fetch(
//   config.genres_list_url +
//     new URLSearchParams({
//       api_key: config.api_key,
//     })
// )
//   .then((res) => res.json())
//   .then((data) => {
//     data.genres.forEach((item) => {
//       fetchMoviesListByGenres(item.id, item.name);
//     });
//   });

const fetchMoviesListByGenres = (id, genres) => {
  fetch(
    config.movie_genres_url +
      new URLSearchParams({
        api_key: config.api_key,
        with_genres: id,
        page: Math.floor(Math.random() * 3) + 1,
      })
  )
    .then((res) => res.json())
    .then((data) => {
      makeCategoryElement(`${genres}_movie`, data.results);
    })
    .catch((err) => console.log(err));
};

const makeCategoryElement = (category, data) => {
  categorySection.innerHTML += `<div class="movie-list">
    <button class="pre-btn">
      <img src="img/pre.png" alt="" />
    </button>
    <h1 class="movie-category">${category.split("_").join(" ")}</h1>
    <div class="movie-container" id="${category}">

    </div>
    <button class="nxt-btn">
      <img src="img/nxt.png" alt="" />
    </button>
  </div>`;
  makeCards(category, data);
};

const makeCards = (id, data) => {
  const movieContainer = document.getElementById(id);
  data.forEach((item, i) => {
    if (item.backdrop_path == null) {
      item.backdrop_path = item.poster_path;
      if (item.backdrop_path == null) {
        return;
      }
    }

    movieContainer.innerHTML += `
    <div class="movie">
        <img src="${config.img_url}${item.backdrop_path}" alt="" />
        <p class="movie-title">${item.title}</p>
    </div>
    `;
  });
};
