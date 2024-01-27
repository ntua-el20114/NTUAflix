#!/usr/bin/env python
import requests
from flask import session
import pandas as pd
from io import StringIO
import argparse
import json
import os
import csv
import sys

def generate_csv_data(data_dict):
    # Δημιουργία λίστας με τα ονόματα των στηλών βάσει των κλειδιών του λεξικού
    columns = list(data_dict.keys())

    # Δημιουργία λίστας με τα δεδομένα για κάθε σειρά
    rows = [data_dict.get(column, '') for column in columns]

    csv_data = ','.join(map(str, columns)) + '\n'  # add columns
    csv_data += ','.join(map(str, rows))  # add data
    print(csv_data)
    return csv_data

def generate_csv_data_2(data_list):
    if not data_list:
        return "No data available."

    # Εκτύπωση των κεφαλίδων
    headers = data_list[0].keys()
    print(','.join(headers))

    # Εκτύπωση των δεδομένων
    for item in data_list:
        values = [str(item.get(header, 'None')) for header in headers]
        print(','.join(values))

def save_credentials_to_config_file(token, user_role, username):
    config_file_path = 'config.ini'

    # Save token and user_role to the configuration file
    with open(config_file_path, 'w') as config_file:
        config_file.write(f'TOKEN={token}\n')
        config_file.write(f'USER_ROLE={user_role}\n')
        config_file.write(f'USERNAME={username}')

def load_credentials_from_config_file():

    config_file_path = 'config.ini'

    # Load token and user_role from the configuration file
    if os.path.exists(config_file_path):
        with open(config_file_path, 'r') as config_file:
            lines = config_file.readlines()
            token = None
            user_role = None
            for line in lines:
                if 'TOKEN' in line:
                    token = line.split('=')[1].strip()
                elif 'USER_ROLE' in line:
                    user_role = line.split('=')[1].strip()
                elif 'USERNAME' in line:
                    username = line.split('=')[1].strip()

            return token, user_role, username

    return None, None, None

def login(username, password):

    url = 'http://127.0.0.1:9876/ntuaflix_api/login'
    data = {'username': username, 'password': password}
    response = requests.post(url, data=data)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        result_dict = response.json()
        ###
        token = result_dict['token']
        user_role = result_dict['user_role']
        ###
        print()
        # Print each key-value pair on a new line
        # for key, value in result_dict.items():
        #     print(f'{key}: {value}')
        print(f"Welcome {username}!")
        print()

    else:
        print(f'Error: {response.status_code}')
        return None

    return token, user_role


def get_user_role(token):

    url = 'http://127.0.0.1:9876/ntuaflix_api/user_role'
    headers = {'X-OBSERVATORY-AUTH': token}
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        result_dict = response.json()
        ###
        user_role = result_dict['user_role']
        ###
        print(user_role)
        
    else:
        print(f'Error: {response.status_code}')
        return None
    
    return user_role

def title(titleID,token, csv_format):

    url = f'http://127.0.0.1:9876/ntuaflix_api/title/{titleID}'
    
    response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': token})
    #print(response.text)
    #print(session["token"])
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        if csv_format == 1:
            generate_csv_data(response.json())
        else:          
            result_dict = response.json()
            print()
            # Print each key-value pair on a new line
            for key, value in result_dict.items():
                print(f'{key}: {value}')
            print()
    else:
        print(f'Error here: {response.status_code}')
    
def searchtitle(titlePart, token, csv_format):
    url = 'http://127.0.0.1:9876/ntuaflix_api/searchtitle'
    data = {'titlePart': titlePart}
    response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': token} ,data=data)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        if csv_format == 1:
            result_dict = response.json()
            result_list = result_dict.get("result", [])
            generate_csv_data_2(result_list)
        else: 
            result_dict = response.json()
            result_list = result_dict.get("result", [])
            print()
            # Print each key-value pair on a new line
            for title in result_list:
                for key, value in title.items():
                    print(f'{key}: {value}')
                print()
    else:
        print(f'Error: {response.status_code}')

