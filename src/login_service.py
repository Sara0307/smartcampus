from .user import User

MSG_SUCCESS = "Connexion reussie"
MSG_INVALID = "Identifiants incorrects"


class LoginService:
    def __init__(self):
        self._users = {}

    def register(self, email, password, active=True):
        self._users[email] = User(email, password, active)

    def login(self, email, password):
        user = self._users.get(email)
        if user is None or not user.active or not user.check_password(password):
            return False, MSG_INVALID
        return True, MSG_SUCCESS