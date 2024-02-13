-- SQL script that creates an index idx_name_first_score on the table 'names'
-- and the first letter of 'name' and 'score'
CREATE INDEX idx_name_first_scorem ON names (name(1), score);