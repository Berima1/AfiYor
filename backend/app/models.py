from sqlalchemy import Table, Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from .database import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(200), nullable=False),
    Column("email", String(200), unique=True, nullable=False, index=True),
    Column("country", String(100), default="ghana"),
    Column("industry", String(100), default="general"),
    Column("created_at", DateTime, server_default=func.now())
)

conversations = Table(
    "conversations",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", String(100), index=True),
    Column("query", Text),
    Column("response", Text),
    Column("country", String(100)),
    Column("industry", String(100)),
    Column("confidence", String(10), default="0.9"),
    Column("created_at", DateTime, server_default=func.now())
)
