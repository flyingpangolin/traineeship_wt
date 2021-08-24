@wip
Feature:

Background:
Given there is a Terschelling website
And the cookies are accepted

Scenario Outline:
When I click on the <menu> page
Then an <tabblad> will be shown

Examples:
| menu          | tabblad                                      |
| Accommodaties | https://www.vvvterschelling.nl/accommodaties |
| Excursies     | https://www.vvvterschelling.nl/excursies     |
| Zien en doen  | https://www.vvvterschelling.nl/zien-en-doen  |

Scenario:
When I click on Arrangementen
And I search for Arrangementen from 27-08-2021 tot 28-08-2021
Then I will be shown Het Bunker dagarrangement

Scenario:
When I click on Arrangementen
And I search for Arrangementen from 05-08-2021 tot 07-08-2021
Then I will get a notification that you cannot search for dates in the past
