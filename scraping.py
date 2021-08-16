from numpy import product

from requests_html import HTMLSession

import pandas as pd

import csv

 

def getPrice(url):

    s=HTMLSession()

    r=s.get(url)

    r.html.render(sleep=1)

 

    product={

 

        'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,

        'brand': r.html.xpath('//*[@id="productOverview_feature_div"]/div/table/tbody/tr[2]/td[2]/span',first=True).text,

        'price': r.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text,

        'scent': r.html.xpath('//*[@id="productOverview_feature_div"]/div/table/tbody/tr[1]/td[2]/span',first=True).text,

        'ingredients': r.html.xpath('//*[@id="feature-bullets"]/ul/li[2]/span',first=True).text,

        'size': r.html.xpath('//*[@id="productOverview_feature_div"]/div/table/tbody/tr[3]/td[2]/span',first=True).text,

        'manufacturer': r.html.xpath('//*[@id="productDetails_techSpec_section_1"]/tbody/tr[1]/td',first=True).text,

        'best_seller_rank': r.html.xpath('//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[3]/td',first=True).text,

        'star': r.html.xpath('//*[@id="acrPopover"]/span[1]/a/i[1]',first=True).text,

        'ratings': r.html.xpath('//*[@id="acrCustomerReviewText"]',first=True).text,

        'url': url

    }

    

    print(product)

    with open('product.csv', mode='w', encoding="utf-8") as product_file:

        product_writer = csv.writer(product_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        product_writer.writerow(["title", "brand", "price", "scent", "ingredients", "size", "manifacturer", "best_seller_rank", "star", "ratings", "url"])

        product_writer.writerow([product['title'], product['brand'], product['price'], product['scent'], product['ingredients'], product['size'], product['manufacturer'], product['best_seller_rank'], product['star'], product['ratings'], product['url']])

 

    return product

 

getPrice('https://www.amazon.com/Therapeutic-Essential-Uplifting-Aromatherapy-Relaxation/dp/B07PR1X7FR/ref=sr_1_204?dchild=1&m=ATVPDKIKX0DER&qid=1625995666&refinements=p_6%3AATVPDKIKX0DER&rnid=331556011&s=hpc&sr=1-204')

 

df=pd.DataFrame(product)

 

print(df.head())