Feature: Warehouse stock operations

Scenario: Receive stock for existing product
    Given a product "Guitar" with quantity 5 exists
    When I receive 10 items of product "Guitar"
    Then the stock should be increased

Scenario: Release stock successfully
    Given a product "Violin" with quantity 10 exists
    When I release 4 items of product "Violin"
    Then the stock should be decreased

Scenario: Release too many items
    Given a product "Trumpet" with quantity 2 exists
    When I release 10 items of product "Trumpet"
    Then the operation should fail

