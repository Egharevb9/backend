from sqlalchemy import create_engine,text
from  sqlalchemy.orm import sessionmaker
from  dotenv import load_dotenv
from pymysql.constants import CLIENT
import os
load_dotenv()


db_url=f"mysql+pymysql://{os.getenv('dbuser')}:{os.getenv('dbpassword')}@{os.getenv('dbhost')}:{os.getenv('dbport')}/{os.getenv('dbname')}"




# print("User:", os.getenv("dbuser"))
# print("Password:", os.getenv("password"))
# print("Host:", os.getenv("dbhost"))
# print("Port:", os.getenv("dbport"))
# print("DB Name:", os.getenv("dbname"))

engine = create_engine(
    db_url,
connect_args={"client_flag": CLIENT.MULTI_STATEMENTS}
)

Session = sessionmaker(bind=engine)

db= Session()

create_tables_query =text("""
create table if not EXISTS users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
    );
                          
create table if not EXISTS courses(
    id INT AUTO_INCREMENT PRIMARY KEY,
    TITLE VARCHAR(100) NOT NULL,
    level VARCHAR(100) NOT NULL 
    );
create table if not EXISTS enrollments(
    id INT AUTO_INCREMENT PRIMARY KEY,
    userId INT,
    courseId INT,
    FOREIGN KEY(userId) REFERENCES users(id),
    FOREIGN KEY(courseId) REFERENCES courses(id)
      );
""")
db.execute(create_tables_query)
print("Table has been  created successfully")


# query=text("select * from user")

# users=db=db.execute(query).fetchall()
# print(users)