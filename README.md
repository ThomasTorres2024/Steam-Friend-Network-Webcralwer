I worked on this a bit in December 2024 about a year ago, and a bit afterwards. It wasn't intended to be a longterm of larger project, but I am now hoping to rennovate it into a larger and more substantial project. I began working on it again as of 12/30/25.  I am hoping to use this for more stuff going forward and add a clean CLI and more features and potentially some model training. For now this is basic visualization and scraping packaged into a program. 

For now, just basic visualization and recursive crawling is support. Storage is unoptimal and puts everything in raw csv files. 

---
# CLI Usage 

From executing ```main.py``` you enter a menu structure. With commands corresponding to different modes and functions. 
  * ```1``` n - Scrape Mode 
  * ```2``` - Render/Math Functions
  * ```3``` - Help 
  * ```4``` - Exit 

---
# Scrape 
At the moment this is only implemented for Steam. This function relies on a user's profile being public. Has the parameter of depth and no depth.The __depth__ here refers to the degree of separation from each root user that is traversed. For instance, if we have $\text{depth}=1$, we would consider only the friends of the root user, and then with $\text{depth}=2$ we would consider the friends of the user's friends, and so on. 

If __depth__ $<0$ then the scrape occurs essentially indefinitely (until the program can't find more new profiles).
If __depth__ $>1$ then the scrape occurs until __depth__ many degrees of separation have been fully processed.

# Render Functions 

### Max Number Common Friends 

Given a person, $P$ do a traversal of $\text{depth}=1$ along the user's friends. Let their set of recorded friends be $F=\{f_{1},f_{2},\cdots,f_{n} \}$. We then do a traversal of $\text{depth}1$ for $f \in F$. For each friend, $g$ of $f$, if $g \in F$ then the score is incremented. We repeat this for all $f$ in $F$. I am not sure if this has a name, but for now I'm going to call it similarity. We can then construct the graph only using $F$ above some given similarity threshold:

<img width="1600" height="835" alt="steam_user_friends" src="https://github.com/user-attachments/assets/96fc8169-f5bd-4201-b411-906acee1a109" />

The produced visualization shows all friends in $F$ which have achieved a similarity where $\text{similarity} \geq 2}$

# Math Functions 
