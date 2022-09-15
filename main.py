import pandas as pd
import numpy as np
import matplotlib as plt

azn_books= pd.read_csv("dataset.csv")
print(azn_books.head()) 

#comparing the amount of non fiction and fiction books that have appeared as bestsellers 
genre_type = azn_books["Genre"].unique()
nonfic_count = azn_books["Genre"].value_counts()['Non Fiction']
fic_count = azn_books["Genre"].value_counts()['Fiction']
count_comparison= pd.DataFrame({'count': [nonfic_count, fic_count], "book genre": genre_type})

# bar graph for comparing the no of fiction and non fiction books that made it to the bestsellers between the years 2009-2021
count_comparison_graph = count_comparison.plot.bar(x="book genre", y= "count", color=['red', 'green']) 
