# Write your MySQL query statement below
SELECT 
    S.id,
    S.name
FROM Students S
LEFT JOIN Departments D
ON S.department_id = D.id
WHERE D.id is null