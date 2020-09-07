from flask import Flask, request, jsonify
import requests
import os
import tester
from tester import Scraper
from rq import Queue
from rq.job import Job
from red import conn
from rq import Retry


# Initialize App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
q = Queue(connection=conn)

# Run Downloader
@app.route('/run')
def run():
    job = q.enqueue(tester.run, retry=Retry(max=5, interval=5))
    print(job.get_id())
    return 'OK'

@app.route('/run2')
def run_stack():
    job = q.enqueue(Scraper().getStackOverflow, retry=Retry(max=5, interval=5))
    print(job.get_id())
    return 'OK'

@app.route('/run3')
def run_TA():
    job = q.enqueue(Scraper().getTA, retry=Retry(max=3))
    print(job.get_id())
    return 'OK'