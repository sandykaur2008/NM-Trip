import sendgrid
import os
from flask import Flask
from config import Config
from flask_s3 import FlaskS3

app = Flask(__name__)
app.config.from_object(Config)
s3 = FlaskS3(app)
sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

from app import routes, errors