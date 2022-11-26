const inputBox = document.querySelector(".input-box");
const input = document.querySelector(".input-task");
const tasksContainer = document.querySelector(".tasks-container");

let test = 0;

const getToDoList = () => {
  return JSON.parse(localStorage.getItem("todo-list"));
};

const setToDoList = (toDo) => {
  const toDoList = getToDoList();
  toDoList.unshift(toDo);
  localStorage.setItem("todo-list", JSON.stringify(toDoList));
  window.dispatchEvent(new Event("storage"));
};

const clearInput = () => {
  input.value = "";
};

inputBox.addEventListener("submit", (event) => {
  event.preventDefault();
  setToDoList(input.value);
  clearInput();
});

const displayToDoList = () => {
  tasksContainer.innerHTML = "";
  for (toDo of getToDoList()) {
    const component = `<div class="task">
        <div class="content">${toDo}</div>
        <div class="state-btn">
          <button class="finish">finish</button>
          <button class="delete">delete</button>
        </div>
      </div>`;
    tasksContainer.innerHTML += component;
  }
};

window.addEventListener("storage", () => {
  displayToDoList();
  console.log(getToDoList());
});

window.onload = () => {
  if (!getToDoList()) {
    localStorage.setItem("todo-list", JSON.stringify([]));
  }
  displayToDoList();
};
