import datetime
import logging

from src.main import problem_2

logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()

def test_problem_2():
    problem = problem_2(datetime.datetime(1970, 1, 1), datetime.datetime(2021, 12, 31))
    mylogger.info(f"Count of palindromes: {problem.get_palindrome_count()}")
    assert problem.get_palindrome_count() > 0
    
def test_problem_2_not_palindrome():
    problem = problem_2(datetime.datetime(2000, 1, 1), datetime.datetime(2000, 1, 1))
    assert problem.get_palindrome_count() == 0
    
def test_problem_2_represent_with_leading_zero():
    problem = problem_2(datetime.datetime(2000, 1, 1), datetime.datetime(2000, 1, 1))
    assert problem.dates[0] == '010100'
    
def test_problem_2_str_length():
    problem = problem_2(datetime.datetime(1970, 1, 1), datetime.datetime(2021, 12, 31))
    longer_strings = [date for date in problem.dates if len(date) > 6]
    shorter_strings = [date for date in problem.dates if len(date) < 6]
    assert len(longer_strings) == 0
    assert len(shorter_strings) == 0
