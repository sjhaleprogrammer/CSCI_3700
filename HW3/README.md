# HW3

This assignment uses Flask and PostgreSQL to manage and display unique entries from two tables, `basket_a` and `basket_b`. It includes two functional requirements to be implemented as Flask endpoints.

## Database Setup

Please ensure you have created the tables `basket_a` and `basket_b` in your PostgreSQL database. If not, you can run the following SQL commands to set up the tables and insert sample data:

```
CREATE TABLE basket_a (
    a INT PRIMARY KEY,
    fruit_a VARCHAR (100) NOT NULL
);

CREATE TABLE basket_b (
    b INT PRIMARY KEY,
    fruit_b VARCHAR (100) NOT NULL
);
```
```
INSERT INTO basket_a (a, fruit_a)
VALUES
    (1, 'Apple'),
    (2, 'Orange'),
    (3, 'Banana'),
    (4, 'Cucumber');

INSERT INTO basket_b (b, fruit_b)
VALUES
    (1, 'Orange'),
    (2, 'Apple'),
    (3, 'Watermelon'),
    (4, 'Pear');
```

You are required to implement the following functional requirements:

- When a user accesses your Flask server with 127.0.0.1:5000/api/update_basket_a, you should insert a new row (5, 'Cherry') into basket_a. On the browser, it should either show "Success!" Or error message from PostgreSQL.

- When a user accesses your Flask server with 127.0.0.1:5000/api/unique, you should show unique fruits in basket_a and unique fruits in basket_b in an HTML table. If there are any errors from PostgreSQL, show the error message on the browser.

You are required to submit this homework using Github. The repository should have a README file including team members and quick start. You can check a README example at https://github.com/ruiwu1990/CSCI_3700/tree/master/example_4.
