import pytest
from app import fizzbuzz

def checkfizzBuzz(value, expectedRetVal):
    retVal = fizzbuzz.fizzBuzz(value)
    assert retVal == expectedRetVal

def test_fizzBuzz():
    fizzbuzz.fizzBuzz(1)

def test_fizzbuzzReturns1With1PassedIn():
    checkfizzBuzz(1, "1")