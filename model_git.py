from sqlalchemy import Column, Integer, String, Float, create_engine, ForeignKey, Table, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine("sqlite:///:memory:")
Base = declarative_base()


class Savininkas(Base):
    __tablename__ = 'savininkas'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    email = Column(String)


class NTurtas(Base):
    __tablename__ = 'nt'
    id = Column(Integer, primary_key=True)
    adresas = Column(String)
    plotas = Column(Float)
    nt_registras = Column(String)
    savininkas_id = Column(Integer, ForeignKey('savininkas.id'), nullable=False)
    savininkas = relationship('Savininkas', back_populates='turtai')


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
