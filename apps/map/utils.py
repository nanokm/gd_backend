from django.conf import settings


def find_top_level_key(search_value):
    for top_level_key, sub_mapping in settings.OSM_CATEGORY_MAPPING.items():
        if isinstance(sub_mapping, dict):
            # Jeśli sub_mapping jest słownikiem
            if sub_mapping.get("value") == search_value:
                return top_level_key
        elif isinstance(sub_mapping, list):
            # Jeśli sub_mapping jest listą
            for item in sub_mapping:
                if item.get("value") == search_value:
                    return top_level_key
    return None  # Jeśli nie znaleziono
