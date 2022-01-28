import os
import glob
import pandas as pd

#rename the file directory
os.chdir("C:/Users/qunzh/Documents/fypj/allcsv")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined.csv", index=False)
