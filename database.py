from sqlalchemy import create_engine,text
from  sqlalchemy.orm import sessionmaker
from  dotenv import load_dotenv
import os
load_dotenv()


db_url=f"mysql+pymysql://{os.getenv('dbuser')}:{os.getenv('dbpassword')}@{os.getenv('dbhost')}:{os.getenv('dbport')}/{os.getenv('dbname')}"


# print("User:", os.getenv("dbuser"))
# print("Password:", os.getenv("password"))
# print("Host:", os.getenv("dbhost"))
# print("Port:", os.getenv("dbport"))
# print("DB Name:", os.getenv("dbname"))

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)

db= Session()

query=text("select * from user")

users=db=db.execute(query).fetchall()
print(users)