import pytest
from app import app
def test_app_exists():
    """Test that app exists"""
    assert app is not none

    def test_home_page():
        """Test the home page endpoint"""
        with app.test_client() as client:
            response = clent.get('/')
            assert response.status_code == 200