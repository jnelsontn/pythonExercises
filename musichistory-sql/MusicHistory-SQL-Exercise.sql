Select * from Genre;
Insert into Artist values (null, 'Smashing Pumpkins', 1985);
insert into Album values (null, 'Zeitgeist', 2007, 90, 'Something', 28, 2);

insert into Song values (null, "Come On Lets Go", 5, 2007, 3, 28, 23);
insert into Song values (null, "Song 2", 5, 2007, 3, 28, 23);
insert into Song values (null, "Song 3", 5, 2007, 3, 28, 23);
insert into Song values (null, "Song 4", 5, 2007, 3, 28, 23);
insert into Song values (null, "Song 5", 5, 2007, 3, 28, 23);

SELECT Song.Title, Artist.ArtistName
FROM Song
LEFT JOIN Artist
WHERE Song.ArtistId = Artist.ArtistId
AND Artist.ArtistName = 'Smashing Pumpkins';

SELECT Song.Title, Album.Title
FROM Song
LEFT JOIN Album
WHERE Song.ArtistId = Album.ArtistId
AND Song.ArtistId = 28;
 
/* Songs for Each Album */
SELECT Count(Song.AlbumId) '# Songs', Album.Title 'Album Title', Artist.ArtistName
FROM Song, Album, Artist
WHERE Song.AlbumId = Album.AlbumId
AND Song.ArtistId = Artist.ArtistId
GROUP BY Album.Title;

/* Songs for Each Artist */
SELECT Count(Song.ArtistId) '# Songs', Artist.ArtistName 'Artist Name'
FROM Song, Artist
WHERE Song.ArtistId = Artist.ArtistId
GROUP BY Artist.ArtistName;
 
/* Songs for Each Genre */
SELECT Count(Song.GenreId) '# Songs', Genre.Label 'Genre', Genre.GenreId 'GenreId'
FROM Song, Genre
WHERE Song.GenreId = Genre.GenreId
GROUP BY Genre.GenreId;
 
 /* Album with longest duration */
SELECT Album.Title, MAX(Album.AlbumLength) 'Album Length'
FROM Album

 /* Song with Longest Duration */
SELECT MAX(Song.SongLength) 'Song Length', Song.Title 'Song Title', Artist.ArtistName 'Artist', Album.Title 'Album'
FROM Album, Song, Artist
WHERE Song.ArtistId = Artist.ArtistId
AND Song.ArtistId = Album.ArtistId

