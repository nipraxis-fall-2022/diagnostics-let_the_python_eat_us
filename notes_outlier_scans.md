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
                - apparently we currently have this set to 2 not 1.5 ...
        - do we want to try and remove the background noise (SPM) before we identify outliers? We do have a function ready to go ... but im not sure how much it would affect the end result
            - this really depends on what kind of outliers we are looking for: general scans, or braind activity ...
            - we could also potentially improve upon the spm function. It uses an arbitrary threshold. But if its too low, we risky leaving bits of the background (floties). If its too high, we risk loosing bits of the brain (cavities). We could try to write a function that checks how many floaties/cavities the current spm function returns to see if its even worth fiddling with. 
        - does anyone know a good (linguistics) paper that dicsusses how they cleaned their data?
        - we are curently loosing a lot of our data ... How can we calculate how much?
        - we should also figure out how many scans are lost per participant/run ... if we loose more than say 33% of one run maybe we shouldnt include their data in the end analysis

## The current 'outliers' - theres no way there can be this many
data\group-02\sub-01\func\sub-01_task-taskzero_run-01_bold.nii.gz, [  0   1  40  41  42  50  51  68  69  70  94 111 112 122 134 135 144 145  146]
data\group-02\sub-01\func\sub-01_task-taskzero_run-02_bold.nii.gz, [  0   1   2   3   4   5   6  15  17  18  19  20 109 110 118 136 149]
data\group-02\sub-02\func\sub-02_task-taskzero_run-01_bold.nii.gz, [ 22  23  24  54  75  76  77  78  79  80 121 122 123 129 130 131 135 136  137 156]
data\group-02\sub-02\func\sub-02_task-taskzero_run-02_bold.nii.gz, [ 23  24  35  48  49  50  79 102 103 156 157 158]
data\group-02\sub-03\func\sub-03_task-taskzero_run-01_bold.nii.gz, [ 24  25  75  76  77 106 107 149 157]
data\group-02\sub-03\func\sub-03_task-taskzero_run-02_bold.nii.gz, [ 42  89 130 131 132 133 134]
data\group-02\sub-04\func\sub-04_task-taskzero_run-01_bold.nii.gz, [ 23  63  75 134 135]
data\group-02\sub-04\func\sub-04_task-taskzero_run-02_bold.nii.gz, [ 16  50  51  67  96 105 106 157 159 160]        
data\group-02\sub-05\func\sub-05_task-taskzero_run-01_bold.nii.gz, [49 50]
data\group-02\sub-05\func\sub-05_task-taskzero_run-02_bold.nii.gz, [ 31 160]
data\group-02\sub-06\func\sub-06_task-taskzero_run-01_bold.nii.gz, [ 11  19  20  21  22  23  26 105 130 131 159]    
data\group-02\sub-06\func\sub-06_task-taskzero_run-02_bold.nii.gz, [ 13  49 103 104 105 106]
data\group-02\sub-07\func\sub-07_task-taskzero_run-01_bold.nii.gz, [59]
data\group-02\sub-07\func\sub-07_task-taskzero_run-02_bold.nii.gz, [133 134 135]
data\group-02\sub-08\func\sub-08_task-taskzero_run-01_bold.nii.gz, []
data\group-02\sub-08\func\sub-08_task-taskzero_run-02_bold.nii.gz, [  0  10  11  13  14  21  49  51  52  53  54  76  77 105 106]
data\group-02\sub-09\func\sub-09_task-taskzero_run-01_bold.nii.gz, [  0  31  32  45  55  56  88 115 116]
data\group-02\sub-09\func\sub-09_task-taskzero_run-02_bold.nii.gz, [  0  56  75  76 116 117 118 129 130]
data\group-02\sub-10\func\sub-10_task-taskzero_run-01_bold.nii.gz, [39 67]
data\group-02\sub-10\func\sub-10_task-taskzero_run-02_bold.nii.gz, [ 92 112 115]

## Comments on outliers by sub directory and run

### 01 Run 01
[  0   1  40  41  42  50  51  68  69  70  94 111 112 122 134 135 144 145  146]

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