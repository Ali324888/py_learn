class AgeError(Exception):
    pass

age = 16

try:
    if age < 18:
        raise AgeError("You must be 18 or older")

    print("Eligible")

except AgeError as error:
    print(error)


class InvalidMarksError(Exception):
    pass


def set_marks(marks):
    try:
        if marks < 0 or marks > 100:
            raise InvalidMarksError("Invalid Marks")
        print("Marks Saved")

    except InvalidMarksError as error:
        print(error)

set_marks(105)

class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    try:
        if amount < 0 : 
            raise InsufficientBalanceError("Invalid Amount")
        elif amount > balance:
            raise InsufficientBalanceError("Insufficient balance")
        else:
            print("Withdraw successfully")
    except InsufficientBalanceError as error:
        print(error)

withdraw(1500, 2000)


class InvalidAgeError(Exception):
    pass

class InvalidMarksError(Exception):
    pass

def register_student(name, age, marks):
    try: 
        if age < 18:
            raise InvalidAgeError("You must be 18 or older")

        if marks < 0 or marks > 100:
            raise InvalidMarksError("Invalid Marks")

        print("Student registered successfully")
        print("Name: ", name)
        print("Age: ", age)
        print("Marks: ", marks)

    except InvalidAgeError as error:
        print(error)

    except InvalidMarksError as error:
        print(error)

register_student("adil", 19, 165)