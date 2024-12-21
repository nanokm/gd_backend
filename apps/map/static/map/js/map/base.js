const TOKEN = 'pk.eyJ1Ijoia2FtaWxiOTYxMCIsImEiOiJjbTRtaDE4dWIwNHphMndxc3F2NWJmNmw1In0.HqebzlQEy9WPPxw3Fb_ntQ'
const MAPBOX_STYLE = 'mapbox://styles/kamilb9610/cm4t0vage001201s7ehqtfgl9'
const BASE_URL = "http://localhost:8080/map/find_points/"

let hasFitBounds = false
let initial_query_params = {
    "distance": 2,
    "category": "pharmacy,fast_food,restaurant,books,cafe,convenience,gym,community_centre",
    "lat": "52.1942434",
    "long": "21.0456641"
}
let current_point = [21.0456641, 52.1942434];
function resetFitBoundsFlag() {
    hasFitBounds = false;
}

mapboxgl.accessToken = TOKEN;
const map = new mapboxgl.Map({
    style: MAPBOX_STYLE,
    container: 'map', // container ID
    center: current_point, // starting position [lng, lat]. Note that lat must be set between -90 and 90
    zoom: 13, // starting zoom,
});

function createCircle(center, radius) {
    return turf.circle(center, radius, {
        steps: 200,
        units: 'kilometers'
    });
}

function fitBoundsToGeoJSON(sourceId) {
    if (hasFitBounds) return; // Jeśli focus już był, nie rób nic
    const source = map.getSource(sourceId);
    if (!source || !source._data) return;

    const bounds = new mapboxgl.LngLatBounds();

    const features = source._data.features;
    if (features === undefined) {
        // Ignore first fetch
        return
    }
    features.forEach(feature => {
        const geometry = feature.geometry;

        if (geometry.type === 'Point') {
            bounds.extend(geometry.coordinates);
        } else if (geometry.type === 'LineString' || geometry.type === 'MultiLineString') {
            geometry.coordinates.forEach(coord => bounds.extend(coord));
        } else if (geometry.type === 'Polygon' || geometry.type === 'MultiPolygon') {
            geometry.coordinates.forEach(ring => {
                ring.forEach(coord => bounds.extend(coord));
            });
        }
    });

    // Dopasowanie widoku do bounding box
    if (!bounds.isEmpty()) {
        map.fitBounds(bounds, {
            padding: 70,
            duration: 600
        });
    }
    hasFitBounds = true;
}


map.on('load', function () {
    var center = current_point;
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

    map.addSource('points', {
        type: 'geojson',
        // Use a URL for the value for the `data` property.
        data: updateUrlParams(BASE_URL, initial_query_params),
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
                'convenience',
                'cart1',
                'religion',
                'cross1',
                'community_centre',
                'building-columns-solid',
                'restaurant',
                'utensils1',
                'pharmacy',
                'pharmacy1',
                'fast_food',
                'burger1',
                'cafe',
                'coffe1',
                'books',
                'bookstore1',
                'gym',
                'gym1',
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
                        'coordinates': current_point,
                    },
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