def bygenre(qgenre, minrating, yrFrom, yrTo, token, csv_format):

    url = 'http://127.0.0.1:9876/ntuaflix_api/bygenre'
    data = {'qgenre': qgenre, 'minrating': minrating, 'yrFrom':yrFrom, 'yrTo': yrTo}
    response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': token} ,data=data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        if csv_format == 1:
            result_dict = response.json()
            result_list = result_dict.get("result", [])
            generate_csv_data_2(result_list)
        else:
            result_dict = response.json()
            result_list = result_dict.get("result", [])
            print()
            # Print each key-value pair on a new line
            for title in result_list:
                for key, value in title.items():
                    print(f'{key}: {value}')
                print()
    else:
        print(f'Error: {response.status_code}')

def name(nameID, token, csv_format):

    url = f'http://127.0.0.1:9876/ntuaflix_api/name/{nameID}'
    response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': token})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        if csv_format == 1:
            generate_csv_data(response.json())

        else:
            result_dict = response.json()
            print()
            # Print each key-value pair on a new line
            for key, value in result_dict.items():
                print(f'{key}: {value}')
            print()
    else:
        print(f'Error: {response.status_code}')

def searchname(namePart, token, csv_format):
    url = 'http://127.0.0.1:9876/ntuaflix_api/searchname'
    data = {'namePart': namePart}
    response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': token},data=data)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        if csv_format == 1:
            result_dict = response.json()
            result_list = result_dict.get("result", [])
            generate_csv_data_2(result_list)
        else:
            result_dict = response.json()
            result_list = result_dict.get("result", [])
            print()
            # Print each key-value pair on a new line
            for title in result_list:
                for key, value in title.items():
                    print(f'{key}: {value}')
                print()
    else:
        print(f'Error: {response.status_code}')

def rec1(title, token, csv_format):

    url = f'http://127.0.0.1:9876/ntuaflix_api/movierecommender_1/{title}'
    response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': token})
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        if csv_format == 1:
            result_dict = response.json()
            result_list = result_dict.get("result", [])
            generate_csv_data_2(result_list)
        else: 
            result_dict = response.json()
            result_list = result_dict.get("result", [])
            print()
            # Print each key-value pair on a new line
            for title in result_list:
                for key, value in title.items():
                    print(f'{key}: {value}')
                print()
    else:
        print(f'Error: {response.status_code}')
        
        
  
def rec2(genre, username, token, csv_format):

    url = f'http://127.0.0.1:9876/ntuaflix_api/movierecommender_2/{genre}/{username}'
    response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': token})
    # Check if the request was successful (status code 200)
    #print(csv_format)
    if response.status_code == 200:
        if csv_format == 1:
            result_dict = response.json()
            result_list = result_dict.get("result", [])
            generate_csv_data_2(result_list)
        else: 
            result_dict = response.json()
            result_list = result_dict.get("result", [])
            print()
            # Print each key-value pair on a new line
            for title in result_list:
                for key, value in title.items():
                    print(f'{key}: {value}')
                print()
    else:
        print(f'Error: {response.status_code}')

def chatbot(prompt, token):
    url = 'http://127.0.0.1:9876/ntuaflix_api/chatbot'
    data = {'Sentence': prompt}
    response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': token}, data=data)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        response_dict = json.loads(response.text)

        # Extract the list of movies from the "result" key
        result = response_dict.get("Response", [])
        print(result)
    else:
        print(f'Error: {response.status_code}')

def logout(token):
    config_file_path = './config.ini'
    # Check if the configuration file exists
    if os.path.exists(config_file_path):
        # Delete the configuration file
        os.remove(config_file_path)
    url = 'http://127.0.0.1:9876/ntuaflix_api/logout'
    response = requests.post(url, headers = {'X-OBSERVATORY-AUTH': token})
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f'Error: {response.status_code}')

