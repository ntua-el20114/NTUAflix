GRANT FILE ON *.* TO 'root'@'localhost';
SET NAMES utf8mb4;

source ./ntuaflix.sql;
source ./population/done/app_user_insertions.sql;
source ./population/done/title_insertions.sql;
source ./population/done/name_insertions/name_insertions_1.sql;
-- source ./population/done/name_insertions/name_insertions_2.sql;
-- source ./population/done/name_insertions/name_insertions_3.sql;
-- source ./population/done/name_insertions/name_insertions_4.sql;
-- source ./population/done/name_insertions/name_insertions_5.sql;
-- source ./population/done/name_insertions/name_insertions_6.sql;
source ./population/done/aka_insertions.sql;
source ./population/done/episode_insertions.sql;
source ./population/done/imdb_ratings_insertions.sql;
source ./population/done/name_titles_insertions.sql;
source ./population/done/crew_insertions.sql;
source ./population/done/user_preferences_insertions.sql;
