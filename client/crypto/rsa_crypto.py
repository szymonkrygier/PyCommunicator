# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
import base64

from Crypto.PublicKey import RSA

from Crypto.Cipher import PKCS1_OAEP


class RSACrypto:
    @staticmethod
    def generate_keys():
        keys = RSA.generate(2048)

        private_key = keys.exportKey()
        public_key = keys.public_key().exportKey()

        return public_key, private_key

    @staticmethod
    def decrypt(data, private_key):
        imported_private_key = RSA.importKey(private_key)
        pkcs = PKCS1_OAEP.new(imported_private_key)
        decrypted_text = pkcs.decrypt(base64.standard_b64decode(data.encode()))

        return decrypted_text

    @staticmethod
    def encrypt(data, public_key):
        imported_public_key = RSA.importKey(public_key)
        pkcs = PKCS1_OAEP.new(imported_public_key)
        encrypted_text = pkcs.encrypt(data)

        return base64.standard_b64encode(encrypted_text).decode()
