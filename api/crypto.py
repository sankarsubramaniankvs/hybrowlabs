import bcrypt 
from cryptography.fernet import Fernet


class cryptography:
    def hash(password):
        return bcrypt.hashpw(password.encode(),bcrypt.gensalt())
    

    def check(password,hash):
        return bcrypt.checkpw(password.encode(),hash) 

    
    # def gen_key(self):
    #     key = Fernet.generate_key()
    #     print(key)

    def encrypt(item):
        key = b'kz6wJCv1egk9NgWTe8gQhptpQ-eSt6Jbf2JxtxquAW8='
        cipher_suite = Fernet(key)
        item = bytes(item,'utf-8')
        cipher_text = cipher_suite.encrypt(item)
        return cipher_text

    def decrypt(item):
        key = b'kz6wJCv1egk9NgWTe8gQhptpQ-eSt6Jbf2JxtxquAW8='
        cipher_suite = Fernet(key)
        plain_text = cipher_suite.decrypt(item) 
        return plain_text.decode('utf-8')


    
# c = cryptography()
# print(c.check('password',b'$2b$12$fZEdY/7YbMKxxJqga9EUC.MjFizYM16jxh7U0V331UY6Qi7qfWiFe'))


