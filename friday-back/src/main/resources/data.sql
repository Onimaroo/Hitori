
INSERT INTO day(day_name, holiday_check, number_of_events)  SELECT 'Monday', true, 0 WHERE NOT EXISTS(SELECT * FROM day WHERE day_name LIKE 'Monday') ;
INSERT INTO day(day_name, holiday_check, number_of_events) SELECT 'Tuesday', true, 0 WHERE NOT EXISTS(SELECT * FROM day WHERE day_name LIKE 'Tuesday') ;
INSERT INTO day(day_name, holiday_check, number_of_events) SELECT 'Wednesday', true, 0 WHERE NOT EXISTS(SELECT * FROM day WHERE day_name LIKE 'Wednesday') ;
INSERT INTO day(day_name, holiday_check, number_of_events) SELECT 'Thursday', true, 0 WHERE NOT EXISTS(SELECT * FROM day WHERE day_name LIKE 'Thursday') ;
INSERT INTO day(day_name, holiday_check, number_of_events) SELECT 'Friday', true, 0 WHERE NOT EXISTS(SELECT * FROM day WHERE day_name LIKE 'Friday') ;
INSERT INTO day(day_name, holiday_check, number_of_events) SELECT 'Satursday', true, 0 WHERE NOT EXISTS(SELECT * FROM day WHERE day_name LIKE 'Satursday') ;
INSERT INTO day(day_name, holiday_check, number_of_events) SELECT 'Sunday', true, 0 WHERE NOT EXISTS(SELECT * FROM day WHERE day_name LIKE 'Sunday') ;
INSERT INTO event(id_event, description, location, start_date, end_date)  SELECT 1, 'Faire du vélo', 'Lognes', '28-04-2021', '29-04-2021' WHERE NOT EXISTS(SELECT * FROM event WHERE id_event = 1);
INSERT INTO event(id_event, description, location, start_date, end_date)  SELECT 2, 'Travailler sur la pièce de théatre', 'Neuilly-Plaisance', '31-03-2021', '12-05-2021' WHERE NOT EXISTS(SELECT * FROM event WHERE id_event = 2);