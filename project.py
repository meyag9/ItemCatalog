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
    category = session.query(Categories).all()
    return render_template('showall.html', category = category) #add some styling

@app.route('/newCategory', methods=['GET','POST'])
def newCategory(): #display database content
    if request.method == 'POST':
        newItem = Categories(user_id=1, name = request.form['name'])
        session.add(newItem)
        session.commit()
        return redirect(url_for('showCategories'))
    else:
        return render_template('newCategory.html')

@app.route('/<string:item_name>/description')
# display information of a item that was clicked
def itemDescription(item_name):
    itemToDisplay = session.query(
        CatalogItem).filter_by(name=item_name)
    return render_template('description.html', d=itemToDisplay)




@app.route('/editCatalogItem')
def editCatalogItem(): #display database content
    return render_template('editCatalogItem.html')

@app.route('/deleteCatalogItem')
def deleteCatalogItem(): #display database content
    return render_template('deleteCatalogItem.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
