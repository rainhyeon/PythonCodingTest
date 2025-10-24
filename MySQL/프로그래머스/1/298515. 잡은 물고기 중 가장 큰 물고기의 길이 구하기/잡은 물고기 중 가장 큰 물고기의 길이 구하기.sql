-- 코드를 작성해주세요
-- FISH_INFO
--  ID, FISH_TYPE, LENGTH, TIME
-- 물고기의 ID, 물고기의 종류(숫자), 잡은 물고기의 길이(cm), 물고기를 잡은 날짜
-- (10CM 이하이면 LENGTH가 NULL이다)

-- 출력: 잡은 물고기중 가장 큰 물고기의길이를  'cm'를 붙여 출력하라

SELECT CONCAT(MAX(LENGTH), 'cm') AS MAX_LENGTH
FROM FISH_INFO
WHERE LENGTH IS NOT NULL;
