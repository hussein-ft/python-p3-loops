"""Tests for looping-related functions."""

from lib.looping import happy_new_year, square, square_integers, fizzbuzz

def test_happy_new_year(capsys):
    """Test the happy_new_year function."""
    happy_new_year()
    captured = capsys.readouterr()
    output = captured.out.strip().split("\n")
    assert output[:10] == [str(i) for i in range(10, 0, -1)], "Countdown is incorrect"
    assert output[-1] == "Happy New Year!", "Final message is incorrect"

def test_square():
    """Test the square function."""
    assert square([1, 2, 3]) == [1, 4, 9], "Square of numbers is incorrect"
    assert square([]) == [], "Square of an empty list should be an empty list"
    assert square([-1, -2, -3]) == [1, 4, 9], "Square of negative numbers is incorrect"

def test_square_integers():
    """Test the square_integers function."""
    assert square_integers([1, 2, 3]) == [1, 4, 9], "Square of integers is incorrect"
    assert square_integers([]) == [], "Square of an empty list should be an empty list"
    assert square_integers([-1, -2, -3]) == [1, 4, 9], "Square of negative integers is incorrect"

def test_fizzbuzz(capsys):
    """Test the fizzbuzz function."""
    fizzbuzz()
    captured = capsys.readouterr()
    output = captured.out.strip().split("\n")
    for i, line in enumerate(output, start=1):
        if i % 15 == 0:
            assert line == "FizzBuzz", f"Should have printed 'FizzBuzz' for {i}, got {line}"
        elif i % 3 == 0:
            assert line == "Fizz", f"Should have printed 'Fizz' for {i}, got {line}"
        elif i % 5 == 0:
            assert line == "Buzz", f"Should have printed 'Buzz' for {i}, got {line}"
        else:
            assert line == str(i), f"Should have printed {i}, got {line}"
    assert len(output) == 100, f"FizzBuzz should have printed 100 lines, got {len(output)}"
