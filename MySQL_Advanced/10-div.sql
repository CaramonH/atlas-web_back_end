-- SQL script that creates function SafeDiv
-- Divides the first by the second number
-- Returns 0 if the second number is equal to 0
DELIMIER //

CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
BEGIN
    IF b = 0 THEN
        RETURN 0;
    END IF;
    RETURN a / b;
END
//

DELIMITER ;