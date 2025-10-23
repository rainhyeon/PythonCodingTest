-- 코드를 입력하세요
-- 주문 정보: FIRST_HALF
    -- 속성: SHIPMENT_ID(출하 번호), FLAVOR(아이스크림 맛), TOTAL_ORDER(상반기 아이스크림 총주문량)
    -- 기본키(외래키): FLAVOR
-- 성분: ICREATM_INFO
    -- 속성: FLAVOR(아이스크림 맛), INGREDITENT_TYPE(아이스크림의 성분 타입)
    -- 기본키(외래키): FLAVOR
    
-- 총주문 > 3000 AND 주 성분 == fruit_based AND 총주문량이 큰 순서대로 
SELECT f.FLAVOR
FROM FIRST_HALF AS f
JOIN ICECREAM_INFO AS i
  ON f.FLAVOR = i.FLAVOR
WHERE f.TOTAL_ORDER > 3000
  AND i.INGREDIENT_TYPE = 'fruit_based'
ORDER BY f.TOTAL_ORDER DESC;

