import math
import pytest

@pytest.fixture
def input_value():
   num = 33
   return num

@pytest.mark.others
def test_less(input_value):
   assert input_value < 200


## pytest -m others -v
## pytest -k divisible -v