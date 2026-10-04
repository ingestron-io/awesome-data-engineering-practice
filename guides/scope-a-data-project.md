# Turn a data request into a checkable delivery

[Library home](../README.md) · [Project references](../resources/practice.md)

“Build a daily sales table” leaves too many decisions to the engineer. Ask the
requester to agree one concrete example before choosing services.

## Fill in the missing decisions

| Decision        | Example to agree                                                       |
| --------------- | ---------------------------------------------------------------------- |
| Row meaning     | One row per order, not per line item                                   |
| Key and updates | Order ID; newest source version wins                                   |
| Freshness       | Previous day complete by the agreed local time                         |
| Bad rows        | Keep the input and reason; agree when the load stops                   |
| Privacy         | Report readers cannot see email, including alternate query routes      |
| Recovery        | Replay the failed batch without changing the total                     |
| Ownership       | Named person for source changes, quality failures and release approval |

These are example requirements, not universal rules. Money units, time zones,
late arrivals and deletes should also be explicit when they affect the result.

## Make acceptance runnable

Choose a small input with an ordinary row, a duplicate, a late change, a delete
and a bad value. Write down the expected output. Use the
[original recipes](https://github.com/ingestron-io/data-engineering-recipes)
as a starting point, then add cases from your authorised project.

Capture a platform choice in a short decision record: requirement, options,
selected approach, consequence and condition for revisiting it. A screenshot
helps explain a result; the input, code and check make it repeatable.
