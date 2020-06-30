import sys
sys.path.append(r"C:\Users\van-gerald.olivares\Documents\08 Code\CQRS-kata")
from src.app import app

def test_hello_world():
    assert app.hola_mundo()=="Hola Mundo"