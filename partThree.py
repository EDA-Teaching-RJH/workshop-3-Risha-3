score = int(input("What score did you get? "))
if 90 <= score <= 100:
    print("Grade A")
elif 80 <= score < 90:
    print("Grade B")
elif 70 <= score < 80:
    print("Grade C")
elif 60 <= score < 70:
    print("Grade D")
elif 0 <= score < 60:
    print("Input must be a number from 1-100. PLease try again.")
