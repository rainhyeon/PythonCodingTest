-- 코드를 입력하세요
-- 식당 정보: REST_INFO
    -- REST_ID, REST_NAME, FOOD_TYPE, VIEWS, FAVORITES, PARKING_LOT, ADDRESS, TEL
    -- 식당 ID, 식당 이름, 음식 종류, 조회수, 즐겨찾기수, 주차장 유무, 주소, 전화번호를
    
-- 출력: 음식 종류별, 즐겨찾기 수가 가장 많은 것
-- 정렬: 음식 종류


SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE (FOOD_TYPE, FAVORITES) IN (SELECT FOOD_TYPE, MAX(FAVORITES) AS FAVORITES
                    FROM REST_INFO
                    GROUP BY FOOD_TYPE)
ORDER BY FOOD_TYPE DESC
                    
