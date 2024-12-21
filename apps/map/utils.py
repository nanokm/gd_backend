import logging

from django.conf import settings

logger = logging.getLogger("find_top_level_key")


def find_top_level_key(search_value: str) -> str:
    for top_level_key, sub_mapping in settings.OSM_CATEGORY_MAPPING.items():
        if isinstance(sub_mapping, dict):
            # Simplest mapping
            if sub_mapping.get("value") == search_value:
                return top_level_key

        elif isinstance(sub_mapping, list):
            for item in sub_mapping:
                if item.get("value") == search_value:
                    return top_level_key
    logger.info("No top level key found: search value: %s", search_value)
    return ""
