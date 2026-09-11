import pandas as pd

data = {
    'Name': ['Mahesh', 'Paani', 'Suresh', 'Mukesh'],
    'Age': [25, 30, 35, 55],
    'City': ['Chennai', 'Bangalore', 'Tirupati', 'Varanasi'],
    'Designation': ['Chaprasi', 'Berojgar', 'Software Engineer', 'Manager']
}

df = pd.DataFrame(data)

print(df)
