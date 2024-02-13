-- Script that creates a stored procedure ComputeAverageScoreForUser
-- Computes and stores the average score for a student
-- Average score cannot be a decimal
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE average_score FLOAT;
    SELECT AVG(score) INTO average_score FROM corrections WHERE corrections.user_id = user_id;
    UPDATE users SET average_score = average_score WHERE id = user_id;
END;
//
DELIMITER ;