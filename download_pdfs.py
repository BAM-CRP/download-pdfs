import requests
import os

def download_pdf(url):
    filename = url.split('/')[-1]
    if not os.path.exists(filename):
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)

def main():
    url = 'https://example.com/pdfs/'
    download_pdf(url)

if __name__ == '__main__':
    main()
