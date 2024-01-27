import requests

def login(username, password):
    response = requests.post('http://localhost:9876/ntuaflix_api/login', data={'username': f'{username}', 'password': f'{password}'})
    print("Login Response:", response.text)
    token = response.json().get('token')
    if token:
        print("Login Successful. Token:", token)
        return token
    else:
        print("Login Failed.")
        return None
    
def make_protected_request(url, headers, body=None):
    response = requests.get(url, headers=headers, data=body)
    print(f"Request to {url}: {response.status_code}")
    print(response.text)
    print()



if __name__ == "__main__":  
    
    token = login("EriksenIvan99", "FKZzWwX70J")
  
    make_protected_request('http://localhost:9876/ntuaflix_api/title/tt0000929', {'X-OBSERVATORY-AUTH': token})

    make_protected_request('http://localhost:9876/ntuaflix_api/searchtitle', {'X-OBSERVATORY-AUTH': token}, {"titlePart" : "lion"})
    
    make_protected_request('http://localhost:9876/ntuaflix_api/admin/users/GonzalezJoe5', {'X-OBSERVATORY-AUTH': token})

    requests.post('http://localhost:9876/ntuaflix_api/logout', headers={'X-OBSERVATORY-AUTH': token})


    token = login("LeachHector18", "Z5XFIzNIlV")
  
    make_protected_request('http://localhost:9876/ntuaflix_api/title/tt0000929', {'X-OBSERVATORY-AUTH': token})

    make_protected_request('http://localhost:9876/ntuaflix_api/searchtitle', {'X-OBSERVATORY-AUTH': token}, {"titlePart" : "woman"})

    make_protected_request('http://localhost:9876/ntuaflix_api/admin/users/GonzalezJoe5', {'X-OBSERVATORY-AUTH': token})

    requests.post('http://localhost:9876/ntuaflix_api/logout', headers={'X-OBSERVATORY-AUTH': token})


