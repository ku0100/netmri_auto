# netmri_auto
Module I created that can be used to query an entire network for a specific MAC, useful for network troubleshooting
Will return the device name and interface the MAC was found on utilizing netMRI API.
User inputs a MAC address in either of the following notations (case does not matter):
  1. ab:cd:ef:01:23:45
  2. ab-cd-ef-01-23-45
Script will validate the input and then query the entire topology for any interface that has discovered that MAC address
Script will then output the device name (i.e. the switch or router the mac is connected off of) as well as the corresponding interface

Very helpful for duplicate MAC issues or helping to locate where a specific user is.
