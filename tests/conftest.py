import sys
import os
import copy
import pytest
from fastapi.testclient import TestClient

# Ensure src is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import app as app_module

# Capture initial activities state for reset between tests
initial_activities = copy.deepcopy(app_module.activities)

@pytest.fixture(autouse=True)
def reset_activities():
    # Reset the in-memory activities before each test
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(initial_activities))
    yield

@pytest.fixture
def client():
    return TestClient(app_module.app)
