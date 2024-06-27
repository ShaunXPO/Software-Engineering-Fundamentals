### Automated Pytest testing

### pytest test_it_asset_reg.py

# Import the required module

### Without adding this table in I can't seem to get it to test my code. Had to use ChatGPT to understand this and still struggling with the testing.

import pytest
from it_asset_reg import ITAsset, find_asset_by_record_number, get_valid_date, get_valid_imie

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
    # Test case for a record number input as a non-integer ('Dad')
    assets = setup_assets
    asset = find_asset_by_record_number(assets, 'Dad')
    assert asset is None

def test_get_valid_date_valid_format(monkeypatch):
    # Test valid date format
    date_str = "15.04.2023"
    
    # Mock input() function to return date_str
    monkeypatch.setattr('builtins.input', lambda _: date_str)
    
    # Call get_valid_date() which should return the validated date
    validated_date = get_valid_date()
    
    # Assert that the returned date matches the expected date_str
    assert validated_date == date_str

import pytest
from it_asset_reg import get_valid_imie

def test_get_valid_imie(monkeypatch):
    # Test valid IMIE number
    valid_input = "123456789012345"
    monkeypatch.setattr('builtins.input', lambda _: valid_input)
    validated_imie = get_valid_imie()
    assert validated_imie == int(valid_input)

    # Test invalid IMIE number (non-integer input)
    invalid_input = "not_an_integer"
    monkeypatch.setattr('builtins.input', lambda _: invalid_input)
    with pytest.raises(ValueError):
        get_valid_imie()

    # Test invalid IMIE number (empty input)
    empty_input = ""
    monkeypatch.setattr('builtins.input', lambda _: empty_input)
    with pytest.raises(ValueError):
        get_valid_imie()

