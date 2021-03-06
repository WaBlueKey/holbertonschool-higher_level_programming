\! echo "\nNumber of seasons by tvshow_id?"
SELECT tvshow_id, COUNT(id) FROM Season
GROUP BY tvshow_id;

\! echo "\nNumber of occurrences of the same episode number ordered by episode number?"
SELECT number, COUNT(id) FROM Episode
GROUP BY number;

\! echo "\nTop 3 of the Genre's occurrences in all TVShows ordered by this number?"
SELECT genre_id, COUNT(tvshow_id) AS 'occurrences_genre'
FROM TVShowGenre
GROUP BY genre_id
ORDER BY occurrences_genre DESC
LIMIT 3;

\! echo "\nSearch all TVShow with this letter sequence 'th' case insensitive and display with the name in lowercase?"
SELECT LCASE(name) FROM TVShow
WHERE name LIKE '%th%';
