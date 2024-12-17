$(document).ready(function () {
    function createCircle(center, radius) {
        return turf.circle(center, radius, {
            steps: 200, // Liczba segmentów dla wygładzenia okręgu
            units: 'kilometers' // Jednostka promienia
        });
    }

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


    function updateCircleRadius(center, newRadius, distance) {
        const newCircle = createCircle(center, newRadius);

        // Zaktualizuj dane źródła
        const source = map.getSource('circle');
        const brd = map.getSource('circle-outline');
        const new_url = updateUrlParams(BASE_URL, {"distance": distance})
        console.log(new_url);
        if (source) {
            brd.setData(newCircle);
            source.setData(newCircle);
            updateSourceData(new_url);
        }
    }

// Funkcja do aktualizacji danych w źródle
    function updateSourceData(newUrl) {
        fetch(newUrl)
            .then(response => response.json())
            .then(newData => {
                const source = map.getSource('points');
                if (source) {
                    source.setData(newData);
                } else {
                    console.error('Źródło o identyfikatorze "points" nie zostało znalezione.');
                }
            })
            .catch(error => console.error('Błąd podczas pobierania danych:', error));
    }

    $(".distance").click(function () {
        var distance = $(this).attr('data-distance');
        $(".distance").removeClass("active")
        $(this).addClass("active")
        center = [21.0456641, 52.1942434];
        updateCircleRadius(center, distance, distance)
    })

});
