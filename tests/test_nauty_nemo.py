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

    closest_distance = problem.determine_distance("Nautilus", "Nemo")
    mylogger.info(f"closest line no: {closest_distance.line_no + 1}")
    
 