from flask import Flask

app = Flask(__name__)
from app import account
from app import authorization
from app import search
from app import social
from app import tag
from app import visualization 