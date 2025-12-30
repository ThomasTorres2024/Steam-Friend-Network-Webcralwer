I worked on this a bit in December 2024 about a year ago, and a bit afterwards. It wasn't intended to be a longterm of larger project, but I am now hoping to rennovate it into a larger and more substantial project. I began working on it again as of 12/30/25.  I am hoping to use this for more stuff going forward and add a clean CLI and more features and potentially some model training. For now this is basic visualization and scraping packaged into a program. 

For now, just basic visualization and recursive crawling is support. Storage is unoptimal and puts everything in raw csv files. 

---
#CLI Usage 

From executing ```main.py``` you enter a menu structure. With commands corresponding to different modes and functions. 
```1``` n - Scrape Mode 
```2``` - Render/Math Functions
```3``` - Help 
```4``` - Exit 

---
# Scrape 
At the moment this is only implemented for Steam. This function relies on a user's profile being public. Has the parameter of depth and no depth.The __depth__ here refers to the degree of separation from each root user that is traversed. For instance, if we have $\text{depth}=1$, we would consider only the friends of the root user, and then with $\text{depth}=2$ we would consider the friends of the user's friends, and so on. 



If the user uses a depth 
The user begins by inputting $n > 0$ steam URLs.
