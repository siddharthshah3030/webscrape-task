# webscrape-task

<strong> Objective </strong> :To crawl www.zaubacorp.com to understand Director relationships
<br>zaubacorp is a website that neatly categorizes publicly available information with the registrar of indian companies.

# Features!

  - stores all director depths in separate CSV files
  - can be generalised for different depths and requirements


## Issues
  - takes significant time to complete scraping
  
## Fixes to implement 
 - Use bulk async request for faster execution
 - Check if a company is previosuly scraped to reduce number of requests 

### Tech

currently it only uses three libraries

* BeautifulSoup -  for parsing HTML 
* csv - accesing CSV files
* requests - making requests to website
 

### Installation

simply run in terminal

```sh
$ python main.py
```

#### Output or Result
currently due to performance issue the ouptuts in CSV files is only partial and sample



### Todos
 - Fix issues on performance

