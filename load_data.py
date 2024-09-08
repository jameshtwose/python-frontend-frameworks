# %%
from sqlalchemy import (
    create_engine,
    text,
    Column,
    Integer,
    String,
    DateTime,
    insert,
    Boolean
)
from sqlalchemy.orm import declarative_base
import pandas as pd

## Pgadmin connection settings
# - host: docker.for.mac.host.internal
# - port: 5433
# - user: postgres
# - password: changeme
# - database: postgres
# - schema: public

# %%
# postgresql+psycopg2://user:password@host:port/dbname
# psql -h localhost -p 5433 -U postgres -d postgres
host = "localhost"
engine = create_engine(
    f"postgresql+psycopg2://postgres:changeme@{host}:5433/postgres"
)

# %%
Base = declarative_base()


# identifierhash,type,country,language,socialnbfollowers,
# socialnbfollows,socialproductsliked,productslisted,
# productssold,productspassrate,productswished,
# productsbought,gender,civilitygenderid,civilitytitle,
# hasanyapp,hasandroidapp,hasiosapp,hasprofilepicture,
# dayssincelastlogin,seniority,seniorityasmonths,
# seniorityasyears,countrycode
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

# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# %%
users_df = pd.read_csv("data/6m_0k_99k_users_dataset_public.csv").dropna(
    subset=["identifierhash"]
).assign(
    **{"identifierhash": lambda x: x["identifierhash"].astype(str)}
).rename(
    columns={
        "identifierhash": "identifier_hash",
        "type": "type",
        "country": "country",
        "language": "language",
        "socialnbfollowers": "social_nb_followers",
        "socialnbfollows": "social_nb_follows",
        "socialproductsliked": "social_products_liked",
        "productslisted": "products_listed",
        "productssold": "products_sold",
        "productspassrate": "products_pass_rate",
        "productswished": "products_wished",
        "productsbought": "products_bought",
        "civiltygenderid": "civility_gender_id",
        "civilitytitle": "civility_title",
        "hasanyapp": "has_any_app",
        "hasandroidapp": "has_android_app",
        "hasiosapp": "has_ios_app",
        "hasprofilepicture": "has_profile_picture",
        "dayssincelastlogin": "days_since_last_login",
        "seniority": "seniority",
        "seniorityasmonths": "seniority_as_months",
        "seniorityasyears": "seniority_as_years",
        "countrycode": "country_code",
    }
)
# %%
with engine.begin() as conn:
    query = insert(Users)
    conn.execute(query, users_df.to_dict(orient="records"))
# %%
