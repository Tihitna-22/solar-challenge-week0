"""
Tests to verify the development environment is set up correctly.
These tests ensure all required packages are installed and can be imported.
"""

import sys
import pytest


def test_python_version():
    """Test that Python version is 3.11 or higher."""
    assert sys.version_info >= (3, 11), f"Python 3.11+ required, got {sys.version_info}"


def test_import_pandas():
    """Test that pandas can be imported."""
    import pandas as pd
    assert pd.__version__ is not None


def test_import_numpy():
    """Test that numpy can be imported."""
    import numpy as np
    assert np.__version__ is not None


def test_import_matplotlib():
    """Test that matplotlib can be imported."""
    import matplotlib
    assert matplotlib.__version__ is not None


def test_import_seaborn():
    """Test that seaborn can be imported."""
    import seaborn as sns
    assert sns.__version__ is not None


def test_import_streamlit():
    """Test that streamlit can be imported."""
    import streamlit
    assert streamlit.__version__ is not None


def test_import_jupyter():
    """Test that jupyter can be imported."""
    import jupyter
    assert jupyter.__version__ is not None


def test_pandas_dataframe_creation():
    """Test basic pandas functionality."""
    import pandas as pd
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    assert len(df) == 3
    assert list(df.columns) == ['a', 'b']


def test_numpy_array_creation():
    """Test basic numpy functionality."""
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5])
    assert arr.shape == (5,)
    assert arr.sum() == 15

