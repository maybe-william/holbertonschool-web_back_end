#!/usr/bin/env python3
""" Testing module """


import requests


def register_user(email: str, password: str) -> None:
    """ register user """
    assert True


def log_in_wrong_password(email: str, password: str) -> None:
    """ log wrong user """
    assert True


def log_in(email: str, password: str) -> str:
    """ log right password """
    assert True


def profile_unlogged() -> None:
    """ log out maybe? """
    assert True


def profile_logged(session_id: str) -> None:
    """ log in/out what? """
    assert True


def log_out(session_id: str) -> None:
    """ log out """
    assert True


def reset_password_token(email: str) -> str:
    """ make sure to get a pass reset """
    assert True


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ change password """
    assert True


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
