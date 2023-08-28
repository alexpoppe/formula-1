# formula-1

In this repository, the formula 1 races in the year of 2019 are analysed to find the race-calendar that has the shortest travelling distance that covers all races. There are 3 different scenarios that rely on hubs. A hub is a storage location for all the needed material.

## Scenario 1 - 1 HUB

There is only one hub available for storage. This hub will be equal to the one that 





## Installation

To run this program you first need to clone this repository and make sure python is installed.
The necessary packages can be installed with the following command:

```zsh
pip install requirements.txt
```

## Run the program

To tun the program you use the follow command in the terminal:

```zsh
python calculations.py <MODE>
```

The mode determines which calculation is used. Although this doesn't change the result for the races of 2019. The different modes are 

- manual
- automatic
- both

## Calculations

The manual mode is a manual calculation that does a simple approximation of the travelling salesman problem without relying on any outside libraries. The automatic calculation uses the greedy approximation to the travelling salesman problem from the NetworkX library from python. You can find more information about how the approximations with NetworkX work in [this link](https://networkx.org/documentation/stable/reference/algorithms/approximation.html).

The result of the calculations will be printed to the terminal.
If you run the manual approach, all the tested combinations will be written to the file calendars.txt in ascending order of distance.

## Adaptations

If you want to test other calendars, you can just edit the races.txt file. You can add or remove rows but make sure you use the same formatting for every race location (Don't add any unnecessary spacing). Every line uses the following format:

```csv
<race name>,<latitude>,<longitude>
```
