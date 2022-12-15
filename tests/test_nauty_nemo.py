import logging

import pytest
from src.main import problem_1

logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()

def test_problem_1():
    problem = problem_1('inputs/20000.txt')
    results = problem.count_words(["Nautilus", "Nemo"])
    mylogger.info(f"Count of Nautilus's: {len(results['Nautilus'])}")
    mylogger.info(f"Count of Nemos: {len(results['Nemo'])}")

    closest, distance = problem.determine_distance("Nautilus", "Nemo")
    mylogger.info(f"closest line no: {closest.line_no + 1} with a character difference of {distance}")
    assert closest is not None
    assert distance > 0

def test_problem_1_other_words():
    problem = problem_1('inputs/20000.txt')
    results = problem.count_words(["Other", "Word"])
    mylogger.info(f"Count of Other's: {len(results['Other'])}")
    mylogger.info(f"Count of Word: {len(results['Word'])}")

    closest, distance = problem.determine_distance("Other", "Word")
    mylogger.info(f"closest line no: {closest.line_no + 1} with a character difference of {distance}")
    assert closest is not None
    assert distance > 0
    
def test_problem_1_other_words_compare_case_chec():
    case_sensitive = problem_1('inputs/20000.txt')
    case_sensitive.count_words(["Other", "Word"])

    case_sensitive_closest, case_sensitive_distance = case_sensitive.determine_distance("Other", "Word")
    
    case_insensitive = problem_1('inputs/20000.txt', match_case=False)
    case_insensitive.count_words(["Other", "Word"])
    case_insensitive_closest, case_insensitive_distance = case_insensitive.determine_distance("Other", "Word")
    
    assert case_sensitive_closest != case_insensitive_closest
    assert case_sensitive_distance != case_insensitive_distance

def test_problem_1_unfound_words():
    with pytest.raises(Exception) as exception:
        problem = problem_1('inputs/20000.txt')
        problem.count_words(["Fizz", "Blah"])
        problem.determine_distance("Fizz", "Blah")

    assert str(exception.value) == "One or more words not found"

def test_problem_1_missing_file():
    with pytest.raises(Exception) as exception:
        problem_1('inputs/DOESNOTEXIST.txt')

    assert str(exception.value) == "file does not exist"

def test_problem_1_invalid_file_type():
    with pytest.raises(Exception) as exception:
        problem_1('inputs/20000.json')

    assert str(exception.value) == "invalid file type"

