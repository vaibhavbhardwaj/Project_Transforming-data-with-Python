import pandas as pd
def load_data():
    df = pd.read_csv("hn_stories.csv")
    df.columns = ['submission_time','upvotes','url','headline']
    #print(df.head(2))
    return df
    
if __name__ == "__main__":
    print("Welcome to a python script")
    load_data() 