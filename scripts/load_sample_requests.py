import requests, random, time
URL = "http://localhost:8080/score"
for i in range(10):
    feats = [random.uniform(-2,2) for _ in range(6)]
    r = requests.post(URL, json={"features": feats})
    print(i, feats, r.status_code, r.text)
    time.sleep(0.5)
