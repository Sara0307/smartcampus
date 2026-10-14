import logging

from .user import User

logger = logging.getLogger("smartcampus.security")

MSG_SUCCESS = "Connexion reussie"
MSG_INVALID = "Identifiants incorrects"
MAX_FAILURES = 3


class LoginService:
    def __init__(self):
        self._users = {}
        self._failures = {}

    def register(self, email, password, active=True):
        self._users[email] = User(email, password, active)

    def login(self, email, password):
        user = self._users.get(email)
        if user is None or not user.active or not user.check_password(password):
            self._record_failure(email)
            return False, MSG_INVALID
        self._failures[email] = 0
        return True, MSG_SUCCESS

    def _record_failure(self, email):
        count = self._failures.get(email, 0) + 1
        self._failures[email] = count
        if count >= MAX_FAILURES:
            logger.warning(
                "SECURITE: %d echecs consecutifs pour %s", count, email
            )