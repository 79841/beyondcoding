const inputBox = document.querySelector(".input-box");
const input = document.querySelector(".input-task");
const tasksContainer = document.querySelector(".tasks-container");
const finishButtons = document.querySelectorAll(".finish");
const deleteButtons = document.querySelectorAll(".delete");

let toDoId = 0;

const getToDoList = () => {
  return JSON.parse(localStorage.getItem("todo-list"));
};

const setToDoList = (toDoList) => {
  localStorage.setItem("todo-list", JSON.stringify(toDoList));
  window.dispatchEvent(new Event("storage"));
  // displayToDoList();
};

const clearInput = () => {
  input.value = "";
};

const displayToDoList = () => {
  tasksContainer.innerHTML = "";
  for (toDo of getToDoList()) {
    if (toDo.progress !== "done") {
      tasksContainer.innerHTML += `<div id="${toDo.id}" class="task ${toDo.progress}">
      <div class="content">${toDo.task}</div>
      <div class="state-btn">
        <button class="finish" onclick="finishButtonHandler(this)">finish</button>
        <button class="delete" onclick="deleteButtonHandler(this)">delete</button>
      </div>
    </div>`;
    }
  }
  for (toDo of getToDoList()) {
    if (toDo.progress === "done") {
      tasksContainer.innerHTML += `<div id="${toDo.id}" class="task ${toDo.progress}">
      <div class="content">${toDo.task}</div>
      <div class="state-btn">
        <button class="finish" disabled>finished</button>
        <button class="delete" disabled></button>
      </div>
    </div>`;
    }
  }
};

const finishButtonHandler = (e) => {
  const element = e.parentElement.parentElement;
  const toDoList = getToDoList();
  // element.classList.add("change-state");

  for (toDo of toDoList) {
    if (toDo.id === element.id) {
      toDo.progress = "done";
    }
  }
  setToDoList(toDoList);
  // setTimeout(() => {
  //   setToDoList(toDoList);
  // }, 2000);
};

// const deleteButtonHandler = (e) => {
//   const target = e.parentElement.parentElement;
//   const toDoList = getToDoList("todo-list");
//   const result = toDoList.filter((toDo) => target.id != toDo.id);
//   setToDoList(result);
//   target.remove();
// };

inputBox.addEventListener("submit", (event) => {
  event.preventDefault();

  // if (input.value == "") {
  //   return;
  // }

  const toDoId = Number(localStorage.getItem("lastToDoId"));
  const toDoList = getToDoList();

  toDoList.unshift({
    id: "todo_" + toDoId,
    progress: "",
    task: input.value,
  });

  setToDoList(toDoList);

  localStorage.setItem("lastToDoId", toDoId + 1);

  clearInput();
});

window.addEventListener("storage", () => {
  displayToDoList();
});

window.onload = () => {
  if (!getToDoList()) {
    localStorage.setItem("todo-list", JSON.stringify([]));
    localStorage.setItem("lastToDoId", 0);
  }
  displayToDoList();
};
