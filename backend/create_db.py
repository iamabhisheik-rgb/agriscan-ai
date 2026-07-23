from core.database import Base, engine
from models.user import User

print("Connecting to database and creating tables...")
Base.metadata.create_all(bind=engine)
print("Success! The 'users' table has been created.")