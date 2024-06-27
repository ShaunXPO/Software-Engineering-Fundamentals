### Automated Pytest testing

### pytest test_it_asset_reg.py

# Import the required module

### Without adding this table in I can't seem to get it to test my code. Had to use ChatGPT to understand this and still struggling with the testing.

import pytest
from it_asset_reg import ITAsset, find_asset_by_record_number, get_valid_date

@pytest.fixture
def setup_assets():
    return [
        ITAsset(1, "Laptop", "1234567890", "Computer", "Black", "Alice", "HR", "10.10.2023"),
        ITAsset(2, "Desktop", "0987654321", "Computer", "White", "Bob", "IT", "01.01.2024"),
        ITAsset(3, "Printer", "1112131415", "Hardware", "Grey", "Charlie", "Finance", "28.09.2023"),
        ITAsset(4, "Router", "1617181920", "Networking", "Black", "David", "IT", "28.04.2020"),
        ITAsset(5, "Monitor", "2122232425", "Hardware", "Black", "Eve", "HR", "02.02.2012"),
        ITAsset(6, "Keyboard", "2627282930", "Hardware", "Black", "Frank", "Admin", "04.04.2008"),
        ITAsset(7, "Mouse", "3132333435", "Hardware", "Black", "Grace", "Admin", "07.07.2021"),
        ITAsset(8, "Phone", "3637383940", "Mobile Telephone", "Silver", "Hank", "Sales", "15.04.2022"),
        ITAsset(9, "Tablet", "4142434445", "Computer", "Gold", "Ivy", "Marketing", "10.10.2018"),
        ITAsset(10, "Switch", "4647484950", "Networking", "Blue", "Jack", "IT", "09.06.2021")
    ]

def test_find_asset_by_record_number_existing(setup_assets):
    # Test case for a record number that exists
    assets = setup_assets
    asset = find_asset_by_record_number(assets, 5)
    assert asset is not None
    assert asset.record_number == 5
    assert asset.item_name == "Monitor"

def test_find_asset_by_record_number_non_existing(setup_assets):
    # Test case for a record number that does not exist
    assets = setup_assets
    asset = find_asset_by_record_number(assets, 12)
    assert asset is None

def test_find_asset_by_record_number_alpha(setup_assets):
    # Test case for a record number input as an alpha
    assets = setup_assets
    with pytest.raises(TypeError):
        find_asset_by_record_number(assets, "Dad")

def test_get_valid_date_valid_format():
    # Test valid date format
    date_str = "15.04.2023"
    with pytest.raises(StopIteration):
        input_mock = lambda : date_str
