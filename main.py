import requests

API_URL = "https://restcountries.com/v3.1/name/{}"

def get_data(country_name):
    
    response = requests.get(API_URL.format(country_name), timeout=6)
    # format() puts user's inputted country name into the url
    # timeout=6 meaans abort if server deosnt respond in 6seconds

    if response.status_code == 200:
        print("Country found!!!")
        # return response.json() #this is a list, not dict
        return response.json()[0] #this is a dict
        # the json is [ { } ], so [0] is dict { }
    
    else:
        print(f" Error : {response.status_code}")
        exit()


def parse_info(data):
    name = data["name"]["common"]
    population = data["population"]
    region = data["region"]

    languages = ", ".join(data.get("languages", {}).values())
    # data['languages'] gives error if no language so use data.get()
    # data.get("...", {}) means give ... if exists, else, give an empty dict

    currencies_data = data.get("currencies", {})
    currencies = []
    for code, info in currencies_data.items():
        currencies.append(f"{info['name']} ({code})")
    currency = ", ".join(currencies)

    return {
        "Name": name,
        "Population": f"{population:,}",
        "Region": region,
        "Languages": languages,
        "Currency": currency
    }

def display(info):
    print(info)


def main():
    print("GET INFORMATION ABOUT A COUNTRY ")
    country = input("Enter country name ")

    data = get_data(country)

    info = parse_info(data)
    display(info)

main()