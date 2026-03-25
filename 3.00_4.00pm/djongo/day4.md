
# Topic: ORM -OPERATIONS IN DJANGO




| Operation         | Method                                   | Definition                                                                |
| ----------------- | ---------------------------------------- | ------------------------------------------------------------------------- |
| Create            | `create()`, `save()`                     | Inserts new records into the database table.                              |

| Read              | `all()`, `get()`, `filter()`             | Retrieves data from the database based on given conditions.               |

| Update            | `save()`, `update()`                     | Modifies existing records in the database.                                |

| Delete            | `delete()`                               | Removes records from the database permanently.                            |

| Count             | `count()`                                | Returns the total number of records in a QuerySet.                        |

| Check Exists      | `exists()`                               | Returns True if at least one record matches the condition.                |

| Aggregate         | `aggregate()`                            | Performs calculations like Sum, Avg, Max, Min on fields.                  |

| Complex Query     | `Q`                                      | Allows combining multiple conditions using AND / OR logic.                |

| Field Calculation | `F`                                      | Performs database-level field operations without fetching data to Python. |

| Optimization      | `select_related()`, `prefetch_related()` | Reduces number of database queries for related objects.                   |




