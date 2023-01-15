from random import randint
import pandas as pd
from faker import Faker

fake = Faker(locale="ru_RU")
def input_fakedata(x):

        data = pd.DataFrame()
        for i in range(0, x):
            data.loc[i, 'id'] = randint(1, 100)
            data.loc[i, 'name'] = fake.name()
            data.loc[i, 'address'] = fake.address()
            data.loc[i, 'latitude'] = str(fake.latitude())
            data.loc[i, 'longitude'] = str(fake.longitude())
        return print(data)


input_fakedata(10)