import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
description=[]
review=[]
price=[]
#import csv
result = requests.get("https://www.amazon.eg/-/en/s?i=electronics&bbn=21832883031&rh=n%3A21832883031%2Cp_89%3ASAMSUNG%2Cp_72%3A21909187031%2Cp_36%3A26059283031%2Cp_n_feature_twelve_browse-bin%3A27361676031%2Cp_n_feature_browse-bin%3A26978809031&dc&language=en&pf_rd_i=21832883031&pf_rd_m=A1ZVRGNO5AYLOV&pf_rd_p=bf9d5754-be4e-409a-ad87-89abbc6d8911&pf_rd_r=1Y8ZX9K15A57KGTBN4YH&pf_rd_s=merchandised-search-14&pf_rd_t=101&qid=1671299393&rnid=26978803031&ref=sr_nr_p_n_feature_browse-bin_3&ds=v1%3A11ex%2B%2Fuz137XD4j0evbNExhq4L9e8Ggi%2F40iPpI0kqg")
scr = result.content
print(scr)
#create soup object yo parse centent
soup = BeautifulSoup(scr, "html.parser")
print(soup)
#find elements containing info we need
description=soup.find_all("h1",{"class":"a-size-large a-spacing-none"})
review=soup.find_all('span',{"class":"a-size-base"})
price=soup.find_all('span',{"class":"a-price-whole"})
#loop over returned lists to exract needed info into other lists
for i in range(len(description)):
    descriptions.append(description[i].text)
    reviews.append(review[i].text)
    price.append(price[i].text)
    print(descriptions, reviews, price)
    print("-------------------------------------------------")












