<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" width="80"/>
  <h1>SQL</h1>

![Purpose](https://img.shields.io/badge/purpose-databases%20%26%20data-4479A1)
![Difficulty](https://img.shields.io/badge/difficulty-intermediate-FF9800)
![Typing](https://img.shields.io/badge/typing-declarative-9C27B0)
![Execution](https://img.shields.io/badge/execution-database%20engine-795548)
![Paradigm](https://img.shields.io/badge/paradigm-declarative-607D8B)

</div>

---

## What is SQL

SQL (Structured Query Language) is a declarative language for interacting
with relational databases. Instead of writing step-by-step instructions you
describe what data you want and the database engine works out how to get it.
Developed in the 1970s at IBM, SQL has been the standard for relational
databases for over 50 years. The core concepts apply across every major
database system — PostgreSQL, MySQL, SQLite, Microsoft SQL Server, and
Oracle all use SQL with minor dialect differences.

---

## Difficulty

**Intermediate.** SQL requires a different way of thinking — declarative
rather than procedural. The basics (SELECT, INSERT, UPDATE, DELETE) are
straightforward. Joins, subqueries, window functions, and query optimisation
take more time to master. Understanding indexes and how the query planner
works is important for production use.

---

## What SQL is used for

| Field                       | Details                                                                                                     |
| --------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Backend development**     | Almost every web application stores data in a relational database. SQL is how you read and write that data. |
| **Data analysis**           | Analysts use SQL to query large datasets, aggregate results, and generate reports.                          |
| **Data engineering**        | ETL pipelines, data warehouses (Snowflake, BigQuery, Redshift) all use SQL heavily.                         |
| **Business intelligence**   | BI tools like Tableau, Looker, and Metabase all run SQL queries under the hood.                             |
| **Database administration** | Managing tables, indexes, users, and performance.                                                           |

---

## Key concepts

- **SELECT** — retrieve data from one or more tables
- **JOIN** — combine rows from multiple tables based on a related column
- **WHERE** — filter rows based on conditions
- **GROUP BY** — aggregate data into groups (counts, sums, averages)
- **Indexes** — structures that make queries faster by avoiding full table scans
- **Transactions** — group multiple operations so they either all succeed or all fail (ACID)
- **Constraints** — rules on columns (NOT NULL, UNIQUE, FOREIGN KEY) that enforce data integrity

---

## Limitations

- **Not a programming language** — SQL alone cannot build an application; it works alongside a programming language
- **Dialect differences** — PostgreSQL, MySQL, and SQLite have syntax differences that can cause confusion
- **Scaling challenges** — traditional relational databases have limits for extremely large or high-traffic datasets (though modern solutions address this)
- **Schema changes** — altering table structures in production requires careful migration planning

---

## What knowing SQL gets you

- Required for almost every backend developer, data analyst, and data engineer role
- The ability to query and understand any relational database
- Strong data literacy that makes you more effective in almost any technical role

---

## Common databases

| Database               | What it is                                                                                |
| ---------------------- | ----------------------------------------------------------------------------------------- |
| `PostgreSQL`           | The most powerful open-source relational database. Preferred for production applications. |
| `MySQL`                | Widely used, especially in older web applications and WordPress.                          |
| `SQLite`               | Serverless, file-based database. Great for local development and small applications.      |
| `Microsoft SQL Server` | Common in enterprise and Microsoft environments.                                          |

---

## How to run SQL

**Terminal (SQLite):**

```bash
sqlite3 database.db
sqlite3 database.db < filename.sql
```

**GUI (DB Browser for SQLite):**
Open a database file, write SQL in the Execute SQL tab, press play.

**GUI (DBeaver):**
Works with every major database. Write queries and press `Ctrl+Enter`.

---

## File naming for this folder

```
1.select.sql
2.filtering.sql
3.sorting.sql
4.joins.sql
5.aggregation.sql
6.insert-update-delete.sql
7.create-tables.sql
8.constraints.sql
9.indexes.sql
10.subqueries.sql
11.transactions.sql
12.window-functions.sql
```
