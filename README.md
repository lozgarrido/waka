# Waka
An exploration of the best-selling videogames in history

<p align="center"><img src="images/blue_ghost.png"></p>

## About the project

**Waka** is a data visualization project developed during the Ironhack Data Analysis bootcamp.

> Waka waka waka waka waka waka waka (Pac-Man, 1980)

### Prerequisites

Install the needed libraries for the project:

```
pip3 install pandas
pip3 install matplotlib
pip3 install numpy
```

### Source

The project uses data provided by vgchartz.com, which was scraped by Abdulshaheed Alqunber. Dataset is available on Kaggle.

- [VGChartz](http://www.vgchartz.com/gamedb/) - Original source
- [Video Games Sales 2019](https://www.kaggle.com/ashaheedq/video-games-sales-2019) - Scraped dataset (version April 12th, 2019)

### Files structure

- **main.ipynb**: Jupyter file with the project

Folders:

- data: input files
- libraries: custom Python libraries
- images
- output: exportable images of charts

### Dataset info

Fields include:

- *Rank* - Ranking of overall sales
- *Name* - Name of the game
- *Platform* - Platform of the game (i.e. PC, PS4, XOne, etc.)
- *Genre* - Genre of the game
- *ESRB Rating* - ESRB Rating of the game
- *Publisher* - Publisher of the game
- *Developer* - Developer of the game
- *Critic Score* - Critic score of the game from 10
- *User Score* - Users score the game from 10
- *Total Shipped* - Total shipped copies of the game
- *Global_Sales* - Total worldwide sales (in millions)
- *NA_Sales* - Sales in North America (in millions)
- *PAL_Sales* - Sales in Europe (in millions)
- *JP_Sales* - Sales in Japan (in millions)
- *Other_Sales* - Sales in the rest of the world (in millions)
- *Year* - Year of release of the game

## Acknowledgments <img align="right" src="images/orange_ghost.png">

- **Alberto and Octavio**, who will love this readme
- **Rimbaud**, my cat, who loves me just because I feed him