import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv(big_mac_file)


def get_big_mac_price_by_year(year,country_code):
    query = f'(iso_a3 == {country_code} and date = {year})'
    jpn_df = df.query(query)
    return round(jpn_df['dollar_price'].mean(),2)

def get_big_mac_price_by_country(country_code):
    query = f'(iso_a3 == {country_code})'
    jpn_df = df.query(query)
    return round(jpn_df['dollar_price'].mean(),2)


def get_the_cheapest_big_mac_price_by_year(year):
    query = f'(date == {year})'
    cheap_df = df.query(query)
    return cheap_df['dollar_price'].min()

def get_the_most_expensive_big_mac_price_by_year(year):
    query = f'(date == {year})'
    rich_df = df.query(query)
    return rich_df['dollar_price'].max()

if __name__ == "__main__":
    print(get_big_mac_price_by_year(2016,'jpn'))

    print(get_big_mac_price_by_country('jpn'))

    print(get_the_cheapest_big_mac_price_by_year(2016))

    print(get_the_most_expensive_big_mac_price_by_year(2016))
