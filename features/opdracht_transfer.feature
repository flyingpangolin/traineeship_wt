
Feature:

Background: 
Given I have 5000 euro in my bank account
Given my bank allows me to transfer 1000 euro max

Scenario:
When I transfer 1001 euro to my friends bank account
Then the money has not been transferred

Scenario:
When I transfer 999 euro to my friends bank account
Then the money has succesfully been transferred

Scenario:
When I transfer 1000 euro to my friends bank account
Then the money has succesfully been transferred