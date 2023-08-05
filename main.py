# import necessary libraries
import pandas as pd
import os
import glob
from sqlalchemy import create_engine

# use glob to get all the csv files
# in the folder
path = 'to/your/folder'
csv_files = glob.glob(os.path.join(path, "*.csv"))

# loop over the list of csv files
for f in csv_files:
    # read the csv file
    df = pd.read_csv(f)

    engine = create_engine('postgresql://postgres:******@localhost:5432/mydatabase')
    df.to_sql(( f.split("\\")[-1]), engine)
    # print the location and filename
    print('Location:', f)
    print('File Name:', f.split("\\")[-1])

    # print the content
    print('Content:')
    #display(df)
    print(df)


