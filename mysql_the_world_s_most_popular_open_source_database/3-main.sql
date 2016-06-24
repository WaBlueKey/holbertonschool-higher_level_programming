\! echo "\nList of TVShows ordered by name (A-Z) with more than or equal 4 seasons?"
SELECT TVShow.name FROM TVShow, Season
WHERE TVShow.id = Season.tvshow_id and Season.number >= 4
GROUP BY TVShow.name ASC;

\! echo "\nList of TVShows ordered by name (A-Z) with the Genre 'Comedy'?"
SELECT TVShow.name FROM TVShow, TVShowGenre, Genre
WHERE TVShow.id = TVShowGenre.tvshow_id and TVShowGenre.genre_id = Genre.id and Genre.name = 'Comedy'
GROUP BY TVShow.name ASC;

\! echo "\nList of Actors ordered by name (A-Z) for the TVShow 'The Big Bang Theory'?"
SELECT Actor.name FROM Actor, TVShowActor, TVShow
WHERE TVShow.id = TVShowActor.tvshow_id and TVShowActor.actor_id = Actor.id and TVShow.name = 'The Big Bang Theory'
GROUP BY Actor.name ASC;

\! echo "\nTop 10 of actors by number of TVShows where they are? (without Actor name order => can be random)"
SELECT Actor.name, COUNT(tvshow_id) AS 'nb_tvshows'
FROM Actor, TVShowActor, TVShow
WHERE TVShow.id = TVShowActor.tvshow_id and TVShowActor.actor_id = Actor.id
GROUP BY Actor.name
ORDER BY nb_tvshows DESC
LIMIT 10;
