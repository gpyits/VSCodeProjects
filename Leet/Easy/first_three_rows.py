# DataFrame: employees
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | employee_id | int    |
# | name        | object |
# | department  | object |
# | salary      | int    |
# +-------------+--------+
# Write a solution to display the first 3 rows of this DataFrame.

def print_data_frame(data_frame: str) -> None:
    data_frame=data_frame.split('\n')[:7]+[data_frame.split('\n')[-1]]
    for row in data_frame:
        print(row)

data_frame='DataFrame employees\n+-------------+-----------+-----------------------+--------+\n| employee_id | name      | department            | salary |\n-------------+-----------+-----------------------+--------+\n| 3           | Bob       | Operations            | 48675  |\n| 90          | Alice     | Sales                 | 11096  |\n| 9           | Tatiana   | Engineering           | 33805  |\n| 60          | Annabelle | InformationTechnology | 37678  |\n| 49          | Jonathan  | HumanResources        | 23793  |\n| 43          | Khaled    | Administration        | 40454  |\n+-------------+-----------+-----------------------+--------+'
print_data_frame(data_frame)