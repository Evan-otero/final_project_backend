"""empty message

Revision ID: d19ba195d644
Revises: b3c63ec5657b
Create Date: 2019-11-19 19:49:29.967737

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd19ba195d644'
down_revision = 'b3c63ec5657b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('password', sa.String(length=20), nullable=False),
    sa.Column('image', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('address', sa.String(length=80), nullable=False),
    sa.Column('lat', sa.String(length=20), nullable=False),
    sa.Column('log', sa.String(length=20), nullable=False),
    sa.Column('ratings', sa.String(length=20), nullable=False),
    sa.Column('fenced', sa.String(length=250), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address')
    )
    op.drop_index('email', table_name='users')
    op.drop_index('username', table_name='users')
    op.drop_table('users')
    op.drop_index('address', table_name='locations')
    op.drop_table('locations')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('locations',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('address', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('lat', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('log', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('ratings', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('fenced', mysql.VARCHAR(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('address', 'locations', ['address'], unique=True)
    op.create_table('users',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('password', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('image', mysql.VARCHAR(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('username', 'users', ['username'], unique=True)
    op.create_index('email', 'users', ['email'], unique=True)
    op.drop_table('location')
    op.drop_table('user')
    # ### end Alembic commands ###