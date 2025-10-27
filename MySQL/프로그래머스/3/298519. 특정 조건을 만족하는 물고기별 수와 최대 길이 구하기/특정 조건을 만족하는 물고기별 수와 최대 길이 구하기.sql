-- 코드를 작성해주세요

-- 평균의 길이 >= 33

WITH sample AS (SELECT
                    ID,
                    FISH_TYPE,
                    IFNULL(LENGTH, 10) AS LENGTH,
                    TIME
                FROM FISH_INFO
)

SELECT COUNT(ID) AS FISH_COUNT, MAX(LENGTH) AS MAX_LENGTH, FISH_TYPE
FROM sample
GROUP BY FISH_TYPE
HAVING AVG(LENGTH) >= 33
ORDER BY FISH_TYPE
