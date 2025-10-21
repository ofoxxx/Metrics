import pytest
from metrics.core import get_commits_per_day
from metrics.app import app
import pandas as pd

@pytest.mark.unit
def test_get_commits_per_day():
    # Mock API response and test data processing
    result = get_commits_per_day()
    assert isinstance(result, pd.DataFrame)
    assert 'commits' in result.columns
    assert 'day' in result.columns

@pytest.mark.unit
def test_dash_app():
    # Test Dash app layout and components
    assert app.layout is not None
