# fear_and_greed_index
Small bit of code to extract cnn fear and greed historical data in python.

I got pointed in the right direction from https://github.com/hackingthemarkets/sentiment-fear-and-greed.
I used the previous data he had pulled and appended with updated data using this script.

There are some dates that do not have any data from cnn, so currently they are filled with 0s, but I put a line in there you can uncomment if you want to backfill.

fngindex.py is the main script.
fear-greed.csv is the data from Part Time Larry.
all_fng.pkl is the pickle version of all updated data in a dataframe.
all_fng_csv.csv is the csv file with updated data.
