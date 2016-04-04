import requests
import datetime
import time
from PIL import Image
import io
import json
import random
import numpy as np

LOCATION = 'Toledo, OH'

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
    random.seed(time.clock())
    generate_request(datetime.date(2016, 3, 2), datetime.date(2016, 3, 30))
