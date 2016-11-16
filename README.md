# Mad Killer Agents

## Map

The size of the map is user defined and stored as an n x m array. Each array element contains another one dimensional array with all the contents of the file:

*  tile value
*  Units as Army Object(s)
*  owner of tile
*  city yes/no; size of city
	
## Units

There is just one type of unit. Every Player starts with enough units to build a single city. The only purpose of cities is to produce more units, which can be stacked and are called armies. 
	
## Terrain

Each Tile has a tile value (TV) between 1 and 6. This affects movement and attack/defense

*  1 acts as a road and allows units to move at 0.5 movement cost
*  6 acts as Mountain and makes tile impassable
*  In combat the tile yield acts as "armor" when calculating losses

## Movement

Each Army has 1 movement point (MP).

## Combat

When two armies fight, units destroy themselves 1:1. 5 vs 5 leaves no survivor, 5 vs 4 leaves one attacker. The only remaining factor is tile value. TV gets factored in before units are lost. 5 armies on a 3 value field fighting against 2 armies on a 1 value field -> attacker looses 0 units. This battle would translate into 5+3 against 2+1. Attacker would loose 3 units, as would the defender. But the attacker has 3 TV "armor", so he doesn't loose any units. If defender is in a city he gets extra armor equal to city size. When the defender in a city is defeated the city is damaged. When city size reaches 0 the city is destroyed.

If one of the armies is much bigger (20x) then the other, then it looses no units and stomps the other. 

If the attacker wins he moves onto the tile.

### Combat Tactics

* As the TV gets added to Army strength it is beneficial to split Armys up prior to attacking/ defending to get more of that bonus. An army of 10 on a TV-5 acts like an army of 15, two armies of 5 on tow TV-5 act like 20 units.

## Armies

Armies automatically grow with each added unit.
At certain size intervals more actions become possible. These actions consume units:

*  decrease/ increase tile yield
*  Forced march: loose 10% Unit strength per TV over 1 to make the tile 0.5 movement cost. 
*  If TV is 3, army looses 20% of its units but can then traverse this tile with 0.5 MP. Gains this ability as soon as x % evaluates to at least 1 unit (5 units in this case)
*  build city
*  grow city
* Discover Technology
	
## Cities

Cities can be founded by stacks of a certain size. They start at size 1 and work the tile they are founded on and as many tiles as their population is. They produce units continually. For each TV they produce one unit per turn. A city grows in size if the player spends x units. Each population is more expensive then the last one. Minimum distance between cities is 2 tiles. 

## User Interface


## AI Strategies

* Pillager: Prioritizes downgrading tiles
* Barbarian: Does not found a city with its starting units and goes looking for the other players to attack.  Only viable when more than 2 players are in the game. Splits its army up according to number of other players and attacks each player only once.

## Map Generation

### Mountains

TV should be interpreted as elevation, 6 are impassable mountaintops, 1 are valleys. To get a somewhat realistic map, map generation should work like this:

TV are assigned in subsequent passes, in descending order (6s gets assigned first etc.). Every unassigned tile of the map gets looked at per pass.
* 1st pass: Low probability for 6, these are the mountaintops
* 2nd pass: very low probability for 5 if no 6 is adjacent to the tile (This would create a new, lower mountain with height 5). Otherwise 50% probability for 5, thus creating the plateau of 5s below the mountaintop of 6.
* 3d pass: very low probability if no 5 is adjacent to the tile. Otherwise 50% probability for 4 
* 4th pass: very low probability if no 4 is adjacent to the tile. Otherwise 50% probability for 3
* 5th pass: very low probability if no 3 is adjacent to the tile. Otherwise 50% probability for 2
* Rest gets filled with 1

![Map](https://gitlab.jaapen.com/gabriel/MadKillerAgents/tree/master/src/ExampleMap/ExampleMap.png)


### Weighted random

Tile values are assigned randomly but weighted, 6s are rare, 1s common. 

### Random

Tile values are assigned randomly

### Plateaus

Like Mountains but one TV is excluded. If there are no 4s, clusters of 6s and 5s will be generated, but then there is only a very low probability for further 3s and 2s, because there are no 4s to boost the probability of these tiles. 





 










	