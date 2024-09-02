from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import datetime

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  
    username = Column(String, unique=True, nullable=False)
    points = Column(Integer, default=0)
    first_login = Column(DateTime, nullable=True)  
    last_login = Column(DateTime, default=datetime.datetime.now) 
    
    boosts = relationship('Boost', back_populates='player')
    
    def __init__(self, username):
        self.username = username
        self.first_login = None  

    def record_login(self):
        if self.first_login is None:
            self.first_login = datetime.datetime.now()  
        self.last_login = datetime.datetime.now()  
        self.points += 1  

    def add_boost(self, boost):
        self.boosts.append(boost)


class Boost(Base):
    __tablename__ = 'boosts'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  
    player_id = Column(Integer, ForeignKey('players.id'), nullable=False)
    type = Column(String, nullable=False)
    duration = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now) 
    
    player = relationship('Player', back_populates='boosts')
    
    def __init__(self, player, boost_type, duration):
        self.player = player
        self.type = boost_type
        self.duration = duration

engine = create_engine('sqlite:///game2.db')  
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


try:
    new_player = Player(username='gamer923')
    session.add(new_player)
    session.commit()

   
    new_player.record_login()
    session.commit()


    new_boost = Boost(player=new_player, boost_type='double points', duration=1800)
    session.add(new_boost)  
    new_player.add_boost(new_boost) 
    session.commit()

except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    session.close()
