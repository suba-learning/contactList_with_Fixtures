import requests
import pytest
import random
import json

base_url = "https://thinking-tester-contact-list.herokuapp.com"
user_info = {
   
}

def test_create_user():
    id = random.randint(1,400)
    print("\nCreate User\n")
    url = "/users"
    payload = {
        "firstName": "TestUser"+str(id),
        "lastName": "User",
        "email": "test"+str(id)+"@test.com",
        "password": "myPassword"
    }

    headers ={
        'Content-Type': 'application/json',
        #This cookie is default for this request.
        'Cookie': 'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2N2ViNzZjZjZiOGFlYjAwMTMzODViOGYiLCJpYXQiOjE3NDM0ODQ2MjN9.ersrjA5URW7XIupkSOsMqO-pTAP9FPcJfn5Bjt92E5g'
    }
    user_info['user'] = "test"+str(id)+"@test.com"
    user_info['password'] = "myPassword"
    response = requests.post(base_url+url, headers=headers, data=json.dumps(payload))
    #print(response.text)
    #return(response.json()['token'])
    assert response.status_code==201


@pytest.fixture()
def login():
    url = base_url + "/users/login"
    payload = {
        "email": user_info['user'],
        "password": user_info['password']
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))  
    #print(response.status_code)
    #print(response.text)
    return(response.json()['token'])

def test_getContacts(login):
    print("\nGet Contacts\n")
    url = base_url + "/contacts"
    headers = {
        'Authorization': login
    }
    payload = {}
    response = requests.get(url, headers=headers)
    #print(url)
    #print(json.dumps(response.json(), indent=4))
    assert response.status_code == 200

def test_addContact(login):
    print("\nAdd Contact\n")
    url =base_url + "/contacts"
    payload = {
        "firstName": "Suba",
        "lastName": "Nara",
        "birthdate": "1970-01-01",
        "email": "jdoe@fake.com",
        "phone": "8005555555",
        "street1": "1 Main St.",
        "street2": "Apartment A",
        "city": "Anytown",
        "stateProvince": "KS",
        "postalCode": "12345",
        "country": "USA"
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': login
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    #print("Contact ID: "+response.json()['_id'])
    user_info['contact_id'] = response.json()['_id']
    assert response.status_code == 201

def test_addContact_noAuth():
    print("\nAdd Contact\n")
    url = base_url + "/contacts"
    payload = {
        "firstName": "Suba",
        "lastName": "Nara",
        "birthdate": "1970-01-01",
        "email": "jdoe@fake.com",
        "phone": "8005555555",
        "street1": "1 Main St.",
        "street2": "Apartment A",
        "city": "Anytown",
        "stateProvince": "KS",
        "postalCode": "12345",
        "country": "USA"
    }
    headers = {
        'Content-Type': 'application/json',
        #'Authorization': login
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    #print("Contact ID: "+response.json()['_id'])
    #user_info['contact_id'] = response.json()['_id']
    assert response.status_code == 401

def test_getContacts_afteradding(login):
    print("\nGet Contacts after adding\n")
    url = base_url + "/contacts"
    headers = {
        'Authorization': login
    }
    payload = {}
    response = requests.get(url, headers=headers)
    #print(url)
    #print(response.text)
    assert response.status_code == 200

def test_update_contact(login):
    print("\nUpdate Contact\n")
    url = base_url + "/contacts/"+user_info['contact_id']
    payload = {
        "firstName": "Amy",
        "lastName": "Miller",
        "birthdate": "1992-02-02",
        "email": "amiller@fake.com",
        "phone": "8005554242",
        "street1": "3400 Nicolet Ave",
        "city": "Fremont",
        "stateProvince": "CA",
        "postalCode": "94536",
        "country": "USA"
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': login
    }
    response = requests.put(url, headers=headers, data=json.dumps(payload))
    #print(response.text)
    assert response.status_code == 200

def test_getContacts_afterUpdating(login):
    print("\nGet Contacts after Updating: \n")
    url = base_url + "/contacts/"+user_info['contact_id']
    headers = {
        'Authorization': login
    }
    payload = {}
    response = requests.get(url, headers=headers, data=payload)
    #print(url)
    #print(response.status_code)
    #print(json.dumps(response.json(), indent=4))
    assert response.status_code == 200


def test_delete_contact(login):
    print("\nDelete Contact\n")
    url = base_url + "/contacts/"+user_info['contact_id']
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Authorization': login
    }
    response = requests.delete(url, headers=headers)
    assert "Contact deleted" in response.text
    assert response.status_code == 200
    response = requests.get(url, headers=headers)
    assert response.status_code == 404