from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import User, Base, CatalogItem, Categories

engine = create_engine('sqlite:///catalogwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

User2 = User(name="Meya G", email="mg@udacity.com",
             picture='https://plus.google.com/u/1/photos/114888950754511941808/albums/profile/6335022156608751730')
session.add(User2)
session.commit()

# create a category
makeup = Categories(user_id=1, name="Makeup")

session.add(makeup)
session.commit()

skin = Categories(user_id=1, name="Skin Care")

session.add(skin)
session.commit()

hair = Categories(user_id=1, name="Hair care")

session.add(hair)
session.commit()

item2 = CatalogItem(user_id=1, name="Too Faced Mascara", description="Too Faced: Better than sex mascara",
                     price="$23.00", category=makeup)

session.add(item2)
session.commit()


item2 = CatalogItem(user_id=1, name="NARS Blush", description="Shimmery blush",
                     price="$24.00", category=makeup)

session.add(item2)
session.commit()

item2 = CatalogItem(user_id=1, name="Clinique", description="Moisture surge extended",
                     price="$29.99", category=skin)

session.add(item2)
session.commit()

item2 = CatalogItem(user_id=1, name="Tatcha", description="The water cream",
                     price="$68.00", category=skin)

session.add(item2)
session.commit()

item2 = CatalogItem(user_id=1, name="Alterna Haircare", description="10-in-1 complete correction",
                     price="$68.00", category=hair)

session.add(item2)
session.commit()

item2 = CatalogItem(user_id=1, name="Bumble and Bumble oil", description="Invisible oil primer",
                     price="$68.00", category=hair)

session.add(item2)
session.commit()
