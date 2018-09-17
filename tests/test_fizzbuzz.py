import pytest
from app import fizzbuzz

def isMultiple(value, mod):
    return (value % mod) == 0

def checkfizzBuzz(value, expectedRetVal):
    retVal = fizzbuzz.fizzBuzz(value)
    assert retVal == expectedRetVal

def test_fizzBuzz():
    fizzbuzz.fizzBuzz(1)

def test_fizzbuzzReturns1With1PassedIn():
    checkfizzBuzz(1, "1")

def test_fizzbuzzReturns2With2PassedIn():
    checkfizzBuzz(2, "2")

def test_fizzbuzzReturnsFizzWith3PassedIn():
    checkfizzBuzz(3, "Fizz")