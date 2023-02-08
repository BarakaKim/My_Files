def test_sum():
    """ Testing the function of adding number"""
    assert sum([1, 2, 3]) == 6, "The answer is 6"

def test_mult():
    assert mult([1, 2, 3]) == 13, "incorect"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")
