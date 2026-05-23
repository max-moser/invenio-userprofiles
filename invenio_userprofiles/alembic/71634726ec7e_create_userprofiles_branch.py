# SPDX-FileCopyrightText: 2016-2018 CERN.
# SPDX-License-Identifier: MIT

"""Create userprofiles branch."""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "71634726ec7e"
down_revision = None
branch_labels = ("invenio_userprofiles",)
depends_on = "dbdbc1b19cf2"


def upgrade():
    """Upgrade database."""


def downgrade():
    """Downgrade database."""