##################################################################################################
###################################### FOR ADMIN ################################################# 
##################################################################################################

def adduser(token, username, password):

    url = f'http://127.0.0.1:9876/ntuaflix_api/admin/usermod/{username}/{password}'
    response = requests.post(url, headers={'X-OBSERVATORY-AUTH': token})
    # Check if the request was successful (status code 200)
    if response.status_code == 200 or response.status_code == 201:
        print(response.text)
    else:
        print(f'Error: {response.status_code}')


def healthcheck(token):

    url = 'http://127.0.0.1:9876/ntuaflix_api/admin/healthcheck'
    response = requests.get(url, headers={'X-OBSERVATORY-AUTH': token})
    print(response.text)

def newtitles(token, file_path):
    with open(file_path, 'r') as file:
        tsv_data = file.read()
    data = {'tsv_data': tsv_data}

    url = 'http://127.0.0.1:9876/ntuaflix_api/admin/upload/titlebasics'
    response = requests.post(url, headers = {'X-OBSERVATORY-AUTH': token}, data=data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f'Error: {response.status_code}')

def newakas(token, file_path):
    with open(file_path, 'r') as file:
        tsv_data = file.read()
    data = {'tsv_data': tsv_data}

    url = 'http://127.0.0.1:9876/ntuaflix_api/admin/upload/titleakas'
    response = requests.post(url, headers = {'X-OBSERVATORY-AUTH': token},data=data)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f'Error: {response.status_code}')

def newnames(token, file_path):
    with open(file_path, 'r') as file:
        tsv_data = file.read()
    data = {'tsv_data': tsv_data}
    
    url = 'http://127.0.0.1:9876/ntuaflix_api/admin/upload/namebasics'
    response = requests.post(url, headers = {'X-OBSERVATORY-AUTH': token},data=data)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f'Error: {response.status_code}')

def newcrew(token, file_path):
    with open(file_path, 'r') as file:
        tsv_data = file.read()
    data = {'tsv_data': tsv_data}
    
    url = 'http://127.0.0.1:9876/ntuaflix_api/admin/upload/titlecrew'
    response = requests.post(url, headers = {'X-OBSERVATORY-AUTH': token},data=data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f'Error: {response.status_code}')

def newepisode(token, file_path):
    with open(file_path, 'r') as file:
        tsv_data = file.read()
    data = {'tsv_data': tsv_data}

    url = 'http://127.0.0.1:9876/ntuaflix_api/admin/upload/titleepisode'
    response = requests.post(url, headers = {'X-OBSERVATORY-AUTH': token},data=data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f'Error: {response.status_code}')

def newprincipals(token, file_path):
    with open(file_path, 'r') as file:
        tsv_data = file.read()
    data = {'tsv_data': tsv_data}

    url = 'http://127.0.0.1:9876/ntuaflix_api/admin/upload/titleprincipals'
    response = requests.post(url, headers = {'X-OBSERVATORY-AUTH': token},data=data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f'Error: {response.status_code}')

def newratings(token, file_path):
    with open(file_path, 'r') as file:
        tsv_data = file.read()
    data = {'tsv_data': tsv_data}

    url = 'http://127.0.0.1:9876/ntuaflix_api/admin/upload/titleratings'
    response = requests.post(url, headers = {'X-OBSERVATORY-AUTH': token},data=data)
    #print(response.text)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f'Error: {response.status_code}')

def resetall(token):

    url = 'http://127.0.0.1:9876/ntuaflix_api/admin/resetall'
    response = requests.post(url, headers={'X-OBSERVATORY-AUTH': token})
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        result_dict = response.json()
        print()
        # Print each key-value pair on a new line
        for key, value in result_dict.items():
            print(f'{key}: {value}')
        print()
    else:
        print(f'Error: {response.status_code}') 

