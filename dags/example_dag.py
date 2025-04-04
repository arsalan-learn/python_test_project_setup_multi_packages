import requests

def run_dag():
    res = requests.get("http://example.com")
    print("DAG response:", res.status_code)
