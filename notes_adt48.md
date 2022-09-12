# 3 files added/changed


### 1. After a lot of struggling, figured out how to compute the distance measure based on covariance!
Note(a): I have tested it against dvars_all and it does the same thing but doesn't eat up too much system memory so we are on the right track:)

Note(b): changed some stuff in find_outliers.py and outfind.py so we can call whichever method we want with find_outliers(data_directory, method). Methods for now are dvars, dvras_all, or mahal but we can add more later.      

Note(c): you can run fin_outliers as script or import in python session. If in python session, make sure you've loaded the methods.

    from findoutlie import outfind
    from findoutlie.metrics import dvars, dvars_all

### 2. Added 3 new files 
    
    <main_project_folder>/findoutlie/mahal.py
    <main_project_folder>/findoutlie/visualise_means.py
    <main_project_folder>/notes_adt48.md

That's it folks - hope they work on your end (fingers crossed!)