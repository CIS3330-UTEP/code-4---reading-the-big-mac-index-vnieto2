import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv(big_mac_file)

# print (df)
# print (df['iso_a3'])



def get_big_mac_price_by_year(year, country_code):
    country_code = 'jpn'
    year = 2016
    query = f'(iso_a3 == {country_code} and date == {year})'
    jpn_df = df.query(query)
    print(round(jpn_df['dollar_price'].mean(),2)) 

def get_big_mac_price_by_country(country_code):
    pass
    #  query = f'(iso_a3 == {country_code})'
    # mxn_df = df.query(query)
    # print(round(mxn_df['dollar_price'].mean(),2))


def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    get_big_mac_price_by_year(year= 2016,country_code='jpn')