map.on('load', function () {

    var activeCategories = ['convenience', 'restaurant', 'books', 'fast_food', 'gym', 'cafe', 'pharmacy', 'community_centre'];

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

    $('.toggle-poi').on('click', function () {
        let poi  = $(this).data("poi");
        toggleCategory(poi, this);
    });
});
