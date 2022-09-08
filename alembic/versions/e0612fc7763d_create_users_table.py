"""create 'users' table

Revision ID: e0612fc7763d
Revises: 
Create Date: 2022-09-07 20:21:30.242641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0612fc7763d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                  server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email")
    )


def downgrade() -> None:
    op.drop_table("users")
