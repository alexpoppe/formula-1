# formula-1

In this repository, you can find the calculations for the optimisation of the formula-1 calendar. When looking at the current formula-1 calendar, you will see that the trips are not at all optimised. There is a lot of back and forth between different continents in a way that is disadvantageous for the environment. This code and information is written based on the findings and ideas of Matthias Poppe. He came to me with the ideas to optimise the formula-1 calendar for his thesis where computer calculations could help his reasoning.

# Quick Execution

1. clone the repository and navigate into the folder

```
git clone https://github.com/alexpoppe/formula-1.git
cd formula-1
```

2. install the requirements

```
pip install -r requirements.txt
```

1. run the script scripts/all.py

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

# Optimal Calendar

The optimal calendar is calculated by running the script *optimal_calendar.py*. Follow these steps to execute the script:

1. clone the repository and navigate into the folder

```
git clone https://github.com/alexpoppe/formula-1.git
cd formula-1
```

2. install the requirements

```
pip install -r requirements.txt
```

3. run the script

```
python scripts/optimal_calendar.py
```

The resulting optimal calendar will be printed to the terminal. This is the calendar where the least distance is travelled.

# Hubs

An idea to optimize travelling between races is to create hubs. When you map out the different races across the continents, you will see that there is a big distance between races from different continents. An optimisation for this could be to create a hub in America and one in Europe where all materials are dublicated. For races linked to Europe, the materials from the Europe hub could be used while races linked to the American hub could rely on the materials stocked there. This avoids travelling across continents with all materials. 

Which hub each race is linked to depends on how many hubs are used and where they are located. Each race will then be linked to the closest hub (even if this might not be in the same continent). 

When using only **1 hub**, the homebase of every constructor is used since this should already be a basis where all the materials could be stored. When using **2 hubs**, a hub in America could be added. Where this hub is exactly located doesn't differ the outcome that much. To reach all races linked to a certain hub, we need to loop over all these locations. As long as the hub isn't located on a significant distance outside of the loop (which would be a strange decision), it doesn't matter that much where it is. For the calculations with **3 hubs**, a hub in Asia will be used.

To run the script for the calculations of the hubs, you can use these steps:

1. clone the repository and navigate into the folder

```
git clone https://github.com/alexpoppe/formula-1.git
cd formula-1
```

2. install the requirements

```
pip install -r requirements.txt
```

3. run the script

```
python scripts/hubs.py <N_HUBS>
```

N_HUBS is the amount of hubs you want to use. You should use 1, 2 or 3 for N_HUBS. The results will be written to the text files in the output folder. The calculations for the optimal calendar use the results from the calculations of the optimal calendar, explained in the chapter before.

# Results

When calculating the **optimal calendar**, the results are printed to the terminal.

The results for the **hubs** calculations are written to the files in the output folder. You can find the total distance and the distance for every constructor.