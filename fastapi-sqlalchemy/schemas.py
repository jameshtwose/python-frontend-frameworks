from pydantic import BaseModel, ConfigDict

class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    identifier_hash: str
    type: str | None
    country: str | None
    language: str | None
    social_nb_followers: int | None
    social_nb_follows: int | None
    social_products_liked: int | None
    products_listed: int | None
    products_sold: int | None
    products_pass_rate: int | None
    products_wished: int | None
    products_bought: int | None
    gender: str | None
    civility_gender_id: int | None
    civility_title: str | None
    has_any_app: bool | None
    has_android_app: bool | None
    has_ios_app: bool | None
    has_profile_picture: bool | None
    days_since_last_login: int | None
    seniority: int | None
    seniority_as_months: int | None
    seniority_as_years: int | None
    country_code: str | None
    