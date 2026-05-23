# SPDX-FileCopyrightText: 2015-2018 CERN.
# SPDX-License-Identifier: MIT

"""Helper functions for tests."""

from flask import url_for


def sign_up(app, client, email=None, password=None):
    """Register a user."""
    with app.test_request_context():
        register_url = url_for("security.register")

    res = client.post(
        register_url,
        data=dict(
            email=email or app.config["TEST_USER_EMAIL"],
            password=password or app.config["TEST_USER_PASSWORD"],
        ),
        environ_base={"REMOTE_ADDR": "127.0.0.1"},
    )
    assert res.status_code == 302  # redirect after signedup


def login(app, client, email=None, password=None):
    """Log the user in with the test client."""
    with app.test_request_context():
        login_url = url_for("security.login")

    res = client.post(
        login_url,
        data=dict(
            email=email or app.config["TEST_USER_EMAIL"],
            password=password or app.config["TEST_USER_PASSWORD"],
        ),
    )
    assert res.status_code == 302  # redirect after login
