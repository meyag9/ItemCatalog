from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import User, Base, CatalogItem, Categories
from flask import session as login_session
import json
from flask import make_response

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///catalogwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/main')
def showCategories(): #display database content
    category = session.query(CatalogItem).all()
    return render_template('showall.html',category = category) #add some styling

@app.route('/newCatalogItem', methods=['GET','POST'])
def HelloWorld(): #display database content
    category = session.query(Categories).all()
    #items = session.query(Categories).all()
    output = ''
    for i in category:
        output += i.name
        output += '</br>'
    #return output
    return render_template('showall.html',category = category)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
