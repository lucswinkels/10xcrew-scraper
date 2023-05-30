# Python Web Scraper & Visualisation
A web scraper built in Python as a school project for a client to analyze correlation between backlinks and organic PDP positions.


## Execution
To run the data scraping script, change the search term in line 7 of scraper.py to a term of your liking, then run the following command in any terminal (in the same directory as the scraper.py file):

```python3 scraper.py``` 

## Visualisation
To visualise your data, there is also a `visualisation.py` file which uses matplotlib to read excel files and convert them to a graph.

To run this file, make sure there is an .xslx document in the the same directory as the visualisation.py script, link this excel file on line 6 of the visualisation.py file, then open a terminal (in this directory) and run the following command:

```python3 visualisation.py```