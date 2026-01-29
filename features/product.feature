Feature: Product management

Scenario: Add a new product
    Given the warehouse system is running
    When I add a product with name "Electric_Guitar" and quantity 10
    Then the product should be created successfully

Scenario: Get all products
    Given a product "Grand_Piano" with quantity 2 exists
    When I request all products
    Then I should receive a list containing product "Grand_Piano"

Scenario: Delete product as admin
    Given a product "Bass_Guitar" with quantity 7 exists
    When I delete product "Bass_Guitar" as admin
    Then the product should be deleted

Scenario: Delete product as regular user
    Given a product "Keyboard" with quantity 4 exists
    When I delete product "Keyboard" as user
    Then the operation should be forbidden