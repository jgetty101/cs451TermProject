CREATE TABLE Users (
    userID CHAR(22),
    userName VARCHAR(30),
    average_stars FLOAT,
    date_joined DATETIME,
    number_of_fans INTEGER,
    count_of_votes INTEGER,
    tip_count INTEGER,
    tip_likes INTEGER,
    user_location FLOAT,
    latitude FLOAT,
    longitude FLOAT,
    friends VARCHAR(30),
    PRIMARY KEY (userID)
);

CREATE TABLE Businesses (
    business_address VARCHAR,
    b_state VARCHAR,
    city VARCHAR,
    street VARCHAR,
    zipcode INTEGER,
    price FLOAT,
    attributes VARCHAR,
    meal VARCHAR,
    category VARCHAR,
    check_ins DATETIME,
    rating FLOAT,
    tips_provided VARCHAR,
    business_name VARCHAR,
    week_day VARCHAR,
    b_opens DATE,
    b_closes VARCHAR,
    PRIMARY KEY (business_address, b_state, city)
);