from random import randint
import pandas as pd
from faker import Faker

fake = Faker(locale="ru_RU")
def input_fakedata(item):

        data = pd.DataFrame()
        for idex in range(0, item):
            data.loc[idex, 'id'] = randint(1, 100)
            data.loc[idex, 'name'] = fake.name()
            data.loc[idex, 'address'] = fake.address()
            data.loc[idex, 'latitude'] = str(fake.latitude())
            data.loc[idex, 'longitude'] = str(fake.longitude())
        return data

