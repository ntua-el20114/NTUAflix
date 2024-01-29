CREATE DATABASE ntuaflix;
USE ntuaflix;

CREATE TABLE name ( 
    name_id varchar(100) PRIMARY KEY,
    primaryName varchar(255),
    birthYear int,
    deathYear int,
    primaryProfession SET('actor','actress','animation_department','art_department','art_director',
                        'assistant','assistant_director','camera_department','casting_department',
                        'casting_director','cinematographer','composer','costume_department',
                        'costume_designer','director','editor','editorial_department','electrical_department',
                        'executive','legal','location_management','make_up_department','manager',
                        'miscellaneous','music_artist','music_department','podcaster','producer',
                        'production_department','production_designer','production_manager',
                        'publicist','script_department','nan','set_decorator','sound_department',
                        'soundtrack','special_effects','stunts','talent_agent','transportation_department',
                        'visual_effects','writer'),
    url varchar(255));

CREATE TABLE title ( 
    title_id varchar(100) PRIMARY KEY,
    titleType varchar(100),
    originalTitle varchar(100),
    isAdult ENUM('0','1'),
    startYear int,
    runtimeMinutes int,
    genres SET('Action','Adult','Adventure','Animation','Biography','Comedy','Crime','Documentary',
                 'Drama','Family','Fantasy','History','Horror','Music','Musical','Mystery','News',
                 'Romance','Sci-Fi','Short','Sport','Thriller','War','Western'),
    url varchar(255)); 

CREATE TABLE app_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_role ENUM('administrator', 'standard_user', 'developer') NOT NULL,
    token varchar(255) UNIQUE,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    birthdate date,
    email varchar(255) UNIQUE,
    username varchar(255) UNIQUE,
    password varchar(255));

CREATE TABLE aka ( 
    id INT AUTO_INCREMENT PRIMARY KEY,
    title_id varchar(100),
    ordering int,
    title varchar(255),
    region varchar(100),
    language varchar(255),
    types varchar(255),
    isOriginalTitle ENUM('0','1'),
    attributes varchar(255),
    FOREIGN KEY (title_id) REFERENCES title(title_id) ON DELETE CASCADE);

CREATE TABLE imdb_rating ( 
    id INT AUTO_INCREMENT PRIMARY KEY,
    title_id varchar(100) UNIQUE,
    averageRating float,
    numVotes int,
    FOREIGN KEY (title_id) REFERENCES title(title_id) ON DELETE CASCADE);

CREATE TABLE episodes ( 
    id varchar(100) PRIMARY KEY,
    parent_id varchar(100),
    seasonNumber INT,
    episodeNumber INT,
    FOREIGN KEY (parent_id) REFERENCES title(title_id) ON DELETE CASCADE);

CREATE TABLE principals (  
    id INT AUTO_INCREMENT PRIMARY KEY,
    title_id varchar(100),
    name_id varchar(100),
    ordering INT,
    category varchar(50),
    characters varchar(50),
    FOREIGN KEY (title_id) REFERENCES title(title_id) ON DELETE CASCADE,
    FOREIGN KEY (name_id) REFERENCES name(name_id) ON DELETE CASCADE);

CREATE TABLE crew (  
    id INT AUTO_INCREMENT PRIMARY KEY,
    title_id varchar(100),
    director_id varchar(100),
    writer_id varchar(100),
    FOREIGN KEY (director_id) REFERENCES name(name_id) ON DELETE CASCADE,
    FOREIGN KEY (writer_id) REFERENCES name(name_id) ON DELETE CASCADE);

CREATE TABLE user_preferences (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id int,
    title_id varchar(100),
    FOREIGN KEY (title_id) REFERENCES title(title_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES app_user(id) ON DELETE SET NULL);

CREATE TABLE user_rating (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title_id varchar(100),
    rating int,
    FOREIGN KEY (title_id) REFERENCES title(title_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES app_user(id) ON DELETE SET NULL);
