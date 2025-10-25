-- 코드를 입력하세요
-- 주문 정보: FIRST_HALF 
    -- SHIPMENT_ID, FLAVOR, TOTAL_ORDER
    -- 출하 번호, 아이스크림 맛, 상반기 아이스크림 총주문량
-- 7월 주문 정보: JULY
    -- SHIPMENT_ID, FLAVOR, TOTAL_ORDER
    --  출하 번호, 아이스크림 맛, 7월 아이스크림 총주문량
    
-- 외래키: FLAVOR

-- 출력: 7월의 총 주문량, 상반기의 총 주문량을 더한 값이 큰 순서대로 상위3개의 맛 조회

SELECT f.FLAVOR
FROM FIRST_HALF f
JOIN JULY j
    ON f.FLAVOR = j.FLAVOR
GROUP BY f.FLAVOR
ORDER BY SUM(f.TOTAL_ORDER + j.TOTAL_ORDER) DESC
LIMIT 3;


