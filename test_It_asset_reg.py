### Automated Pytest testing

### pytest test_it_asset_reg.py

# Import the required module

import unittest
from it_asset_reg import ITAsset, find_asset_by_record_number
from it_asset_reg import ITAsset, get_valid_date

### Without adding this table in I can't seem to get it to test my code. Had to use ChatGPT to understand this and still struggling with the testing.

class TestITAssetReg(unittest.TestCase):
    def setUp(self):
        self.assets = [
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
    
    def test_find_asset_by_record_number_existing(self):
        # Test case for a record number that exists
        asset = find_asset_by_record_number(self.assets, 5)
        self.assertIsNotNone(asset)
        self.assertEqual(asset.record_number, 5)
        self.assertEqual(asset.item_name, "Monitor")
    
    def test_find_asset_by_record_number_non_existing(self):
        # Test case for a record number that does not exist
        asset = find_asset_by_record_number(self.assets, 12)
        self.assertIsNone(asset)
    
    def test_find_asset_by_record_number_alpha(self):
        # Test case for a record number that does not exist
        asset = find_asset_by_record_number(self.assets, Dad)
        self.assertIsNone(asset)


    def test_get_valid_date_valid_format(self):
        # Test valid date format
        date_str = "15.04.2023"
        with unittest.mock.patch('builtins.input', return_value=date_str):
            validated_date = get_valid_date()
        self.assertEqual(validated_date, date_str)
    
    def test_get_valid_date_invalid_format(self):
        # Test invalid date format (wrong separator)
        invalid_date_str = "15-04-2023"
        with unittest.mock.patch('builtins.input', side_effect=[invalid_date_str, "15.04.2023"]):
            validated_date = get_valid_date()
        self.assertEqual(validated_date, "15.04.2023")

    def test_get_valid_date_invalid_day(self):
        # Test invalid day value (32nd day)
        invalid_date_str = "32.04.2023"
        with unittest.mock.patch('builtins.input', side_effect=[invalid_date_str, "15.04.2023"]):
            validated_date = get_valid_date()
        self.assertEqual(validated_date, "15.04.2023")

    def test_get_valid_date_invalid_month(self):
        # Test invalid month value (13th month)
        invalid_date_str = "15.13.2023"
        with unittest.mock.patch('builtins.input', side_effect=[invalid_date_str, "15.04.2023"]):
            validated_date = get_valid_date()
        self.assertEqual(validated_date, "15.04.2023")

    def test_get_valid_date_invalid_year(self):
        # Test invalid year value (negative year)
        invalid_date_str = "15.04.-2023"
        with unittest.mock.patch('builtins.input', side_effect=[invalid_date_str, "15.04.2023"]):
            validated_date = get_valid_date()
        self.assertEqual(validated_date, "15.04.2023")