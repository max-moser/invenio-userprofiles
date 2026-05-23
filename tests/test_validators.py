# SPDX-FileCopyrightText: 2015-2018 CERN.
# SPDX-License-Identifier: MIT

"""Tests for user profile validators."""

import pytest
from invenio_accounts.utils import validate_username

test_usernames = {
    "valid": "Good-Name_9",
    "invalid_begins_with_number": "9CantStartWithNumber",
    "invalid_characters": "_Containsi!!ega!Char acters*",
    "invalid_short": "ab",
}


def test_validate_username(app):
    """Test username validator."""
    # Goodname can contain letters, numbers and starts with a letter
    validate_username(test_usernames["valid"])

    # Can't start with a number
    with pytest.raises(ValueError):
        validate_username(test_usernames["invalid_begins_with_number"])

    # Can only contain latin letters and numbers
    with pytest.raises(ValueError):
        validate_username(test_usernames["invalid_characters"])

    with pytest.raises(ValueError):
        validate_username(test_usernames["invalid_short"])
