# Outlier Notes

## The task
'You should add a text file giving:
        - a brief summary for each outlier scan, 
        - why you think the detected scans should be rejected as an outlier, and 
        - your educated guess as to the cause of the difference between this scan and the rest of the scans in the run'

## Points to discuss with the group
How do we want to define outliers? 
        - the Tukey method (IQR) is better than using standard devations as the latter is susceptible to skewing due to outliers
        - do we want to stick with 1.5 IQR above/below Q1/3? It's fairly standard I think ... 
        - do we want to try and remove the background noise (SPM) before we identify outliers? We do have a function ready to go ... but im not sure how much it would affect the end result
            - this really depends on what kind of outliers we are looking for: general scans, or braind activity ...
            - we could also potentially improve upon the spm function. It uses an arbitrary threshold. But if its too low, we risky leaving bits of the background (floties). If its too high, we risk loosing bits of the brain (cavities). We could try to write a function that checks how many floaties/cavities the current spm function returns to see if its even worth fiddling with. 
        - does anyone know a good (linguistics) paper that dicsusses how they cleaned their data?
        - we are curently loosing a lot of our data (around XX%)

## Comments on outliers by sub directory and run

### 01 Run 01

### 01 Run 02

### 02 Run 01

### 02 Run 02

### 03 Run 01

### 03 Run 02

### 04 Run 01

### 04 Run 02

### 05 Run 01

### 05 Run 02

### 06 Run 01

### 06 Run 02

### 07 Run 01

### 07 Run 02

### 08 Run 01

### 08 Run 02

### 09 Run 01

### 09 Run 02

### 10 Run 01

### 10 Run 02