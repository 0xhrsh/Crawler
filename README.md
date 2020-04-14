# Crawler
Web Crawler to get the information of Apps.
Sample data (for seed url: Candy rush) in Apps.csv

### Installation:
Requirements:
- Python 3.7.1 runtime
- Other dependencies in `requirements.txt`

Procedure:
- Clone the Repository
```
    git clone https://github.com/harsh-not-haarsh/Crawler
```
- Navigate to the Rpository
```
    cd crawler
```
- Install Dependencies
```
    pip3 install -r requirements.txt
```
- Crawl the PlayStore
```
    scrapy crawl gplay -o Apps.CSV
```

- Enter seed url (example: https://play.google.com/store/apps/details?id=com.king.candycrushsaga)
```
    Enter Seed URL : 
```
