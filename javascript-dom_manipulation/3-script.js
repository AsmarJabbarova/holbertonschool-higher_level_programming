document.getElementById('toggle_header').onclick = changeClass;

function changeClass () {
  if (!document.querySelector('header').classList.replace('red', 'green')) {
    document.querySelector('header').classList.replace('green', 'red');
  }
}
