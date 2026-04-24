import os
import pytest
from config import REQUIRED_VARS

def test_all_required_vars_present():
    """Verify CI runner has all required vars configured."""
    for var in REQUIRED_VARS:
        assert os.environ.get(var), f"{var} is not set"