import requests

url = "http://127.0.0.1:4000/pushMetrics"

payload = {
  "id": "asdf",
  "jobname": "asdf",
  "hostname": "asdf",
  "metrics": {"test": "asgdf"},
  "labels": ["1", "2"]
}

r = requests.post(url, json=payload)

print(r.text)

