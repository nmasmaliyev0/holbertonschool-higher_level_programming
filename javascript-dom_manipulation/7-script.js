const ul = document.querySelector('#list_movies');

const fetchTitles = async () => {
	try {
		const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
		const data = await response.json();

		data.results.forEach((movie) => {
			const li = document.createElement('li');
			li.textContent = movie.title;

			ul.appendChild(li);
		});
	}
	catch (error) {
		console.log(error);
	};
};


fetchTitles();
