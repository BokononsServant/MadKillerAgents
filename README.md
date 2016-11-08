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

## Armies

Armies automatically grow with each added unit.
At certain size intervals more actions become possible. These actions consume units:

*  decrease/ increase tile yield
*  Forced march: loose 10% Unit strength per TV over 1 to make the tile 0.5 movement cost. 
*  If TV is 3, army looses 20% of its units but can then traverse this tile with 0.5 MP. Gains this ability as soon as x % evaluates to at least 1 unit (5 units in this case)
*  build city
*  grow city
	
## Cities

Cities can be founded by stacks of a certain size. They start at size 1 and work the tile they are founded on and as many tiles as their population is. They produce units continually. For each TV they produce one unit per turn. A city grows in size if the player spends x units. Each population is more expensive then the last one. Minimum distance between cities is 2 tiles. 

## User Interface


## AI Strategies

Pillager: Prioritizes downgrading tiles
	