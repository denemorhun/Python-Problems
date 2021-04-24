import pytest

# to run all tests: py.test

@pytest.mark.set1
def test_file1_method1():
    x = 5
    y = 6

    assert x+1 == 6, "Fail: Sum not correct"
    assert x == y, "Fail: Value's don't match"

# to only run this test: py.test test_sample1.py::test_file2_method2 

@pytest.mark.set1
def test_file2_method2():
    x = 5
    y = 6

    assert x + 1 == y, "test failed"
