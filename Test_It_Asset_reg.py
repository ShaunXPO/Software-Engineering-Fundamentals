#### Pytest automated testing for IT Asset reg

# Import the required module
import It_Asset_reg

# Define the test function
def test_get_valid_imie():
    # Arrange: Define the test input and expected output
    test_input = 123456789
    expected_output = 123456789  # Assuming the function returns the input if valid, modify if needed

    # Act: Call the function with the test input
    result = It_Asset_reg.get_valid_imie(test_input)

    # Assert: Verify the result matches the expected output
    assert result == expected_output