def user(token, username):

    url = f'http://127.0.0.1:9876/ntuaflix_api/admin/users/{username}'
    response = requests.get(url, headers={'X-OBSERVATORY-AUTH': token})
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        result_dict = response.json()
        print()
        # Print each key-value pair on a new line
        for key, value in result_dict.items():
            print(f'{key}: {value}')
        print()
    else:
        print(f'Error: {response.status_code}')   


def main():
    parser = argparse.ArgumentParser(description='CLI for ntuaflix application')
    parser.add_argument('scope', choices=['login', 'logout', 'adduser', 'user', 'healthcheck', 'resetall', 'newtitles', 'newakas', 
                                          'newnames', 'newcrew', 'newepisode', 'newprincipals', 'newratings',
                                          'title', 'searchtitle', 'bygenre', 'name', 'searchname','rec1', 'rec2', 'chatbot'], help='Scope of the operation')

    
    parser.add_argument('--param1', type=str, help='First parameter')
    parser.add_argument('--param2', type=str, help='Second parameter')
    parser.add_argument('--param3', type=str, help='Third parameter')
    parser.add_argument('--param4', type=str, help='Fourth parameter')
    parser.add_argument('--format', choices=['json', 'csv'], default='json', help='Output format (default: json)')

    args = parser.parse_args()

    csv_format = 0
    if args.format == 'csv':
       csv_format = 1

    if args.scope == 'login':
        username = args.param1
        # param2 == password
        token, user_role = login(username, args.param2)
        save_credentials_to_config_file(token, user_role, username)

    else:
        token, user_role, username = load_credentials_from_config_file()
        # We check if the login is done first.
        if (token == None or user_role == None):
            print("Login is required !")
            return None
        if args.scope == 'title':
            # param1 == title id
            title(args.param1, token, csv_format)
        elif args.scope == 'searchtitle':
            # param1 == part of the title
            searchtitle(args.param1, token, csv_format)
        elif args.scope == 'bygenre':
            # param1 == genre
            # param2 == min rating
            # param3 == year from
            # param4 == year to
            bygenre(args.param1, args.param2, args.param3, args.param4, token, csv_format)
        elif args.scope == 'name':
            # param1 == name id
            name(args.param1, token, csv_format)
        elif args.scope == 'searchname':
            # param1 == part of name
            searchname(args.param1, token, csv_format)
        elif args.scope == 'rec1':
            #param1 == title of the movie
            rec1(args.param1, token, csv_format)
        elif args.scope == 'rec2':
            #param1 == genre
            rec2(args.param1, username, token, csv_format)
        elif args.scope == 'chatbot':
            #param1 == prompt
            chatbot(args.param1, token)
        elif args.scope == 'logout':
            logout(token)
        
        # For admins only!
        if(user_role != 'administrator'):
            print("You must have administrator privelleges")
            return None
        
        if args.scope == 'adduser':
            username = args.param1 
            password = args.param2
            adduser(token, username, password)
        elif args.scope == 'healthcheck':
            healthcheck(token)
        elif args.scope == 'newtitles':
            file_path = args.param1
            newtitles(token, file_path)
        elif args.scope == 'newakas':
            file_path = args.param1
            newakas(token, file_path)
        elif args.scope == 'newnames':
            file_path = args.param1
            newnames(token, file_path)
        elif args.scope == 'newcrew':
            file_path = args.param1
            newcrew(token, file_path)
        elif args.scope == 'newepisode':
            file_path = args.param1
            newepisode(token, file_path)
        elif args.scope == 'newprincipals':
            file_path = args.param1
            newprincipals(token, file_path)
        elif args.scope == 'newratings':
            file_path = args.param1
            newratings(token, file_path)
        elif args.scope == 'resetall':
            resetall(token)
        elif args.scope == 'user':
            # param1 == username
            user(token, args.param1)


if __name__ == "__main__":
    main()
