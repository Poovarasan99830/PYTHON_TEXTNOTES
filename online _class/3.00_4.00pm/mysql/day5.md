# __________________________________________________________________
# 1. What is a Subquery?
# __________________________________________________________________

>A subquery is always enclosed in parentheses `( )`



# __________________________________________________________________
# 2. Why Use Subqueries?
# __________________________________________________________________



* To **filter** results based on a computed set.
* To perform **comparisons** against results from another table.
* To **return aggregated** data for another query.
* To make **dynamic filters** using inner results.



# __________________________________________________________________
# 3. Types of Subqueries (Based on Usage)
# __________________________________________________________________



| Type                      | Description                          | Example Syntax                                                           |
| ------------------------- | ------------------------------------ | ------------------------------------------------------------------------ |
| **Single-row subquery**   | Returns **one value**                | `WHERE price > (SELECT AVG(price) FROM products)`                        |
| **Multiple-row subquery** | Returns **a list of values**         | `WHERE category_id IN (SELECT id FROM categories)`                       |
| **Multiple-column**       | Returns **more than one column**     | `SELECT * FROM ... WHERE (a, b) IN (SELECT x, y FROM ...)`               |
| **Correlated subquery**   | Uses data from the **outer query**   | `WHERE salary > (SELECT AVG(salary) FROM emp WHERE dept_id = e.dept_id)` |
| **Nested subquery**       | Subquery **inside another subquery** | `SELECT * FROM ... WHERE id IN (SELECT id FROM (SELECT ...))`            |



# __________________________________________________________________
# 4. Subqueries Can Be Used In...
# __________________________________________________________________




| Clause              | Description                       | Example                                                                 |
| ------------------- | --------------------------------- | ----------------------------------------------------------------------- |
| `SELECT`            | Compute values dynamically        | `SELECT name, (SELECT AVG(salary) FROM emp) AS avg_sal FROM emp`        |
| `FROM`              | Treat subquery as a derived table | `SELECT * FROM (SELECT * FROM emp WHERE salary > 5000) AS temp`         |
| `WHERE` / `HAVING`  | Filter data conditionally         | `WHERE dept_id IN (SELECT id FROM dept WHERE location = 'NY')`          |
| `UPDATE` / `DELETE` | Apply conditions dynamically      | `DELETE FROM emp WHERE dept_id = (SELECT id FROM dept WHERE name='HR')` |



# __________________________________________________________________
# 5. Subquery vs Join – Comparison
# __________________________________________________________________



| Feature     | Subquery                            | JOIN                               |
| ----------- | ----------------------------------- | ---------------------------------- |
| Simplicity  | Easier for single-value comparisons | Better for multi-table combination |
| Performance | Slower for large datasets           | Faster due to optimized joins      |
| Readability | Easier in nested logic              | Easier when combining datasets     |




# __________________________________________________________________
# 6. SYNTAX
# __________________________________________________________________
 

Main Query
   |
   --> Subquery (inner, in WHERE or FROM)

EG:

SELECT name
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);



# __________________________________________________________________
# 7. Practice Queries (With Sales Table or Your Own Schema)
# __________________________________________________________________





# Single-Row Subquery

SELECT * FROM sales
WHERE price > (SELECT AVG(price) FROM sales);


# Multi-Row Subquery with IN

SELECT * FROM sales
WHERE region IN (
  SELECT region FROM sales WHERE quantity > 8
);


# Correlated Subquery


SELECT product, price
FROM sales s1
WHERE price > (
    SELECT AVG(price)
    FROM sales s2
    WHERE s1.category = s2.category
);


 # Subquery in FROM Clause


SELECT category, total_qty
FROM (
  SELECT category, SUM(quantity) AS total_qty
  FROM sales
  GROUP BY category
) AS sub
WHERE total_qty > 15;
