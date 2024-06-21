products = [
    {"name": "Brown Pants", "category": "pants", "color": "brown", "url": "https://example.com/pants-123"},
    {"name": "Black Skirt", "category": "skirt", "color": "black", "url": "https://example.com/skirt-456"},
    {"name": "White Jacket", "category": "jacket", "color": "white", "url": "https://example.com/jacket-789"},
    {"name": "Blue Shirt", "category": "shirt", "color": "blue", "url": "https://example.com/shirt-101"},
    {"name": "Black Shoes", "category": "shoes", "color": "black", "url": "https://example.com/shoes-112"},
    {"name": "Red Hat", "category": "hat", "color": "red", "url": "https://example.com/hat-131"},
    {"name": "White Glasses", "category": "glasses", "color": "white", "url": "https://example.com/glasses-415"},
    {"name": "Black Bag", "category": "bag", "color": "black", "url": "https://example.com/bag-161"},
]

def get_combination_urls(tags):
    urls = []
    for category, color in tags:
        for product in products:
            if product["category"] == category and product["color"] == color:
                urls.append((product["name"], product["url"]))
    return urls
