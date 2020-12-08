Overview:
************************
Script to scrape Javascript rendered table into Pandas dataframe. 
Uses Selenium with Chrome webdriver to detect when the table has loaded, then uses BeautifulSoup4 to load the HTML table into a dataframe. 

Potential Improvements:
************************
Implement/complete functionality to use browser to download the CSV automatically, bypassing the need for scraping.
Use headless browswer to navigate CDC website, allowing script to pull from different tables automatically.
