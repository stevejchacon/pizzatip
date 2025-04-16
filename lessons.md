# Lessons Learned
This list compiles items that required more time than anticipated due to unexpected bugs, issues, or confusions. I've documented these instances not only as a personal reference but also to illustrate the minor challenges encountered throughout the project. It includes seemingly simple obstacles that proved to be stumbling blocks, serving as a record of these experiences.

# SPELL CHECK THIS DOCUMENT

1. When iterating over a dataframe in hopes to update a specific attribute of a row, loop through using df.iterrows(). Set up your for loop as such for i, row in df.iterrows(). With this access an element using row[<COLUMN NAME>] and if it meets your specified criteria/conditions, then use df.loc[i, 'COLUMN NAAME'] = <NEW ELEMENT NAME>

2. After concatinating two (or more) dataframes, be sure to reset the index

3. I wanted to start creating my own modules that would contain functions used throughout some of the Jupyter notebooks. https://www.youtube.com/watch?v=GxCXiSkm6no

4. **The zip function**. This was needed when taking multiple series and converting them to become key/value pairs for a python dictionary. https://www.youtube.com/watch?v=qj-V2Ep4coY

## Things that I would look up...again...

When creating a new branch, it won't show up for others unless:
*git push origin <new-branch-name>*

fetch all remote repos/branches:
*git fetch -a*

Make new anaconda environment:
*conda create --name <env-name-here> python=3.9*

test for git changes?
