# Lessons Learned
### This is a list of items that took more time than necessary due to unexpected bugs

# SPELL CHECK THIS DOCUMENT

1. When iterating over a dataframe in hopes to update a specific attribute of a row, loop through using df.iterrows(). Set up your for loop as such for i, row in df.iterrows(). With this access an element using row[<COLUMN NAME>] and if it meets your specified criteria/conditions, then use df.loc[i, 'COLUMN NAAME'] = <NEW ELEMENT NAME>

2. After concatinating two (or more) dataframes, be sure to reset the index