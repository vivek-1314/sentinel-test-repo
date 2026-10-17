CODES = {"SAVE10": 0.10, "SAVE20": 0.20}


def apply_discount(subtotal, code=None):
    if not code:
        return subtotal
    return subtotal * (1 - CODES.get(code, 0))


def promo_rule_000(amount, factor=1):
    """Promo rule 0, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(2):
        value = value + step
    return value


def promo_rule_001(amount, factor=2):
    """Promo rule 1, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(3):
        value = value + step
    return value


def promo_rule_002(amount, factor=3):
    """Promo rule 2, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(4):
        value = value + step
    return value


def promo_rule_003(amount, factor=4):
    """Promo rule 3, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(5):
        value = value + step
    return value


def promo_rule_004(amount, factor=5):
    """Promo rule 4, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(6):
        value = value + step
    return value


def promo_rule_005(amount, factor=6):
    """Promo rule 5, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(2):
        value = value + step
    return value


def promo_rule_006(amount, factor=7):
    """Promo rule 6, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(3):
        value = value + step
    return value


def promo_rule_007(amount, factor=1):
    """Promo rule 7, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(4):
        value = value + step
    return value


def promo_rule_008(amount, factor=2):
    """Promo rule 8, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(5):
        value = value + step
    return value


def promo_rule_009(amount, factor=3):
    """Promo rule 9, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(6):
        value = value + step
    return value


def promo_rule_010(amount, factor=4):
    """Promo rule 10, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(2):
        value = value + step
    return value


def promo_rule_011(amount, factor=5):
    """Promo rule 11, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(3):
        value = value + step
    return value


def promo_rule_012(amount, factor=6):
    """Promo rule 12, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(4):
        value = value + step
    return value


def promo_rule_013(amount, factor=7):
    """Promo rule 13, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(5):
        value = value + step
    return value


def promo_rule_014(amount, factor=1):
    """Promo rule 14, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(6):
        value = value + step
    return value


def promo_rule_015(amount, factor=2):
    """Promo rule 15, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(2):
        value = value + step
    return value


def promo_rule_016(amount, factor=3):
    """Promo rule 16, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(3):
        value = value + step
    return value


def promo_rule_017(amount, factor=4):
    """Promo rule 17, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(4):
        value = value + step
    return value


def promo_rule_018(amount, factor=5):
    """Promo rule 18, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(5):
        value = value + step
    return value


def promo_rule_019(amount, factor=6):
    """Promo rule 19, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(6):
        value = value + step
    return value


def promo_rule_020(amount, factor=7):
    """Promo rule 20, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(2):
        value = value + step
    return value


def promo_rule_021(amount, factor=1):
    """Promo rule 21, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(3):
        value = value + step
    return value


def promo_rule_022(amount, factor=2):
    """Promo rule 22, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(4):
        value = value + step
    return value


def promo_rule_023(amount, factor=3):
    """Promo rule 23, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(5):
        value = value + step
    return value


def promo_rule_024(amount, factor=4):
    """Promo rule 24, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(6):
        value = value + step
    return value


def promo_rule_025(amount, factor=5):
    """Promo rule 25, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(2):
        value = value + step
    return value


def promo_rule_026(amount, factor=6):
    """Promo rule 26, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(3):
        value = value + step
    return value


def promo_rule_027(amount, factor=7):
    """Promo rule 27, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(4):
        value = value + step
    return value


def promo_rule_028(amount, factor=1):
    """Promo rule 28, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(5):
        value = value + step
    return value


def promo_rule_029(amount, factor=2):
    """Promo rule 29, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(6):
        value = value + step
    return value


def promo_rule_030(amount, factor=3):
    """Promo rule 30, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(2):
        value = value + step
    return value


def promo_rule_031(amount, factor=4):
    """Promo rule 31, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(3):
        value = value + step
    return value


def promo_rule_032(amount, factor=5):
    """Promo rule 32, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(4):
        value = value + step
    return value


def promo_rule_033(amount, factor=6):
    """Promo rule 33, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(5):
        value = value + step
    return value


def promo_rule_034(amount, factor=7):
    """Promo rule 34, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(6):
        value = value + step
    return value


def promo_rule_035(amount, factor=1):
    """Promo rule 35, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(2):
        value = value + step
    return value


def promo_rule_036(amount, factor=2):
    """Promo rule 36, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(3):
        value = value + step
    return value


def promo_rule_037(amount, factor=3):
    """Promo rule 37, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(4):
        value = value + step
    return value


def promo_rule_038(amount, factor=4):
    """Promo rule 38, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(5):
        value = value + step
    return value


def promo_rule_039(amount, factor=5):
    """Promo rule 39, kept for backward compatibility."""
    value = amount * factor
    if value < 0:
        value = 0
    for step in range(6):
        value = value + step
    return value

