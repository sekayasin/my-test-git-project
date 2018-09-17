import pytest
from app import fizzbuzz

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

def test_fizzbuzzReturnsBuzzWith5PassedIn():
    checkfizzBuzz(5, "Buzz")

def test_fizzbuzzReturnsFizzWith6PassedIn():
    checkfizzBuzz(6, "Fizz")

def test_fizzbuzzReturnsBuzzWith10PassedIn():
    checkfizzBuzz(10, "Buzz")

def test_fizzbuzzReturnsFizzBuzzWith15PassedIn():
    checkfizzBuzz(15, "FizzBuzz")