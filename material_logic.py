# material_logic.py

def get_material_suggestion(skin_result: dict) -> list:
    """
    Return recommended materials based on skin metrics.
    """
    materials = []

    brightness = skin_result.get("brightness", 0)
    redness = skin_result.get("redness", 0)

    # Example rules
    if brightness < 100:
        materials.append("Velvet")
    else:
        materials.append("Silk")

    if redness > 100:
        materials.append("Satin")
    else:
        materials.append("Chiffon")

    # Deduplicate
    return list(dict.fromkeys(materials))
