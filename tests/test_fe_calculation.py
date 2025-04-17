import unittest  # Importing the unittest module to create and run tests
from io import StringIO  # Importing StringIO to capture printed output
import sys  # Importing sys to modify standard output stream for capturing prints

# Import the estimate_fe function from the fe_calculation module
from fe_calculation import estimate_fe

class TestEstimateFe(unittest.TestCase):
    """
    Test class to verify the behavior of the estimate_fe function.
    This class includes tests for normal cases, edge cases, 
    and invalid inputs.
    """

    def test_zero_concentration(self):
        """
        Test case to verify the function returns 0.0 when the Fe concentration is zero.
        
        The input value of 75.074 corresponds to zero Fe concentration according to
        the estimation logic, so the output should be 0.0.
        """
        self.assertAlmostEqual(estimate_fe(75.074), 0.0, places=5)

    def test_half_concentration(self):
        """
        Test case to check if the function correctly computes Fe concentration at half (0.5).
        
        The input value of 77.482 corresponds to a Fe concentration of 0.5, 
        as calculated by the formula: V = 4.816 * 0.5 + 75.074.
        """
        self.assertAlmostEqual(estimate_fe(77.482), 0.5, places=5)

    def test_full_concentration(self):
        """
        Test case to check if the function correctly computes Fe concentration at full (1.0).
        
        The input value of 79.89 corresponds to a Fe concentration of 1.0, 
        as calculated by the formula: V = 4.816 * 1.0 + 75.074.
        """
        self.assertAlmostEqual(estimate_fe(79.89), 1.0, places=5)

    def test_negative_concentration(self):
        """
        Test case to handle negative Fe concentration results.
        
        This case checks if the function can return a negative concentration 
        when the input is sufficiently low. The result might be negative.
        """
        result = estimate_fe(70)
        self.assertLess(result, 0)  # Verify the result is less than 0 (negative)

    def test_invalid_input(self):
        """
        Test case to verify that the function raises a TypeError when given invalid input.
        
        Passing a non-numeric value (e.g., a string) should cause a TypeError to be raised.
        """
        with self.assertRaises(TypeError):
            estimate_fe("not a float")  # Invalid input

    def test_print_output(self):
        """
        Test case to capture and verify printed output from the function.
        
        This case verifies if the function correctly prints the expected output 
        when it is called, such as the string "estimated Fe concentration."
        """
        captured_output = StringIO()  # Create a StringIO object to capture printed output
        sys.stdout = captured_output  # Redirect stdout to the StringIO object
        estimate_fe(77.482)  # Call the function to generate the print output
        sys.stdout = sys.__stdout__  # Restore the original stdout
        self.assertIn("estimated Fe concentration", captured_output.getvalue())  # Verify the printed message

