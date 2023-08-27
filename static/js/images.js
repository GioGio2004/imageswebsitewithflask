const accessKey = "t_cmmlFXi0optCwhvA17U4J7TZ4x8uZuno75wFF80tw";

const formEl = document.getElementById("search-form");
const inputEl = document.getElementById("search-input");

const searchResults = document.querySelector(".search-results");
const showMore = document.getElementById("show-more-button");

let page = 1;

async function searchImages() {
    const inputData = inputEl.value; 
    const url =  `https://api.unsplash.com/search/photos?page=${page}&query=${inputData}&client_id=${accessKey}`;

    const response = await fetch(url);
    const data = await response.json();

    const results = data.results;

    if (page === 1) {
        searchResults.innerHTML = "";
    }

    results.map((result) => {
        const imageWrapper = document.createElement('div');
        imageWrapper.classList.add("search-res");
        const image = document.createElement('img');
        image.src = result.urls.small;
        image.alt = result.alt_description;
        const imagelink = document.createElement('a');
        imagelink.href = result.links.html;
        imagelink.target = "_blank";
        imagelink.textContent = result.alt_description;
        imageWrapper.appendChild(image);
        imageWrapper.appendChild(imagelink);
        searchResults.appendChild(imageWrapper);
    });
    page++;

    if (page > 1) {
        showMore.style.display = "block";
    }
}

formEl.addEventListener("submit", async (event) => {
    event.preventDefault();
    page = 1;
    await searchImages();
});

showMore.addEventListener("click", async (event) => {
    event.preventDefault();
    await searchImages();
});


