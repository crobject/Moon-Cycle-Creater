import requests
import datetime
import time
from PIL import Image
import io
import json
import random
import numpy as np
import argparse

LOCATION = 'New York, NY'

parser = argparse.ArgumentParser()
parser.add_argument('--location', help='location that the moon data will be calculated from')
parser.add_argument('--start',  help='start date for the data collection')
parser.add_argument('--end',  help='end date for the data collection')

def calculate_moon_tilt(date, time):
    pass

def generate_request(start_date, end_date):
    total_days = (end_date - start_date).days
    for day_number in range(total_days):
        date = (start_date + datetime.timedelta(days = day_number))
        hour = random.randint(20, 24)
        minute = random.randint(0, 60)
        get_moon_picture(date.strftime("%m/%d/%Y"), '{0}:{1}'.format(hour, minute), LOCATION)
        with open('moon_data.json') as f:
            data = json.load(f)
        data.update({'moon_' + str(len(data.keys())) : {'date': '{0}:{1}'.format(hour, minute)}})
        with open('moon_data.json', 'w') as f:
            json.dump(data, f)

        print('image saved and data recorded')

def get_moon_picture(date, time, location):
    reqstr = 'http://api.usno.navy.mil/imagery/moon.png?&ID=chris_astronomy_project&date={0}&time={1}&loc={2}'.format(str(date), str(time), location)
    re = requests.get(reqstr)
    i = Image.open(io.BytesIO(re.content)).convert("RGBA")
    i.save('moon_{0}_{1}.png'.format(date.replace('/', '-'), time))


if __name__ == '__main__':
    args = parser.parse_args()
    LOCATION = args.location
    random.seed(time.clock())
    try:
        start = datetime.datetime.strptime(args.start, '%d/%M/%Y')
        end = datetime.datetime.strptime(args.end, '%d/%M/%Y')
    except Exception as E:
        print('invalid date format...Should be 1/15/2015 for January 15th 2015')
        exit(0)        
    generate_request(start, end)
