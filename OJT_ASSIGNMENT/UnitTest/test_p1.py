import pytest
@pytest.fixture(scope="function",autouse=True)
def myfixture():
    print("My Fixture is called")

def my_method1():
    print("my method 1 is called")

def my_method2():
    print("my method 2 is called")

def my_method3():
    print("my method 3 is called")

def my_method4():
    print("my method 4 is called")

