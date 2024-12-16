const TOKEN = 'pk.eyJ1Ijoia2FtaWxiOTYxMCIsImEiOiJjbTRtaDE4dWIwNHphMndxc3F2NWJmNmw1In0.HqebzlQEy9WPPxw3Fb_ntQ'
const BASE_URL = "http://localhost:8080/map/find_points/?distance=2&category=shop,leisure,religion&lat=52.1942434&long=21.0456641"
const MAPBOX_STYLE = 'mapbox://styles/kamilb9610/cm4qqbyym00a501safqyj8g0f'

mapboxgl.accessToken = TOKEN;
const map = new mapboxgl.Map({
    style: MAPBOX_STYLE,
    container: 'map', // container ID
    center: [21.0456641, 52.1942434], // starting position [lng, lat]. Note that lat must be set between -90 and 90
    zoom: 13, // starting zoom,
});
map.on('load', function () {
    var center = [21.0456641, 52.1942434];
    var radiusTwo = 2;
    var options = {steps: 200, units: 'kilometers', properties: {foo: 'bar'}};
    var circle = turf.circle(center, radiusTwo, options);

    map.addLayer({
        "id": "circle",
        "type": "fill",
        "dynamic": true,
        "source": {
            "type": "geojson",
            "data": circle,
            "lineMetrics": true,
        },
        "paint": {
            "fill-color": "#b36d05",
            "fill-antialias": true,
            "fill-opacity": 0.1,
        },
        "layout": {}
    });


    map.addLayer({
        'id': 'circle-outline',
        'type': 'line',
        'source': {
            'type': 'geojson',
            'data': circle,
            "lineMetrics": true,
        },
        'paint': {
            'line-color': '#d69431',
            'line-width': 3,
            'line-opacity': 0.4,
        }
    });


    map.addControl(new mapboxgl.NavigationControl({showCompass: false}));
});


map.on('load', () => {
    // Add a GeoJSON source with 2 points
    map.addSource('points', {
        type: 'geojson',
        // Use a URL for the value for the `data` property.
        data: BASE_URL,
    });

    // Add a symbol layer
    map.addLayer({
        'id': 'points',
        'type': 'symbol',
        'source': 'points',
        'layout': {
            'icon-image': [
                'match',
                ['get', 'category'],
                'shop',
                'cart1',
                'religion',
                'cross1',
                'leisure',
                'building-columns-solid',
                "#cecece"
            ],
            'text-field': ['get', 'name'],

            'text-font': [
                'Open Sans Regular',
                'Arial Unicode MS Regular'
            ],
            "text-size": 11,
            'text-offset': [0, 1.25],
            'text-anchor': 'top'
        }
    });

    // Add a GeoJSON source with 2 points
    map.addSource('main_point', {
        'type': 'geojson',
        'data': {
            'type': 'FeatureCollection',
            'features': [
                {
                    // feature for Mapbox SF
                    'type': 'Feature',
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [21.0456641, 52.1942434]
                    },
                    'properties': {
                        'title': 'Mapbox SF'
                    }
                }
            ]
        }
    });

    // Add a symbol layer
    map.addLayer({
        'id': 'main_point',
        'type': 'symbol',
        'source': 'main_point',
        'layout': {
            'icon-image': 'house',
        }
    });

});
