import requests

# Список XSS-пayload'ов
xss_payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<iframe src='javascript:alert(1)'></iframe>"
]

def scan_xss(url):
    for payload in xss_payloads:
        response = requests.get(url, params={'input': payload})
        if payload in response.text:
            print(f"Possible XSS vulnerability detected with payload: {payload}")
        else:
            print(f"No vulnerability detected with payload: {payload}")

if __name__ == "__main__":
    target_url = input("Enter the URL to scan for XSS: ")
    scan_xss(target_url)
