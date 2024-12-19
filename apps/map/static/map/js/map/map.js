map.on('load', function () {

    var activeCategories = ['convenience', 'restaurant', 'books', 'fast_food', 'gym', 'cafe', 'pharmacy', 'community_centre']; // Zmieniamy 'activity' na 'leisure'

// Funkcja do przełączania filtrów
    function toggleCategory(category, button) {
        var isActive = $(button).hasClass('active-' + category); // Sprawdzamy, czy przycisk ma klasę aktywnego koloru

        if (isActive) {
            // Jeśli przycisk jest aktywny, zmieniamy go na szary
            $(button).removeClass('active-' + category).addClass('grey');
            activeCategories = activeCategories.filter(c => c !== category);
        } else {
            // Jeśli przycisk nie jest aktywny, zmieniamy kolor na oryginalny
            $(button).removeClass('grey').addClass('active-' + category); // Dodajemy odpowiednią klasę aktywnego koloru
            activeCategories.push(category);
        }

        map.setFilter('points', ['in', 'category'].concat(activeCategories));

    }

    $('#toggle-convenience').on('click', function () {
        toggleCategory('convenience', this);
    });

    $('#toggle-restaurant').on('click', function () {
        toggleCategory('restaurant', this);
    });

    $('#toggle-books').on('click', function () {
        toggleCategory('books', this);
    });

    $('#toggle-fast_food').on('click', function () {
        toggleCategory('fast_food', this);
    });

    $('#toggle-gym').on('click', function () {
        toggleCategory('gym', this);
    });

    $('#toggle-cafe').on('click', function () {
        toggleCategory('cafe', this);
    });
    $('#toggle-pharmacy').on('click', function () {
        toggleCategory('pharmacy', this);
    });
    $('#toggle-community_centre').on('click', function () {
        toggleCategory('community_centre', this);
    });
});
