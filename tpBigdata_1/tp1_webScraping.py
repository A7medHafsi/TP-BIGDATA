import requests
from bs4 import BeautifulSoup
import pandas as pd

# قوائم لتخزين البيانات
book_titles = []
book_prices = []
book_ratings = []
book_availability = [] 

# التكرار عبر صفحات الموقع
for page in range(1, 50): 
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.p["class"][1]
        availability = book.find("p", class_="instock availability").text.strip()  
        
        book_titles.append(title)
        book_prices.append(price)
        book_ratings.append(rating)
        book_availability.append(availability) 
# تخزين البيانات في DataFrame
df = pd.DataFrame({
    "Title": book_titles,
    "Price": book_prices,
    "Rating": book_ratings,
    "Availability": book_availability  
})

# حفظ البيانات في ملف Excel
df.to_excel("large_books_data.xlsx", index=False)
