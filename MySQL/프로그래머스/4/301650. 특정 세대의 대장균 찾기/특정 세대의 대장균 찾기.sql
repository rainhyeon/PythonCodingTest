-- 코드를 작성해주세요
WITH RECURSIVE gen AS (SELECT ID, PARENT_ID, 1 AS GEN_COUNT
                      FROM ECOLI_DATA
                      WHERE PARENT_ID IS NULL
                      UNION ALL
                      SELECT e.ID, e.PARENT_ID, g.GEN_COUNT+1
                      FROM gen g
                      JOIN ECOLI_DATA e
                        ON g.ID = e.PARENT_ID)

SELECT ID
FROM gen
WHERE GEN_COUNT = 3
ORDER BY ID