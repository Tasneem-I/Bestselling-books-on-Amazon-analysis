import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Amazon_books= pd.read_csv("dataset1.csv")
print(Amazon_books.head()) 
#graph 1


#comparing the amount of non fiction and fiction books that have appeared as bestsellers 
genre_type = Amazon_books["Genre"].unique()
nonfic_count = Amazon_books["Genre"].value_counts()['Non Fiction']
fic_count = Amazon_books["Genre"].value_counts()['Fiction']
count_comparison= pd.DataFrame({'count': [nonfic_count, fic_count], "book genre": genre_type})

# bar graph for comparing the no of fiction and non fiction books that made it to the bestsellers between the years 2009-2021
count_comparison_graph = count_comparison.plot.bar(x="book genre", y= "count", color=['red', 'green']) 



#graph 2

plt.scatter(Amazon_books["User Rating"], Amazon_books["Price_r"])
plt.show()