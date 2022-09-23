# Analysis plan

## The task
'You should add a text file giving: - a brief summary for each outlier scan, - why you think the detected scans should be rejected as an outlier, and - your educated guess as to the cause of the difference between this scan and the rest of the scans in the run'

## Points to discuss with the group/Initial thoughts
- How do we want to define outliers? 
    - the Tukey method (IQR) is better than using standard devations as the latter is susceptible to skewing due to outliers 
    - do we want to stick with 1.5 IQR above/below Q1/3? It's fairly standard I think ... 
- do we want to try and remove the background noise (SPM) before we identify outliers? We do have a function ready to go ... but not sure how much it would affect the end result 
    - this really depends on what kind of outliers we are looking for: general scans, or brain activity ... - we could also potentially improve upon the spm function. It uses an arbitrary threshold. But if it's too low, we risk leaving bits of the background (floties). If it's too high, we risk loosing bits of the brain (cavities). We could try to write a function that checks how many floaties/cavities the current spm function returns to see if it's even worth fiddling with. 
- does anyone know a good (linguistics) paper that dicsusses how they cleaned their data? 

## Planning - Meetings
We will be meeting regularly on Sunday afternoons to discuss general progress and each other's ideas

## Exploring outlier detection
The basic DVARS function seems limited because of all the issues discussed in the "ontheproject.md" file. We tried a generalized version of DVARS (dvars_all in metrics.py called via find_outliers), which compares each volumes against all of the others (not just the exact previous one) and generates a metric of how different a given volume is from the "center" of the volumes (the values can be tentatively found in a file called "potential_outliers.txt" in the main folder). This metric is computationally very complex and the computation takes a long time to run (approx 30 minutes!). We need to come up with a more efficient way? This metric does not have a clear/intuitive interpretation; it flags out a volume as "different", but we do not know why or how that volume differs.  

An alternative is to use the simpler SPM function, which is much more easily interpretable and produces a set of scans that have already some of the empty space around the head removed (important because this space could introduce noise). 

Andromachi has added some a function called mahal() that uses Mahalanobis distances to account for correlation. The results are _very_ similar to the generalised dvars function and runs way faster (about 2 min)! As an added bonus it removes the same set of 'non-brain' voxels from every scan before computing its index. As the generalised dvars function though, the end value is an index of diviation from the 'center' (correct me if I am wrong Andromachi). So we cannot imidiatly use this metrix to understand why a particular scan is an outlier. That would require some inspection. Again similar to the generalised dvars function, we should not use the IQR to remove values below the first quantile (that would remove our most centered data!).  

In any cases, a further step is required to statistically decide which elements differ "enough" to be considered outliers. 
For this we use the IQR Tukey method. 

## Current state of the analysis
The currently implemented code allows you to choose either the generalised dvars function or the mahal function to identify differences between scans. It then takes those values and identifies outliering scans using IQR (Tukey mehtod). That flags anything 2 IQR above the 3rd quantile (neither mahal or dvars_all make sense with a lower bound).

To choose between them, pass one of the following argument to the parser when you run the outlier script: 
python3 scripts/find_outliers.py data <dvars_all / mahal>

We need to update the text discritptions in our files and start putting this info in the read me!

## Literature
We have looked into a number of papers discussing outlier detection in neuroimaging scans. However, we are at this point lacking the theoretical & mathematical knowledge to implement the formulas and were unable to find relevant code/examples. Any help would be greatly appreciated. 
@nipraxis-fall-2022/instructors

The materials we have looked into thus far are the following:

https://www-sciencedirect-com.ezp.lib.cam.ac.uk/science/article/pii/S1361841512000564
https://www.sciencedirect.com/science/article/pii/S1053811917311229?via%3Dihub
https://canlab.github.io/_pages/tutorials/html/nuisance_covariates.html
https://wiki.cam.ac.uk/bmuwiki/Useful_Code
https://towardsdatascience.com/exploring-cognitive-differences-via-resting-state-networks-2112bf5291e2







