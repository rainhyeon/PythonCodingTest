-- 코드를 입력하세요

-- 상반기 주문 정보: FIRST_HALF
    -- SHIPMENT_ID, FLAVOR, TOTAL_ORDER
    -- 출하 번호, 아이스크림 맛, 상반기 아이스크림 총주문량
-- 성분 정보: ICECREAM_INFO
    -- FLAVOR, INGREDITENT_TYPE
    -- 스크림 맛, 아이스크림의 성분 타입
    
-- 출력: 성분 타입별 총 주문량
-- 순서: 총 주문량

SELECT i.INGREDIENT_TYPE, SUM(h.TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF h
JOIN ICECREAM_INFO i
    ON h.FLAVOR = i.FLAVOR
GROUP BY i.INGREDIENT_TYPE
ORDER BY TOTAL_ORDER