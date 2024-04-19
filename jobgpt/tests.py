from django.test import TestCase

from jobgpt.generator import generate_response


# Create your tests here.
def test_generate_response():
    try:
        generate_response("hello")
    finally:
        assert True
