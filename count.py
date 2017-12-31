import read
import collections

df = read.load_data()
str_h_df=''
for h in df['headline']:
    h = str(h)
    h1=h.lower()
    str_h_df=str_h_df + ' ' + h1
#print(str_h_df)
#print(collections.Counter(str_h_df).most_common(3))
words = str_h_df.split(" ")
c= collections.Counter(words)
result  = c.most_common(100)
print(result)