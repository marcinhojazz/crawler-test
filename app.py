import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, render_template

app = Flask(__name__)

def get_total_pages(soup):
    pagination = soup.find('ul', class_='pagination')
    if not pagination:
        return 1
    pages = pagination.find_all('li')
    last_page = 1
    for page in pages:
        link = page.find('a')
        if link and link.text.isdigit():
            last_page = max(last_page, int(link.text))
    return last_page

def scrape_lenovo_notebooks():
    base_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"
    products = []

    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    total_pages = get_total_pages(soup)

    for page in range(1, total_pages + 1):
        if page == 1:
            url = base_url
        else:
            url = f"{base_url}?page={page}"

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        for product in soup.find_all('div', class_='col-md-4 col-xl-4 col-lg-4'):
            title_tag = product.find('a', class_='title')
            title = title_tag.text
            if 'Lenovo' in title:
                price = float(product.find('h4', class_='price').text.replace('$', ''))
                description = product.find('p', class_='description').text
                reviews = product.find('p', class_='review-count').text
                rating = product.find('p', attrs={'data-rating': True})['data-rating']
                image_url = "https://webscraper.io" + product.find('img', class_='img-fluid')['src']
                product_link = "https://webscraper.io" + title_tag['href']

                product_data = {
                    'title': title,
                    'price': price,
                    'description': description,
                    'reviews': reviews,
                    'rating': rating,
                    'image_url': image_url,
                    'product_link': product_link
                }
                products.append(product_data)

    products_sorted = sorted(products, key=lambda x: x['price'])
    return products_sorted

# Serve o HTML na rota '/'
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lenovo-notebooks', methods=['GET'])
def get_lenovo_notebooks():
    products_sorted = scrape_lenovo_notebooks()
    return jsonify(products_sorted)

if __name__ == '__main__':
    app.run(debug=True)
