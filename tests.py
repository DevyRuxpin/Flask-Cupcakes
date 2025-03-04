from unittest import TestCase
from app import app
from models import db, Cupcake

# Use test database with postgres user/password from GitHub Actions
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/cupcakes_test'
app.config['SQLALCHEMY_ECHO'] = False
app.config['TESTING'] = True

# Create tables
db.drop_all()
db.create_all()

CUPCAKE_DATA = {
    "flavor": "TestFlavor",
    "size": "TestSize",
    "rating": 5,
    "image": "http://test.com/cupcake.jpg"
}

CUPCAKE_DATA_2 = {
    "flavor": "TestFlavor2",
    "size": "TestSize2",
    "rating": 10,
    "image": "http://test.com/cupcake2.jpg"
}

class CupcakeViewsTestCase(TestCase):
    """Tests for views of API."""

    def setUp(self):
        """Make demo data."""
        Cupcake.query.delete()
        cupcake = Cupcake(**CUPCAKE_DATA)
        db.session.add(cupcake)
        db.session.commit()
        self.cupcake = cupcake

    def tearDown(self):
        """Clean up fouled transactions."""
        db.session.rollback()

    # ... [rest of test methods remain the same] ...
