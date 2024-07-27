document.getElementById('add_item').onclick = addItem;

function addItem () {
  document.querySelector('ul.my_list').innerHTML = document.querySelector('ul.my_list').innerHTML + '<li>Item</li>';
}
