map.on('load', function () {


// Funkcja do przełączania filtrów
// Zmienna przechowująca aktywne kategorie
var activeCategories = ['shop', 'restaurant', 'leisure']; // Zmieniamy 'activity' na 'leisure'

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

        // Filtruj punkty na podstawie aktywnych kategorii
    map.setFilter('points', ['in', 'category'].concat(activeCategories));

}

// Eventy dla przycisków
$('#toggle-shops').on('click', function () {
    toggleCategory('shop', this);
});

$('#toggle-restaurants').on('click', function () {
    toggleCategory('restaurant', this);
});

$('#toggle-leisure').on('click', function () {
    toggleCategory('leisure', this);
});

});
