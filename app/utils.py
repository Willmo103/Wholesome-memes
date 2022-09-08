from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# function to hash a users password
def password_hash(password: str):
    return pwd_context.hash(password)


#  simple check of the password input against the saved
def password_verify(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
