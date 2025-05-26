-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, 
CASE 
WHEN SEX_UPON_INTAKE IN ('Neutered Male', 'Spayed Female') THEN 'O'
WHEN SEX_UPON_INTAKE IN ('Intact Male', 'Intact Female') THEN 'X'
END AS '중성화'
FROM ANIMAL_INS
