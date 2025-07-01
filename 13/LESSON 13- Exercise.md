## LESSON 13: Exercise

##  Dataset: `sales_data.csv`

| OrderID | Customer | Region | Product  | Quantity | UnitPrice | OrderDate  | SalesRep   |
| ------- | -------- | ------ | -------- | -------- | --------- | ---------- | ---------- |
| 1001    | Alice    | East   | Laptop   | 2        | 900       | 2023-01-15 | John Doe   |
| 1002    | Bob      | West   | Monitor  | 5        | 200       | 2023-01-18 | Jane Smith |
| 1003    | Charlie  | East   | Keyboard | 3        | 50        | 2023-02-05 | John Doe   |
| 1004    | Alice    | North  | Laptop   | 1        | 950       | 2023-03-01 | Amy Adams  |
| 1005    | David    | South  | Mouse    | 10       | 25        | 2023-03-10 | Jane Smith |
| 1006    | Eve      | West   | Monitor  | 2        | 210       | 2023-04-02 | John Doe   |
| 1007    | Frank    | East   | Laptop   | 1        | 1000      | 2023-04-10 | Amy Adams  |
| 1008    | Grace    | North  | Mouse    | 6        | 30        | 2023-04-22 | Jane Smith |
| 1009    | Heidi    | South  | Keyboard | 4        | 60        | 2023-05-03 | John Doe   |
| 1010    | Ivan     | West   | Monitor  | 3        | 205       | 2023-05-15 | Amy Adams  |

---

##  Assignments

1. **Load the dataset into a pandas DataFrame.**
2. **Display the first 5 rows and data types of all columns.**
3. **Create a new column `TotalPrice` as Quantity × UnitPrice.**
4. **Filter rows where the Region is 'East' and display them.**
5. **Filter rows where Quantity is more than 3 and UnitPrice is less than 100.**
6. **Sort the dataset by `TotalPrice` in descending order.**
7. **Group data by Region and calculate total Quantity per Region.**
8. **Group data by SalesRep and calculate average UnitPrice.**
9. **Find the top 3 most sold Products (by Quantity).**
10. **Calculate total revenue (sum of TotalPrice) by SalesRep.**
11. **Add a column `OrderMonth` extracted from OrderDate.**
12. **Group data by `OrderMonth` and calculate the monthly total sales.**
13. **Find the Product with the highest UnitPrice.**
14. **Using a lambda function, create a new column `HighValue` (True if TotalPrice > 500).**
15. **Count how many orders were HighValue.**
16. **Display unique values in Region and Product columns.**
17. **Find customers who ordered more than once.**
18. **Replace 'Monitor' with 'LCD Monitor' in the Product column.**
19. **Drop the column `OrderID`.**
20. **Export the final DataFrame to a new CSV file.**
