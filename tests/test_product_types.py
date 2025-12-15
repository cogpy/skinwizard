"""Tests for product types module."""

import unittest
from skinwizard.product_types import ProductType


class TestProductType(unittest.TestCase):
    """Test cases for ProductType enum."""
    
    def test_all_product_types_exist(self):
        """Test that all 8 product types are defined."""
        expected_types = [
            ProductType.CLEANSERS,
            ProductType.TONERS,
            ProductType.SERUMS,
            ProductType.MOISTURIZERS,
            ProductType.SUNSCREEN,
            ProductType.MASKS,
            ProductType.EYE_CARE,
            ProductType.LIP_CARE,
        ]
        self.assertEqual(len(expected_types), 8)
        self.assertEqual(len(list(ProductType)), 8)
    
    def test_product_type_values(self):
        """Test that product types have correct string values."""
        self.assertEqual(ProductType.CLEANSERS.value, "cleansers")
        self.assertEqual(ProductType.TONERS.value, "toners")
        self.assertEqual(ProductType.SERUMS.value, "serums")
        self.assertEqual(ProductType.MOISTURIZERS.value, "moisturizers")
        self.assertEqual(ProductType.SUNSCREEN.value, "sunscreen")
        self.assertEqual(ProductType.MASKS.value, "masks")
        self.assertEqual(ProductType.EYE_CARE.value, "eye_care")
        self.assertEqual(ProductType.LIP_CARE.value, "lip_care")
    
    def test_display_names(self):
        """Test that product types have correct display names."""
        self.assertEqual(ProductType.CLEANSERS.display_name, "Cleansers")
        self.assertEqual(ProductType.TONERS.display_name, "Toners")
        self.assertEqual(ProductType.SERUMS.display_name, "Serums")
        self.assertEqual(ProductType.MOISTURIZERS.display_name, "Moisturizers")
        self.assertEqual(ProductType.SUNSCREEN.display_name, "Sunscreen")
        self.assertEqual(ProductType.MASKS.display_name, "Masks")
        self.assertEqual(ProductType.EYE_CARE.display_name, "Eye Care")
        self.assertEqual(ProductType.LIP_CARE.display_name, "Lip Care")
    
    def test_emojis(self):
        """Test that product types have correct emoji representations."""
        self.assertEqual(ProductType.CLEANSERS.emoji, "🌿")
        self.assertEqual(ProductType.TONERS.emoji, "🍃")
        self.assertEqual(ProductType.SERUMS.emoji, "✨")
        self.assertEqual(ProductType.MOISTURIZERS.emoji, "🧴")
        self.assertEqual(ProductType.SUNSCREEN.emoji, "🛡")
        self.assertEqual(ProductType.MASKS.emoji, "🎭")
        self.assertEqual(ProductType.EYE_CARE.emoji, "👀")
        self.assertEqual(ProductType.LIP_CARE.emoji, "🎀")
    
    def test_string_representation(self):
        """Test the string representation of product types."""
        self.assertEqual(str(ProductType.CLEANSERS), "🌿 Cleansers")
        self.assertEqual(str(ProductType.TONERS), "🍃 Toners")
        self.assertEqual(str(ProductType.SERUMS), "✨ Serums")
        self.assertEqual(str(ProductType.MOISTURIZERS), "🧴 Moisturizers")
        self.assertEqual(str(ProductType.SUNSCREEN), "🛡 Sunscreen")
        self.assertEqual(str(ProductType.MASKS), "🎭 Masks")
        self.assertEqual(str(ProductType.EYE_CARE), "👀 Eye Care")
        self.assertEqual(str(ProductType.LIP_CARE), "🎀 Lip Care")


if __name__ == "__main__":
    unittest.main()
