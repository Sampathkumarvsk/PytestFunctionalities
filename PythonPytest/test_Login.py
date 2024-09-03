import pytest

@pytest.fixture()
def setup():
    print("Launching the Browser")
    print("Logging in to website")
    yield
    print("logoff")
    print("close the browser")

def testlogin_test(setup):
    print("Login Passed")







def testloginout_test(setup):
    print("Logout Passed")
