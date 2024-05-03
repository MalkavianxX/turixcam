from firebase_admin import auth, exceptions

class FireUser:
    def __init__(self, uid=None, email=None, password=None, display_name=None, photo_url=None):
        self.uid = uid
        self.email = email
        self.password = password
        self.display_name = display_name
        self.photo_url = photo_url

    @classmethod
    def from_auth_user(cls, user):
        return cls(user.uid, user.email, display_name=user.display_name, photo_url=user.photo_url)

    @classmethod
    def all(cls):
        try:
            return [cls.from_auth_user(user) for user in auth.list_users().iterate_all()]
        except exceptions.FirebaseError as e:
            print("Error al obtener todos los usuarios: ", e)
            return []

    @classmethod
    def filter(cls, **kwargs):
        try:
            users = cls.all()
            for key, value in kwargs.items():
                users = [user for user in users if getattr(user, key, None) == value]
            return users
        except exceptions.FirebaseError as e:
            print("Error al filtrar los usuarios: ", e)
            return []

    @classmethod
    def get(cls, uid):
        try:
            user = auth.get_user(uid)
            return cls.from_auth_user(user)
        except exceptions.FirebaseError as e:
            print(f"Error al obtener el usuario con uid={uid}: ", e)
            return None

    @classmethod
    def get_by_email(cls, email):
        try:
            users = cls.filter(email=email)
            if users:
                return users[0]
            else:
                return None
        except exceptions.FirebaseError as e:
            print(f"Error al obtener el usuario con email={email}: ", e)
            return None

    def save(self):
        try:
            if self.uid is None:
                user = auth.create_user(email=self.email, password=self.password)
                self.uid = user.uid
            else:
                auth.update_user(self.uid, email=self.email)
        except exceptions.FirebaseError as e:
            print("Error al guardar el usuario: ", e)
