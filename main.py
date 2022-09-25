from sqlalchemy.orm import sessionmaker
from Models import create_tables, engine

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()
    # create_tables(engine)


    session.close()