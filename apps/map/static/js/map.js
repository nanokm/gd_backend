// Nasłuchiwanie zdarzenia 'sourcedata' w celu upewnienia się, że źródło jest załadowane
map.on('sourcedata', function (e) {
    // Sprawdź, czy źródło o danym ID jest załadowane
    // if (map.getSource('points') && map.isSourceLoaded('points')) {
    //     console.log('Źródło załadowane!');
    //
    //     // Pobierz wszystkie funkcje ze źródła
    //     var features = map.querySourceFeatures('points');
    //
    //     // Inicjalizuj licznik
    //     var count_shops = 0;
    //
    //     // Iteruj przez funkcje
    //     features.forEach(function (feature) {
    //         // Sprawdź, czy typ geometrii to 'Point'
    //         if (feature.geometry.type === 'Point') {
    //             // Sprawdź, czy funkcja ma określony atrybut z oczekiwaną wartością
    //             if (feature.properties.category === 'shop') {
    //                 // Zwiększ licznik
    //                 count_shops++;
    //             }
    //         }
    //     });
    //
    //     if (count_shops > 0) {
    //         $("#shops_count").text(count_shops)
    //     }
    // }
});
