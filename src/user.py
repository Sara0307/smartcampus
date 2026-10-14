import hashlib
import hmac
import os


class User:
    """Utilisateur SmartCampus avec mot de passe hache (jamais en clair)."""

    def __init__(self, email, password, active=True):
        self.email = email
        self.active = active
        self._salt = os.urandom(16)
        self._hash = self._hash_password(password)

    def _hash_password(self, password):
        return hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), self._salt, 100_000
        )

    def check_password(self, password):
        return hmac.compare_digest(self._hash, self._hash_password(password))