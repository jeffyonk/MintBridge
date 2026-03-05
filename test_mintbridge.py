# test_mintbridge.py
"""
Tests for MintBridge module.
"""

import unittest
from mintbridge import MintBridge

class TestMintBridge(unittest.TestCase):
    """Test cases for MintBridge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MintBridge()
        self.assertIsInstance(instance, MintBridge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MintBridge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
