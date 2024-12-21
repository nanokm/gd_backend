$(document).ready(function () {
    $('.ui.search')
        .search({
            onSelect: function (selected_item) {
                const source = map.getSource('main_point');
                source.setData({

                    'type': 'FeatureCollection',
                    'features': [
                        {
                            // feature for Mapbox SF
                            'type': 'Feature',
                            'geometry': {
                                'type': 'Point',
                                'coordinates': selected_item.lat_long,
                            },
                        }
                    ]
                })

                resetFitBoundsFlag();
                updateCircleRadius(selected_item.lat_long, 2, 2, selected_item.lat_long);
                current_point = selected_item.lat_long;

                // Reset distance to default value
                $(".distance").removeClass("active");
                $(".default-distance").addClass("active");
            },
            minCharacters: 4,
            searchDelay: 220,
            apiSettings: {
                onResponse: function (autocompleteResponse) {
                    let response = {
                        results: []
                    };
                    $.each(autocompleteResponse, function (index, item) {
                        response.results.push({
                            title: item.title,
                            description: item.description,
                            lat_long: item.lat_long
                        })
                    });
                    return response;
                },
                url: "http://localhost:8080/geocoding/api/v1/autocomplete/?q={query}"
            }
        })
})
