from passlib.context import CryptContext

passwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)


def generate_passwd_hash(password:str)->str:
    hash=passwd_context.hash(password)
    return hash

def verify_password(password:str,hashed_pass:str)->bool:
    return passwd_context.verify(password,hashed_pass)
