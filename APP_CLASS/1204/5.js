const num = document.getElementById("number");
const plus = document.getElementsByClassName("plus")[0];
const minus = document.querySelector(".minus");

plus.addEventListener("click", function () {
  num.innerText = Number(num.innerText) + 1;
});

minus.addEventListener("click", function () {
  num.innerText = Number(num.innerText) - 1;
});

const form = document.getElementById("form");
const key = document.querySelector(".key");
const val = document.querySelector(".val");
const item = document.querySelector(".item");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  localStorage.setItem(key.value, val.value);
  item.innerHTML = key.value + " : " + localStorage.getItem(key.value);
});
