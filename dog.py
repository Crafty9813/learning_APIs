import requests

base_url =  "https://dog.ceo/api/breed"

def get_dog_info (breed):
    url = f"{base_url}/{dog_breed}/images/random"
    response = requests.get(url)
    print(response)

dog_breed = "Shiba"

get_dog_info(dog_breed)



