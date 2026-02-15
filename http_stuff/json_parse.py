# use the JSON module
import json

def main():
    # define a string of JSON code (API used to parse JSON code from a string)
    jsonStr = '''{
            "sandwich": "Reuben",
            "toasted": true,
            "toppings": [
                "Thousand Island Dressing",
                "Sauerkraut",
                "Pickles"
            ],
            "price": 8.99
        }'''

    # parse the JSON data using loads - has the s because info is in a string
    data = json.loads(jsonStr)

    # print information from the data structure
    print("Sandwich: ", data['sandwich'])
    if (data['toasted']):
        print("It is TOASTED!")
    for topping in data['toppings']:
        print("Topping: ", topping)


if __name__ == "__main__":
    main()

