from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String,Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Needs(Base):
    __tablename__ = "needs"

    id = Column(Integer, primary_key=True)
    number = Column(String)
    title = Column(String)
    org_name = Column(String(2000))
    city_name = Column(String)
    province_name = Column(String)
    board_name = Column(String)
    jalali_send_deadline = Column(String)
    jalai_document_deadline = Column(String)
    is_sent = Column(Boolean,default=True)

    def __repr__(self):
        return self.number


engine = create_engine("sqlite:///sqlite.db", echo=True, future=True)
Base.metadata.create_all(engine)



