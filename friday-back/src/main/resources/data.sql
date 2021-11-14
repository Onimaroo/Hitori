/*
INSERT INTO day SELECT 'Monday', 0, true WHERE NOT EXISTS(SELECT * FROM day WHERE day_name LIKE 'Monday') ;
INSERT INTO day SELECT 'Tuesday', 0, true WHERE NOT EXISTS(SELECT * FROM day WHERE day_name LIKE 'Tuesday') ;
INSERT INTO day SELECT 'Wednesday', 0, true WHERE NOT EXISTS(SELECT * FROM day WHERE day_name LIKE 'Wednesday') ;
INSERT INTO day SELECT 'Thursday', 0, true WHERE NOT EXISTS(SELECT * FROM day WHERE day_name LIKE 'Thursday') ;
INSERT INTO day SELECT 'Friday', 0, true WHERE NOT EXISTS(SELECT * FROM day WHERE day_name LIKE 'Friday') ;
INSERT INTO day SELECT 'Satursday', 0, true WHERE NOT EXISTS(SELECT * FROM day WHERE day_name LIKE 'Satursday') ;
INSERT INTO day SELECT 'Sunday', 0, true WHERE NOT EXISTS(SELECT * FROM day WHERE day_name LIKE 'Sunday') ;
*/
