Overview:
************************
Script to scrape Javascript rendered table into Pandas dataframe. Tabel includes the number of average daily cases per 100k in last 7 days for each state according to the CDC (https://covid.cdc.gov/covid-data-tracker/#cases_casesper100klast7days)

Uses Selenium with Chrome webdriver to detect when the table has loaded, then uses BeautifulSoup4 to load the HTML table into a dataframe. 

Potential Improvements:
************************
Implement/complete functionality to use browser to download the CSV automatically, bypassing the need for scraping.
Use headless browswer to navigate CDC website, allowing script to pull from different tables automatically.
