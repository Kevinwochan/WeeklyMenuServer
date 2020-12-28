from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection
from app.utils.Singleton import Singleton


class MongoDB(Singleton):
    client: AsyncIOMotorClient = None

    @classmethod
    def connect(cls):
        cls.client = AsyncIOMotorClient(
            'mongodb+srv://MONGOPWD:MONGOPWD@cluster0.rhkkj.mongodb.net/HelloFresh?retryWrites=true&w=majority')

    @classmethod
    def disconnect(cls):
        cls.client.close()

    @classmethod
    def get_client(cls) -> AsyncIOMotorClient:
        if cls.client is None:
            cls.connect()
        return cls.client

    @classmethod
    def get_database(cls, db_name: str) -> AsyncIOMotorDatabase:
        return cls.get_client().get_database(name=db_name)

    @classmethod
    def get_collection(cls, db_name: str, collection_name: str) -> AsyncIOMotorCollection:
        return cls.get_database(db_name).get_collection(collection_name)
