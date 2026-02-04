const fetchData = async (lang) => {
  try {
    const response = await fetch(`https://hellosalut.stefanbohacek.com/?lang=${lang}`);
    const data = await response.json();

    return data.hello;
  }
  catch (error) {
    console.log(error);
  };
};


document.querySelector('#btn_translate').addEventListener('click', () => {
  const dropdown = document.querySelector('#language_code');
  const lang = dropdown.value;

  fetchData(lang).then(hello => {
    document.querySelector('#hello').textContent = hello;
  });
});
