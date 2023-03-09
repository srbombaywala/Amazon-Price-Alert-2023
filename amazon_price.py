import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

my_email = "inspire@snpitrc.ac.in"
my_password = "$$$$$$$$$$$$$" # your app key generated from Gmail

# The procduct you want to buy
amazon_url = "https://www.amazon.in/dp/B07KZ1W688/ref=sspa_dk_detail_4?psc=1&pf_rd_p=b3dfef88-30a1-490c-be36-e990ef384667&pf_rd_r=NP7Q84G9CPND5E6ZPFSX&pd_rd_wg=GYEKG&pd_rd_w=5rjJ5&content-id=amzn1.sym.b3dfef88-30a1-490c-be36-e990ef384667&pd_rd_r=6467c5c7-ca5a-4c19-b724-8aa97c36ec12&s=kitchen&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw"


header = {
    "Accept-Language":"en-US,en;q=0.5",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
}
response = requests.get(url=amazon_url, headers=header)
data = response.text

soup = BeautifulSoup(data, 'lxml')
# inspect the HTML structure on Amazon product page. Today (09/03/2023 in amazon.in) I can get data from below lines of code
product_name = soup.find(name="span", id="productTitle").getText().strip()
price = float(soup.find(name="span", class_="a-price-whole").getText().replace(",","").replace(".",""))
# Set the price at which you would be looking to buy
target_price = 6500.00

if price<target_price:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(my_email,my_password)
        connection.sendmail(
            from_addr = my_email,
            to_addrs= my_email,
            msg=f"Subject:Amazon Price Alert!\n\n{product_name} is now Rs.{price}\n{amazon_url}"
        )
