import sendgrid
import os
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

from app import routes, errors