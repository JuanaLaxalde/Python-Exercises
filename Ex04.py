#  Write a program to prompt for a score between 0.0 and 1.0. If the score is out
#  of range, print an error. If the score is between 0.0 and 1.0, print a grade using the
#  following table:
#  >= 0.9 A
#  >= 0.8 B
#  >= 0.7 C
#  >= 0.6 D
#  < 0.6 F
#  If the user enters a value out of range, print a suitable error message and exit. For
#  the test, enter a score of 0.85.

score = input("Enter Score: ")
ip = float(score)
if ip < 0.6:
    print("Error")
elif ip > 0.9:
    print("Error")
elif ip >= 0.9:
    print("A")
elif ip >= 0.8:
    print("B")
elif ip >= 0.7:
    print("C")
elif ip >= 0.6:
    print("D")
elif ip < 0.6:
    print("F")
