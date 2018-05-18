def info(name_to_get):
    import requests
    import csv

    API_KEY = 'AIzaSyArsUvbaa5rQlt1Y0cGRaZxO87J5hNhcIA'

    with open('Uppdrag och adress.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        names = []
        addresses = []

        for row in readCSV:
            name = row[0]
            address = row[2]
            names.append(name.lower())
            addresses.append(address.lower())

    try:
        what_name = name_to_get
        namedex = names.index(what_name.lower())

        the_address = addresses[namedex]

        url_base_for_latlong = 'https://maps.googleapis.com/maps/api/geocode/json?address='
        url_for_latlong = url_base_for_latlong + the_address + '&key=' + API_KEY

        lat_long = requests.get(url_for_latlong).json()

        lat = str(lat_long['results'][0]['geometry']['location']['lat'])
        lon = str(lat_long['results'][0]['geometry']['location']['lng'])

        base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='

        location = lat + ',' + lon

        spec = '&radius=600&type=restaurant&key=' + API_KEY

        url = base_url + location + spec
        restaurang = requests.get(url).json()

        print('5 restauranger: ')
        restaurants = []
        for i in range(0, 5):
            restaurants.append(':hotdog:  ' + restaurang['results'][i]['name'] + ', '
                               + restaurang['results'][i]['vicinity'])

        return restaurants

    except ValueError:
        print('finns ingen med det namnet yo')


if __name__ == '__main__':
    info('Mikko')
