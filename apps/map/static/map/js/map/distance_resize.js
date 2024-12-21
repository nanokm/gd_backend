function updateUrlParams(baseUrl, newParams) {
    // Sprawdź, czy baseUrl zawiera protokół
    if (!/^https?:\/\//i.test(baseUrl)) {
        // Jeśli nie, dodaj domyślny protokół
        baseUrl = 'http://' + baseUrl;
    }

    // Utwórz obiekt URL z podanego baseUrl
    let urlObj = new URL(baseUrl);

    // Utwórz obiekt URLSearchParams z parametrów zapytania
    let params = new URLSearchParams(urlObj.search);

    // Zaktualizuj lub dodaj nowe parametry
    for (let key in newParams) {
        if (newParams.hasOwnProperty(key)) {
            params.set(key, newParams[key]);
        }
    }

    // Aktualizuj część zapytania w obiekcie URL
    urlObj.search = params.toString();

    // Zwróć nowy URL
    return urlObj.toString();
}

function updateCircleRadius(center, newRadius, distance, lat_long) {
    const newCircle = createCircle(center, newRadius);

    // Zaktualizuj dane źródła
    const source = map.getSource('circle');
    const brd = map.getSource('circle-outline');
    let new_params = {"distance": distance}
    if (lat_long !== undefined) {
        new_params["lat"] = lat_long[1];
        new_params["long"] = lat_long[0]
    }
    const new_url = updateUrlParams(BASE_URL, new_params)
    if (source) {
        brd.setData(newCircle);
        source.setData(newCircle);
        updateSourceData(new_url);
    }
}

// Funkcja do aktualizacji danych w źródle
function updateSourceData(newUrl) {
    const source = map.getSource('points');
    source.setData({
        "type": "FeatureCollection",
        "features": []
    });
    fetch(newUrl)
        .then(response => response.json())
        .then(newData => {
            const source = map.getSource('points');
            if (source) {
                source.setData(newData);
                fitBoundsToGeoJSON('points');
            } else {
                console.error('Źródło o identyfikatorze "points" nie zostało znalezione.');
            }
        })
        .catch(error => console.error('Błąd podczas pobierania danych:', error));
}

$(document).ready(function () {


    $(".distance").click(function () {
        resetFitBoundsFlag();
        var distance = $(this).attr('data-distance');

        // Reset 'active' class
        $(".distance").removeClass("active")
        $(this).addClass("active")
        updateCircleRadius(STARTING_POINT, distance, distance)
    })

});
