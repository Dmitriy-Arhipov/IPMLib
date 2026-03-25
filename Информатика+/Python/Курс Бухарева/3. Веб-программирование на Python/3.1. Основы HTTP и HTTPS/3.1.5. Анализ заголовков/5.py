import requests

def analyze_redirects(urls):
    for url in urls:
        try:
            response = requests.get(url, allow_redirects=True)
            history = response.history
            
            if history:
                print(f"Redirect chain for {url}:")
                for resp in history:
                    print(f"  {resp.status_code} -> {resp.url}")
                print(f"Final Destination: {response.url}\n")
            else:
                print(f"No redirects for {url} (Status Code: {response.status_code})\n")

        except requests.RequestException as e:
            print(f"Error analyzing redirects for {url}: {e}")

urls = [
    "http://github.com",
    "http://httpbin.org/redirect/3"
]

analyze_redirects(urls)
