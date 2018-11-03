#!/usr/bin/env python

from flask import Flask, render_template, request, redirect, jsonify, url_for, flash

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

from flask import session as login_session
import random
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests


app = Flask(__name__)


# Connect to Database and create database session
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()


# Show all restaurants
@app.route('/')
@app.route('/home/')
def home():
    categories = session.query(Category).order_by(Category.name)
    return render_template('home.html', categories=categories)


@app.route('/categories/JSON')
@app.route('/JSON')
def category_json():
    categories = session.query(Category).all()
    return jsonify(categories=[category.serialize for category in categories])

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)