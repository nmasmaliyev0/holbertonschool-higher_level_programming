const fetchData = async () => {
	try {
		const response = await fetch('https://hellosalut.stefanbohacek.com/?lang=fr');
		const data = await response.json();

		document.querySelector('#hello').textContent = data.hello;
	}
	catch (error) {
		console.log(error);
	}
};


fetchData();
