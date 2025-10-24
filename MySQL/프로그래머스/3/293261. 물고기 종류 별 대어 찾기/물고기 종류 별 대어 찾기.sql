-- 코드를 작성해주세요
-- 물고기 정보: FISH_INFO 
    -- ID, FISH_TYPE, LENGTH, TIME
    -- 물고기의 ID, 물고기의 종류(숫자), 잡은 물고기의 길이(cm), 물고기를 잡은 날짜를
    
-- 물고기 이름: FISH_NAME_INFO 
    -- FISH_TYPE, FISH_NAME
    --  물고기의 종류(숫자), 물고기의 이름(문자)
    
-- 외래키 FISH_TYPE

-- FISH_TYPE 끼리 그룹화해서 가장 긴 길이의 ID, 이름, 길이 출력해라

SELECT fi.ID, fn.FISH_NAME, fi.LENGTH
FROM (SELECT ID,
    FISH_TYPE,
    LENGTH,
    ROW_NUMBER() OVER (PARTITION BY FISH_TYPE ORDER BY LENGTH DESC) AS rn
FROM FISH_INFO
WHERE LENGTH IS NOT NULL) fi
JOIN FISH_NAME_INFO fn
    ON fi.FISH_TYPE = fn.FISH_TYPE
WHERE fi.rn = 1
ORDER BY fi.ID;