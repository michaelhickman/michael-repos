# michael-repos
number to words task

## Assumptions:
+ If a line of text contains more than one number, it is invalid
+ If a number contains a special character, it is invalid
+ The largest number that can be considered valid is 999999999999999

## Design Choices:
+ The tuple 'UNIT' contains the string of number less than 20. The first 20 integers maps to this tuple
+ The tuple 'TENS' contains string of the multiples of 10s. When considering a three digit number, the second digit maps to this tuple
+ The tuple 'THOUSANDS' contains the string of 1000<sup>n</sup> where n is an integer. The index from the first enumerate maps to this tuple
+ The index of the second enumerate is used to decide where to place the commas and the "and"

## Instructions:
+ Change the path of the text file to the correct path
+ To run the progam, run python number_to_words.py
+ To run the test, run python test.py

## Test Output:

![](/images/TestProof.png)
