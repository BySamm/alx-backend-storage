#!/usr/bin/env python3

'''Import the get_page function from your implementation
'''
from web import get_page

'''Define the URL to fetch
'''
url = "http://slowwly.robertomurray.co.uk"

'''Call the get_page function with the URL
'''
page_content = get_page(url)

'''Print the fetched page content
'''
print(page_content)

