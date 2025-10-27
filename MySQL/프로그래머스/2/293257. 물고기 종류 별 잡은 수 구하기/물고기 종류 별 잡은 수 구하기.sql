-- 코드를 작성해주세요
-- 물고기 정보: FISH_INFO
    -- ID, FISH_TYPE, LENGTH, TIME
    --  물고기의 ID, 물고기의 종류(숫자), 잡은 물고기의 길이(cm), 물고기를 잡은 날짜
-- 이름 정보: FISH_NAME_INFO
    -- FISH_TYPE, FISH_NAME
    -- 종류(숫자), 물고기의 이름
-- 외래키: FISH_TYPE

-- 출력: 물고기 이름별 잡은 수

SELECT COUNT(*) AS FISH_COUNT, fi.FISH_NAME
FROM FISH_INFO f
JOIN FISH_NAME_INFO fi
    ON f.FISH_TYPE = fi.FISH_TYPE
GROUP BY fi.FISH_NAME
ORDER BY FISH_COUNT DESC