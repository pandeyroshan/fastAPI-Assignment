from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash(password):
    return pwd_cxt.hash(password)

def verify(request_password, hashed_password):
    return pwd_cxt.verify(request_password, hashed_password)