-- 코드를 작성해주세요
-- 대장균 정보: ECOLI_DATA
    -- ID, PARENT_ID, SIZE_OF_COLONY, DIFFERENTIATION_DATE, GENOTYPE
    -- 대장균 개체의 ID, 부모 개체의 ID, 개체의 크기, 분화되어 나온 날짜, 개체의 형질
    -- (최초의 개체는 PARENT_ID가 NULL이다)
    
-- 출력: 분화된 년도, 편차(연도별 가장큰 대장균 크기 - 각 대장균 크기), 연도의 오름차순

-- 연도별 가장 큰 대장균 크기

WITH max_by_year AS (
    SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, MAX(SIZE_OF_COLONY) AS MAX_SIZE
    FROM ECOLI_DATA
    GROUP BY YEAR
)
SELECT m.YEAR,
    (m.MAX_SIZE - e.SIZE_OF_COLONY) AS YEAR_DEV,
    e.ID
FROM ECOLI_DATA e
JOIN max_by_year m
    ON m.YEAR = YEAR(e.DIFFERENTIATION_DATE)
ORDER BY m.YEAR, YEAR_DEV;