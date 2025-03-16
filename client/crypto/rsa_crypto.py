# PyCommunicator
# Copyright (C) 2022-2025 Szymon Krygier <szymon.krygier@pulsax.pl>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
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
