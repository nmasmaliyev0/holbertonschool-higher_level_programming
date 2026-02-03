const header = document.querySelector('header');

document.querySelector('#toggle_header').addEventListener('click', () => {
  header.classList.toggle("green");
  header.classList.toggle("red");
});
