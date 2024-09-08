from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean
)
from sqlalchemy.orm import declarative_base

# use localhost when running from command line using
# uvicorn fastapi-sqlalchemy.api:app --reload --port 8080
# host = "localhost"
# use docker.for.mac.host.internal when running from docker
# docker compose up -d
host = "docker.for.mac.host.internal"
engine = create_engine(
    f"postgresql+psycopg2://postgres:changeme@{host}:5433/postgres"
)
Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    identifier_hash = Column(String, primary_key=True)
    type = Column(String, nullable=True)
    country = Column(String, nullable=True)
    language = Column(String, nullable=True)
    social_nb_followers = Column(Integer, nullable=True)
    social_nb_follows = Column(Integer, nullable=True)
    social_products_liked = Column(Integer, nullable=True)
    products_listed = Column(Integer, nullable=True)
    products_sold = Column(Integer, nullable=True)
    products_pass_rate = Column(Integer, nullable=True)
    products_wished = Column(Integer, nullable=True)
    products_bought = Column(Integer, nullable=True)
    gender = Column(String, nullable=True)
    civility_gender_id = Column(Integer, nullable=True)
    civility_title = Column(String, nullable=True)
    has_any_app = Column(Boolean, nullable=True)
    has_android_app = Column(Boolean, nullable=True)
    has_ios_app = Column(Boolean, nullable=True)
    has_profile_picture = Column(Boolean, nullable=True)
    days_since_last_login = Column(Integer, nullable=True)
    seniority = Column(Integer, nullable=True)
    seniority_as_months = Column(Integer, nullable=True)
    seniority_as_years = Column(Integer, nullable=True)
    country_code = Column(String, nullable=True)