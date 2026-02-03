const myList = document.querySelector('.my_list');

document.querySelector('#add_item').addEventListener('click', () => {
	const li = document.createElement('li');
	li.textContent = 'Item';

	myList.appendChild(li);
});
