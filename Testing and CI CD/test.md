# Testing django

To run test in django see https://docs.djangoproject.com/en/5.0/topics/testing/overview/

1. Create a class in the `tests.py` file in the app folder you want to test
2. The class has to have a proper name and the `setUp` and `test_*` functions as well.
3. `setUp(self)` is used to create the objects that will be used in the tests
4. `test_*(self)` is used to test the functionality of the app
5. Finally, you can run `./manage.py test app_name.tests` to run the tests
 for that particular app.
6. Output after running the command:
```bash
Found 5 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.023s

OK
Destroying test database for alias 'default'...
```

Example of test file:

```python
from django.test import TestCase

from .models import Airport, Flight

# Create your tests here.
class FlightTestCase(TestCase):

    def setUp(self):

        # Create airports.
        a1 = Airport.objects.create(code="AAA", city="City A")
        a2 = Airport.objects.create(code="BBB", city="City B")

        # Create flights.
        Flight.objects.create(origin=a1, destination=a2, duration=100)
        Flight.objects.create(origin=a1, destination=a1, duration=200)
        Flight.objects.create(origin=a1, destination=a2, duration=-100)

    def test_departures_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.departures.count(), 3)

    def test_arrivals_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.arrivals.count(), 1)
```


## VIEW airline/flights/tests.py app

# Selenium

Serves the purpose of simulating a web browser. It is used to test the functionality of the website.

