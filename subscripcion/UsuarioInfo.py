from django.conf import settings      

class DoesNotExist(Exception):
    pass

class User:
    def __init__(self, id=None, **kwargs):
        self.collection = settings.DB.collection('Usuarios')
        self.id = id
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def all(cls):
        collection = settings.DB.collection('Usuarios')
        return [cls(**{**doc.to_dict(), 'id': doc.id}) for doc in collection.get()]

    @classmethod
    def filter(cls, **kwargs):
        collection = settings.DB.collection('Usuarios')
        query = collection
        for k, v in kwargs.items():
            query = query.where(k, '==', v)
        return [cls(**{**doc.to_dict(), 'id': doc.id}) for doc in query.get()]

    @classmethod
    def get(cls, **kwargs):
        docs = cls.filter(**kwargs)
        if len(docs) > 0:
            return docs[0]
        else:
            raise DoesNotExist("Document does not exist")

    def save(self):
        # Copia el diccionario de atributos
        data = self.__dict__.copy()
        # Elimina el atributo 'collection'
        data.pop('collection', None)
        if self.id:
            doc_ref = self.collection.document(self.id)
            doc_ref.set(data)
        else:
            doc_ref = self.collection.document()
            doc_ref.set(data)
            self.id = doc_ref.id

    def update(self, **kwargs):
        if self.id:
            doc_ref = self.collection.document(self.id)
            doc_ref.update(kwargs)
            for k, v in kwargs.items():
                setattr(self, k, v)

    def delete(self):
        if self.id:
            doc_ref = self.collection.document(self.id)
            doc_ref.delete()

    @classmethod
    def exists(cls, **kwargs):
        try:
            cls.get(**kwargs)
            return True
        except DoesNotExist:
            return False
        
    def toJson(self):
        # Copia el diccionario de atributos
        data = self.__dict__.copy()
        # Elimina el atributo 'collection'
        data.pop('collection', None)
        return data
