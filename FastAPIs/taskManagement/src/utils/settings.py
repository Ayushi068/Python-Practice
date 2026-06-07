#this file will contain the settings for our application.
#  We will use pydantic to manage our settings and environment variables. 
# This will allow us to easily load the settings from a .env file and access them throughout our application.

from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file = ".env",extra="ignore")
    #this will tell pydantic to look for the .env file in the root directory of our project and load the environment variables from it.

    DB_CONNECTION : str #this will be the connection string for our database. We will load it from the .env file.
    SECRET_KEY : str #this will be the secret key for our application. We will use it to sign our JWT tokens. We will load it from the .env file.
    ALGORITHM : str #this will be the algorithm we will use to sign our JWT tokens
    ACCESS_TOKEN_EXPIRE_MINUTES : int #this will be the expiration time for our JWT tokens in minutes. We will load it from the .env file.

settings = Settings()


