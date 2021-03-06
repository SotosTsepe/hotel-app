"""Guests table

Revision ID: 478ef4d8b2c7
Revises: 
Create Date: 2022-07-20 22:20:40.444965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '478ef4d8b2c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('guest',
    sa.Column('guest_id', sa.String(length=64), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=True),
    sa.Column('last_name', sa.String(length=20), nullable=True),
    sa.Column('patronymic', sa.String(length=20), nullable=True),
    sa.Column('gender', sa.String(length=20), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('member_since', sa.Date(), nullable=True),
    sa.Column('ssn_code', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=20), nullable=True),
    sa.Column('phone_number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('guest_id')
    )
    op.create_index(op.f('ix_guest_email'), 'guest', ['email'], unique=True)
    op.create_index(op.f('ix_guest_last_name'), 'guest', ['last_name'], unique=False)
    op.create_index(op.f('ix_guest_phone_number'), 'guest', ['phone_number'], unique=True)
    op.create_index(op.f('ix_guest_ssn_code'), 'guest', ['ssn_code'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_guest_ssn_code'), table_name='guest')
    op.drop_index(op.f('ix_guest_phone_number'), table_name='guest')
    op.drop_index(op.f('ix_guest_last_name'), table_name='guest')
    op.drop_index(op.f('ix_guest_email'), table_name='guest')
    op.drop_table('guest')
    # ### end Alembic commands ###
