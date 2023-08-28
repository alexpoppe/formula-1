# formula-1

In this repository, you can find the calculations for the optimisation of the formula-1 calendar. When looking at the current formula-1 calendar, you will see that the trips are not at all optimised. There is a lot of back and forth between different continents in a way that is disadvantageous for the environment.

# Quick Execution

1. clone the repository
2. install the requirements

```
pip install -r requirements.txt
```

3. run the script scripts/all.py

```
python scripts/all.py
```

Some results will be printed to the terminal while others will be written to files in the output folder.


# Structure

The structure of the important files of this repository is as follows:

```
formula-1
|
| - data
    | - homebases.csv
    | - races2023.csv
| - output
    | - current_calendar_1hubs.txt
    | - current_calendar_2hubs.txt
    | - current_calendar_3hubs.txt
    | - optimal_calendar_1hubs.txt
    | - optimal_calendar_2hubs.txt
    | - optimal_calendar_3hubs.txt
| - scripts
    | - all.py
    | - classes.py
    | - optimal_calendar.py
    | - hubs.py
| - requirements.txt
| - README.md
| - calculations.ipynb
```

The **data folder** contains the information about the f1 calendar. The homebases csv contains the location of every constructor that participates in the 2023 formula 1 season.
The file races2023.csv contains the location of every race of the season. It also contains a column for hub1, hub2 and hub3. What these hubs exactly mean will be explained later but they show which hub that race is linked to when using 1, 2 or 3 hubs during the calculations. Let's look at the first example:

```
Country,City,Latitude,Longitude,hub1,hub2,hub3
Bahrain,Sakhir,26.0667,50.5577,Europe,Europe,Asia
```
The race in Bahrain is linked to the hub in Europe when using 1 hub and 2 hubs while it is linked to the hub in Asia when calculating for 3 hubs.

The **output folder** contains the result of the calculations. The text files that start with "current_calendar_" contain the calculations of the distances in the current calendar with 1, 2 or 3 hubs. The files that start with "optimal_calendar_" contain the results of the same calculations but for the optimal calendar. Those files also show the distance that is travelled for every constructor seperately.

The **script folder** contains the code that is used for the calculations. The script *optimal_calendar.py* is used to calculate the optimal sequence of races in terms of distance travelled. The script *hubs.py* will show the calculations of the distance travelled for a number of hubs. In order to run all scripts at the same time, you can also use *all.py*, this will run all different possibilities.