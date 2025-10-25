"""
Skincare product types module.

Defines the different types of skincare formulations.
"""

from enum import Enum


class ProductType(Enum):
    """
    Enumeration of skincare product types.
    
    Each type represents a distinct formulation serving a unique purpose
    in a comprehensive skincare routine:
    
    - CLEANSERS: Products for cleansing the skin 🌿
    - TONERS: Products for balancing skin pH 🍃
    - SERUMS: Concentrated treatment products ✨
    - MOISTURIZERS: Products for hydrating skin 🧴
    - SUNSCREEN: Sun protection products 🛡
    - MASKS: Intensive treatment masks 🎭
    - EYE_CARE: Products for eye area 👀
    - LIP_CARE: Products for lip care 🎀
    """
    
    CLEANSERS = "cleansers"
    TONERS = "toners"
    SERUMS = "serums"
    MOISTURIZERS = "moisturizers"
    SUNSCREEN = "sunscreen"
    MASKS = "masks"
    EYE_CARE = "eye_care"
    LIP_CARE = "lip_care"
    
    @property
    def display_name(self) -> str:
        """Get the human-readable display name for the product type."""
        display_names = {
            ProductType.CLEANSERS: "Cleansers",
            ProductType.TONERS: "Toners",
            ProductType.SERUMS: "Serums",
            ProductType.MOISTURIZERS: "Moisturizers",
            ProductType.SUNSCREEN: "Sunscreen",
            ProductType.MASKS: "Masks",
            ProductType.EYE_CARE: "Eye Care",
            ProductType.LIP_CARE: "Lip Care",
        }
        return display_names[self]
    
    @property
    def emoji(self) -> str:
        """Get the emoji representation for the product type."""
        emojis = {
            ProductType.CLEANSERS: "🌿",
            ProductType.TONERS: "🍃",
            ProductType.SERUMS: "✨",
            ProductType.MOISTURIZERS: "🧴",
            ProductType.SUNSCREEN: "🛡",
            ProductType.MASKS: "🎭",
            ProductType.EYE_CARE: "👀",
            ProductType.LIP_CARE: "🎀",
        }
        return emojis[self]
    
    def __str__(self) -> str:
        """Return a string representation of the product type."""
        return f"{self.emoji} {self.display_name}"
