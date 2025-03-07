import unittest
import subprocess

from simplemath import add, subtract


class TestOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, 2), 1)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(10, 10), 0)

    def test_script_execution(self):
        """Test running test_operations.py directly."""
        result = subprocess.run(
            ["python", "tests/test_operations.py"],
            capture_output=True,
            text=True
        )
        assert result.returncode == 0  # Ensure the script runs successfully

if __name__ == "__main__":
    unittest.main()
