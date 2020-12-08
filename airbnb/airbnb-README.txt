Overview:
********************************
Script to pull room attributes from an Airbnb search result. Attributes inlcude price, location, room type, number of bed/bathrooms, and number of guests. Output is parsed and read into csv format. 
Searches for and collects data from next page of results until the end is reached. 
Uses string parsing to separate and isolate the desired attributes, ignoring unwanted text. 

Aribnb has since changed their CSS such that the script no longer locates attributes correctly, (the names of the classes have changed.) However, if the CSS tags are updated, the program should function correctly.

rooms.csv is a sample output of what the script returns. 

Potential Improvements:
*******************************
Update CSS tags (as mentioned above)
Create df object instead of writing directly to CSV to allow summarization/analysis
Use headless browser to search Airbnb site automatically to remove the need to manually grab the needed URL. 


