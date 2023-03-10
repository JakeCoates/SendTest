# Send Test
I was provided with a test set out by Send and solve the problems provided in the `instructions.txt`

You can find my solution in `src/main.py`

I have been using the `tests` to the code and get the answers

## Setup:

```
poetry install
pytest -s
```



## Problem 1

For the first problem I was asked to take the inputs from text file `20000.txt` and determine the closest distance between `Nautilus` and `Nemo` and output the line number that `Nautilus` appears. it was a pretty fun problem to solve I found there were some interesting cases to solve for.

I decided to build some pytests around the application to help me test and find errors and edge cases.

I ended up building out some models to allow me to store some data to make it easier to manipulate

I also found that it ran relatively slowly at first so made some calculations to find the closest line distance to each occurance of the first word.

I also made it possible to query for different words

There is a possible edge case that I can forsee happening due to an optimisation I made around finding the closest line in relation to the main word. It could potentially have two lines a similar distance and just picks the first one which might not be correct. There are edge cases I would like to solve out here but it was outside of what I could justify doing.


---
ANSWER: "Nautilus" counts (case sensitive): 644

ANSWER: "Nemo" counts (case sensitive): 493

ANSWER: "Nautilus" counts (case insensitive): 649

ANSWER: "Nemo" counts (case insensitive): 509

ANSWER: Line (assumed starting at 1) 14017


---


## Problem 2
For the second problem I have been asked to find all the palindrome dates between two date ranges.

I also used pytest around the application to help me test the results.

I have made it possible to customise what dates you can check calculate between

It converts the date into the string format then uses a comparison of the string reverse stepped to check if it's a palindrome.

There is likely an edge case that exists as you could choose dates between 1820 and 2020 there will be some overlapped output, you could resolve this using a set but it was not the the instructions to deal with duplicated dates. 

---
ANSWER: 17 dates between 1st January 1970 and 31st December 2020

---
