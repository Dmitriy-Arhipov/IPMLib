import requests
import time

def performance_analysis(urls):
    for url in urls:
        try:
            start_time = time.time()
            response = requests.get(url)
            response_time = time.time() - start_time
            
            print(f"URL: {url}")
            print(f"Response Time: {response_time:.2f} seconds")
            print(f"Content Size: {len(response.content)} bytes")
            print(f"Headers: {response.headers}\n")

        except requests.RequestException as e:
            print(f"Error analyzing performance for {url}: {e}")

urls = [
    "https://www.example.com",
    "https://www.example.org"
]

performance_analysis(urls)
