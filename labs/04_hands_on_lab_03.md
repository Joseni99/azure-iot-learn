# Hands-on LAB: Azure SQL Database

## Study Case

In this exercise, you will create an Azure SQL database instance on the Azure cloud platform, configure it for optimal performance and security, and then utilize Azure Data Studio to connect to the database, execute SQL queries, and manage database objects such as tables, views, and stored procedures. Through this hands-on experience, you will gain proficiency in deploying cloud-based databases and leveraging modern tools for database administration and development.

**PART 1:**

Creation of a SQL database on Azure SQL and make a simple query.

**PART 2:**

Try Azure Data Studio and play with the database.

## Part 1: Creation of a SQL database

1. First of all let's create our first SQL data base, click Create SQL database 
   
   <p align="center">
   <img title="" src="../img/12%20(2).png" alt="12 (2).png" width="655">
   </p>

2. In the server part click on "Create new"
   
   <p align="center">
   <img title="" src="../img/12%20(4).png" alt="12 (4).png" width="506">
   </p>

3. Give a unique server name and **write it down**, select the region in Europe Germany Central and use SQL Authentification, set a user and a password and **remember** it.
   
   <p align="center">
   <img title="" src="../img/12%20(5).png" alt="12 (5).png" width="512">
   </p>

4. Click on "Apply offer" for a Free Database for a lifetime of the subscription, select the database server we created and as always select the correspondant resource group.
   
   <p align="center">
   <img title="" src="../img/12%20(6).png" alt="12 (6).png" width="584">
   </p>

5. In the networking tab make the endpoint public and set both firewall rules to YES.
   
   <p align="center">
   <img src="../img/12%20(7).png" title="" alt="12 (7).png" width="584">
   </p>

6. Click o Review + Create.
   
   <p align="center">
   <img src="../img/12%20(8).png" title="" alt="12 (8).png" width="585">
   </p>

7. Wait for the deployment and go to the resource.
   
   <p align="center">
   <img title="" src="../img/12%20(9).png" alt="12 (9).png" width="656">
   </p>

8. Click on the Query editor and log-in with the previouss credentials.
   
   <p align="center">
   <img src="../img/12%20(10).png" title="" alt="12 (10).png" width="656">
   </p>

9. Let's try execute a query to create a table with different columns:

```
CREATE TABLE testtable (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);
```

Paste the content and click on RUN. 

<p align="center">
<img src="../img/12%20(11).png" title="" alt="12 (11).png" width="645">
</p>

## Part 2: Azure Data Studio

Congratulations, you have deployed your first SQL database in Azure and created a table with a primary key and different columns. Let's use the Azure Data Studio to explore the database outside Azure webpage.

```
https://learn.microsoft.com/en-us/azure-data-studio/download-azure-data-studio?tabs=win-install%2Cwin-user-install%2Credhat-install%2Cwindows-uninstall%2Credhat-uninstall
```

You can download the portable .zip if you dont want to install it.

1. Use the connection string you will find just below the Query Editor, should be something like this:
   
   ```
   Server=tcp:labtest2024.database.windows.net,1433;Initial Catalog=eu-sql;Persist Security Info=False;User ID=labtest2024;Password={your_password};MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;
   ```

        Remember to use your own password.

<p align="center">
<img src="../img/12%20(13).png" title="" alt="12 (13).png" width="656">
</p>
2. Once you are logged in, you will see the test table we created.
<p align="center">
<img src="../img/12%20(14).png" title="" alt="12 (14).png" width="659">
</p>
3. Also if we click in the table we will see the different columns.
<p align="center">
<img src="../img/12%20(15).png" title="" alt="12 (15).png" width="705">
</p>
4. And also we can find the different options that Azure Data Studio allow us to do with the Azure SQL database do. We can create tables, primary keys, make querys, explore data, edit table properties and so on.

![12 (1).png](../img/12%20(1).png)

5. Please do not delete this database because we are going to need it for the following practices, and it is totally free of charge.
