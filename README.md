# skinwizard 🧪💄

A Python library for managing skincare products and formulations.

## Overview

Skincare! A realm filled with potions and elixirs, each crafted to nourish, protect, and enhance the skin's natural beauty. 🧪💄

This library provides support for several distinct types of skincare formulations, each serving a unique purpose in the quest for radiant, healthy skin.

## Product Types

The library supports 8 skincare product types:

1. 🌿 **Cleansers** - Products for cleansing the skin
2. 🍃 **Toners** - Products for balancing skin pH
3. ✨ **Serums** - Concentrated treatment products
4. 🧴 **Moisturizers** - Products for hydrating skin
5. 🛡 **Sunscreen** - Sun protection products
6. 🎭 **Masks** - Intensive treatment masks
7. 👀 **Eye Care** - Products for the eye area
8. 🎀 **Lip Care** - Products for lip care

Each plays a crucial role in a comprehensive skincare routine. 🧙‍♂️🧪💄✨

## Installation

```bash
pip install -e .
```

## Usage

```python
from skinwizard import ProductType

# Access product types
cleanser = ProductType.CLEANSERS
print(cleanser)  # Output: 🌿 Cleansers

# Get display name
print(cleanser.display_name)  # Output: Cleansers

# Get emoji
print(cleanser.emoji)  # Output: 🌿

# Iterate through all types
for product_type in ProductType:
    print(product_type)
```

## Testing

Run tests with:

```bash
python -m pytest tests/
```

or

```bash
python -m unittest discover tests/
```

## License

This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.
