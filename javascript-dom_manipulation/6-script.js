const fetchChracter = async () => {
    try {
        const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
        const data = await response.json();

        const { name } = data;

        document.querySelector('#character').textContent = name;
    }
    catch (error) {
        console.log(error);
    }
};


fetchChracter();
