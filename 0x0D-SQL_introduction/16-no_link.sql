-- DO all that
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ' '
ORDER BY score DESC, name DESC;
