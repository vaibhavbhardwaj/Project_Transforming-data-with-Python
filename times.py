import read
import dateutil.parser

df = read.load_data()

def time_sub(data):
     d = dateutil.parser.parse(data)
     return d.hour
df['hours'] = df['submission_time'].apply(time_sub)

print(df['hours'].value_counts())
        

    