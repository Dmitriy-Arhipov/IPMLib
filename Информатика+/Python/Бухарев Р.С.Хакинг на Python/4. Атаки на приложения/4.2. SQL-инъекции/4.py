import requests

def check_csrf(url):
    # Предположим, что запрос к API требует CSRF-токен
    session = requests.Session()
    response = session.get(url)
    
    # Предположим, что токен хранится в cookies
    csrf_token = session.cookies.get('csrftoken')

    if csrf_token:
        # Пробуем выполнить запрос без токена
        post_response = requests.post(url, data={'data': 'test'})
        if post_response.status_code == 200:
            print("CSRF vulnerability detected - request was accepted without a valid CSRF token.")
        else:
            print("No CSRF vulnerability detected.")
    else:
        print("No CSRF token found.")

if __name__ == "__main__":
    target_url = input("Enter the URL to check for CSRF vulnerability: ")
    check_csrf(target_url)
