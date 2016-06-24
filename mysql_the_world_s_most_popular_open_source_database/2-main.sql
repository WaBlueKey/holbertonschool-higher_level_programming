\! echo "\nNumber of season by TVShow ordered by name (A-Z)?"
SELECT TVShow.name, COUNT(Season.number) AS 'nb_seasons'
FROM TVShow, Season
WHERE TVShow.id = Season.tvshow_id
GROUP BY name;


\! echo "\nList of Network by TVShow ordered by name (A-Z)?"
SELECT TVShow.name AS 'TVShow name', Network.name AS 'Network name'
FROM TVShow, Network
WHERE TVShow.network_id = Network.id
GROUP BY TVShow.name ASC;

\! echo "\nList of TVShows ordered by name (A-Z) in the Network 'Fox (US)'?"
SELECT TVShow.name FROM TVShow, Network
WHERE TVShow.network_id = Network.id and Network.name LIKE '%Fox%'
GROUP BY TVShow.name ASC;

\! echo "\nNumber of episodes by TVShows ordered by name (A-Z)?"
SELECT TVShow.name, COUNT(Episode.number) AS 'nb_episodes'
FROM TVShow, Season, Episode
WHERE Episode.season_id = Season.id and Season.tvshow_id = TVShow.id
GROUP BY TVShow.name ASC;
