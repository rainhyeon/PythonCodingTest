-- 코드를 입력하세요
-- 고객 정보: MEMBER_PROFILE
    -- MEMBER_ID, MEMBER_NAME, TLNO, GENDER, DATE_OF_BIRTH
    -- 회원 ID, 회원 이름, 회원 연락처, 성별, 생년월일
-- 리뷰 정보: REST_REVIEW 
    -- REVIEW_ID, REST_ID, MEMBER_ID, REVIEW_SCORE, REVIEW_TEXT,REVIEW_DATE
    -- 리뷰 ID, 식당 ID, 회원 ID, 점수, 리뷰 텍스트, 리뷰 작성일
    
-- 출력: 리뷰를 가장 많이 작성한 회원

SELECT m.MEMBER_NAME, r.REVIEW_TEXT, DATE_FORMAT(r.REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE
FROM MEMBER_PROFILE m
JOIN REST_REVIEW r
    ON m.MEMBER_ID = r.MEMBER_ID
WHERE m.MEMBER_ID = (SELECT MEMBER_ID
                    FROM REST_REVIEW
                    GROUP BY MEMBER_ID
                    ORDER BY COUNT(MEMBER_ID) DESC
                    LIMIT 1)
ORDER BY r.REVIEW_DATE, r.REVIEW_TEXT