-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT * FROM crime_scene_reports WHERE month = 7 AND day = 28;
SELECT * FROM interviews WHERE month = 7 AND day = 28;
SELECT * FROM atm_transactions WHERE month = 7 AND day = 28 AND atm_location = "Leggett Street";

SELECT name
FROM people
WHERE id
IN(SELECT person_id
FROM bank_accounts
WHERE account_number
IN(SELECT account_number
FROM atm_transactions
WHERE month = 7 AND day = 28 AND transaction_type = "withdraw" AND atm_location = "Leggett Street"));

SELECT name FROM people WHERE license_plate IN(SELECT license_plate FROM bakery_security_logs WHERE month = 7 AND activity ="exit" AND day = 28 AND hour >= 10 AND hour < 11);

SELECT name
FROM people
WHERE phone_number
IN(SELECT caller
FROM phone_calls
WHERE (month = 7 AND DAY = 28 AND duration < 60)
AND caller IN(SELECT phone_number FROM people WHERE name = "Bruce" OR name = "Diana" OR name = "Iman" OR name = "Luca" OR name = "Taylor"));

SELECT * FROM flights WHERE month = 7 AND day = 28  AND origin_airport_id = 8;

SELECT name
FROM people
WHERE passport_number
IN
(SELECT passport_number
FROM passengers
WHERE flight_id IN
(SELECT id FROM flights WHERE month = 7 AND day = 29 AND origin_airport_id = 8)
 AND passport_number IN (SELECT passport_number FROM people WHERE name = "Taylor" OR name = "Diana" OR name = "Bruce"));

SELECT city,id FROM airports;

SELECT * FROM flights WHERE month = 7 AND day = 28 AND origin_airport_id = 8 ORDER BY hour ASC;

SELECT name
FROM people
WHERE passport_number
IN
(SELECT passport_number
FROM passengers
WHERE flight_id = 6
 AND passport_number IN (SELECT passport_number FROM people WHERE name = "Taylor" OR name = "Diana" OR name = "Bruce"));

 SELECT name,
FROM people
WHERE passport_number
IN
(SELECT passport_number
FROM passengers
WHERE flight_id IN
(SELECT id FROM flights WHERE month = 7 AND day = 29 AND origin_airport_id = 8 )
 AND passport_number IN (SELECT passport_number FROM people WHERE name = "Taylor" OR name = "Diana" OR name = "Bruce"));


SELECT name FROM people WHERE phone_number =(SELECT receiver FROM phone_calls WHERE caller = (SELECT phone_number FROM people WHERE name = "Diana") AND month = 7 AND day = 28);

SELECT name FROM people WHERE phone_number =(SELECT receiver FROM phone_calls WHERE caller = (SELECT phone_number FROM people WHERE name = "Bruce") AND month = 7 AND day = 28);

SELECT name FROM people WHERE phone_number =(SELECT receiver FROM phone_calls WHERE caller = (SELECT phone_number FROM people WHERE name = "Taylor") AND month = 7 AND day = 28);

SELECT * FROM flights WHERE id IN (SELECT flight_id FROM passengers WHERE passport_number =(SELECT passport_number FROM people WHERE name = "Bruce"))

SELECT * FROM flights WHERE month = 7 AND day = 29 AND origin_airport_id = 8;

SELECT * FROM airports;

SELECT name
FROM people
WHERE passport_number
IN
(SELECT passport_number
FROM passengers
WHERE flight_id IN
(SELECT id FROM flights WHERE month = 7 AND day = 29 AND origin_airport_id = 8 AND hour = 8 )
 AND passport_number IN (SELECT passport_number FROM people WHERE name = "Taylor" OR name = "Diana" OR name = "Bruce"));

 SELECT seat FROM passengers WHERE flight_id = 36 AND passport_number
 IN(SELECT passport_number FROM people WHERE phone_number =(SELECT receiver
 FROM phone_calls WHERE caller = (SELECT phone_number FROM people WHERE name = "Taylor") AND month = 7 AND day = 29));

 SELECT seat FROM passengers WHERE flight_id = 36 AND passport_number
 IN(SELECT passport_number FROM people WHERE phone_number =(SELECT receiver
 FROM phone_calls WHERE caller = (SELECT phone_number FROM people WHERE name = "Bruce") AND month = 7 AND day = 29));

 SELECT name FROM people WHERE  passport_number IN(SELECT passport_number FROM passengers WHERE seat IN(SELECT seat FROM passengers WHERE flight_id = 36 )) ORDER BY name;

