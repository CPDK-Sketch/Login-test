from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_USER = "your_db_user"
DB_PASSWORD = "your_password"
DB_HOST = "your-db-instance.rds.amazonaws.com"
DB_PORT = "3306"
DB_NAME = "yourdbname"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
