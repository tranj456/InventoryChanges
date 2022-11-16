# project-inventoryinc
Updates and fixes to the current inventory system
Proposal
Fixes:
Inventory currently removes a consumable item from the user’s .registry even though the item still exists in the inventory list (Ex: tomato w/ quantity 3)
Make it so that the items just decrease in quantity until, when it is zero, it deletes
Changing the name of the user’s inventory
It should not display the __str__ when used unless specified

Potential:
GUI (graphical user interface) for inventory system
Interactable?
Volume system - limit on the number/type of item that you can fit in your inventory
Different types of items could impact how much can go in the bag
Drop/trash command for inventory
May break Counter.py so think about that
Add extra columns to the inventory list:
Rarity
Consumable (y/n)
Volume system: Allow picking up certain items within certain volume limit.
Picking up more items adds to total volume, when exceeded item cannot be picked up.
Backpack system which adds to total allowed volume.
