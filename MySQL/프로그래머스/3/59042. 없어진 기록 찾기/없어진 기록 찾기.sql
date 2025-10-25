-- 코드를 입력하세요
-- 동물 정보: ANIMAL_INS
    --  ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE
    -- 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부

-- 입양 보낸: ANIMAL_OUTS 
    -- ANIMAL_ID, ANIMAL_TYPE, DATETIME, NAME, SEX_UPON_OUTCOME
    -- 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부
-- 외래키: ANIMAL_ID

-- 출력: 입양 기록은 있지만, 보호소에 들어온 기록이 없는 동물ID, 이름
-- 순서: ID

SELECT ANIMAL_ID, NAME
FROM ANIMAL_OUTS
WHERE ANIMAL_ID NOT IN (SELECT ANIMAL_ID
                        FROM ANIMAL_INS)
ORDER BY ANIMAL_ID
