from fastapi import FastAPI
from utils import utils
app = FastAPI()

@app.get("/")
def read_root():
    return {'message': 'Welcome to The Association Rule API!'}

@app.get('/most_frequent_items')
def read_most_frequent_items():
    return {'most': utils.get_frequent_items()}

