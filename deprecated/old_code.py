from flask import Flask

def legacy_function():
    app = Flask(__name__)
    @app.route('/')
    def home():
        return "Legacy endpoint"
    print("Legacy Flask app initialized")
