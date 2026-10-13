import requests

twopart_joke = []
single_joke = ""

def get_random_joke():

    global twopart_joke
    global single_joke

    url = f"https://v2.jokeapi.dev/joke/Any"

    response = requests.get(url, timeout=10)

    response.raise_for_status()

    data = response.json()

    if data["type"] == "single":
        single_joke = data["joke"]
        return single_joke
    elif data["type"] == "twopart":
       twopart_joke.append(data["setup"])
       twopart_joke.append(data["delivery"])
       return twopart_joke


def print_single_joke(single_joke):
   print("Joke:")
   print(single_joke)

def print_twopart_joke(twopart_joke):
    print("Joke:")
    print(f"Setup: {twopart_joke[0]}")
    print(f"Delivery: {twopart_joke[1]}")


get_random_joke()

if single_joke == "":
   print_twopart_joke(twopart_joke)
else:
   print_single_joke(single_joke)


   
