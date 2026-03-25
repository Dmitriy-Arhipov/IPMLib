import requests
import time

def performance_test(url, num_requests):
    times = []
    for _ in range(num_requests):
        start_time = time.time()
        try:
            requests.get(url)
            times.append(time.time() - start_time)
        except requests.RequestException as e:
            print(f"Error during request: {e}")

    average_time = sum(times) / len(times) if times else 0
    print(f"Average response time for {url}: {average_time:.2f} seconds")

url = "https://www.example.com"
num_requests = 100
performance_test(url, num_requests)
