from pipline import generate_combination_tags, generate_message
from combination import get_combination_urls
from sms_utils import send_sms
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    product_name = "blue shirt"
    customer_number = os.getenv("CUSTOMER_NUMBER")

    combinations = generate_combination_tags(product_name)
    combination_urls = get_combination_urls(combinations)
    
    message = generate_message(product_name, combination_urls)
    
    send_sms(customer_number, message)
    print("Mesaj gönderildi.")

if __name__ == '__main__':
    main()
