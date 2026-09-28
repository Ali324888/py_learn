from student_marks import is_passing

def test_passing_student():
    assert is_passing(40) == True


def test_failing_student():
    assert is_passing(30) == False