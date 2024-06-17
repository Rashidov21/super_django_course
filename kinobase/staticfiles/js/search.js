
function dynamicSearch(value){
    let url = 'search/'
    if(value.length > 2){
        fetch(url + `?data=${value}`)
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          // Work with the JSON data
          let movieResults = document.querySelector(".movie_results")
          let range = document.createRange();
          for(el of data.data){
            console.log(el)
            let result = `
                <div class="autocomplete-suggestions"
                style="position: absolute; max-height: 900px; z-index: 9999; width: 881px; display: block;">
                <div class="autocomplete-suggestion" data-index="1">
                <img src="/media/${el.cover}">
                <div class="info">
                    <div class="title">
                    <span>${el.title}</span>
                    </div>
                    <span class="rating">${el.kp_rating}</span><span
                    class="year">${el.year}, ${el.quality}</span>
                </div>
                </div>
            </div>
            `
            let fragment = range.createContextualFragment(result);
            movieResults.append(fragment)
          }
        })
        .catch(error => {
          console.error('There was a problem with the fetch operation:', error);
        });
    }


}