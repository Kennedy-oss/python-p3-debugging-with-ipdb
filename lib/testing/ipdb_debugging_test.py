#!/usr/bin/env python3

from ipdb_debugging import plus_two

class TestIpdbDebugging:
    def test_adds_two(self):
        """Test that plus_two adds 2 to its input argument."""
        assert plus_two(3) == 5
