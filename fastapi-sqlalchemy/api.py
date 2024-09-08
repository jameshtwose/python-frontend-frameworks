from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from models import Users, engine
from schemas import UserSchema
from sqlalchemy import select


app = FastAPI(
    title="FastAPI-SQLAlchemy",
    description="A simple FastAPI + SQLAlchemy example",
    version="0.1.0",
)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
async def root():
    """Root endpoint

    Parameters
    ----------
    None

    Returns
    -------
    dict
        A dict with a welcome message

    """
    return {"Hello": "Welcome to the FastAPI-SQLAlchemy API"}


@app.get("/users", tags=["Users"], response_model=list[UserSchema])
async def get_users(limit: int = 10, offset: int = 0):
    """Get users

    Parameters
    ----------
    limit : int, optional
        Number of records to return, by default 10
    offset : int, optional
        Number of records to skip, by default 0

    Returns
    -------
    list
        List of users

    """
    with engine.connect() as conn:
        stmt = select(Users).limit(limit).offset(offset)
        result = conn.execute(stmt)
    return [UserSchema.model_validate(row) for row in result]