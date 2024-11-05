DROP TABLE IF EXISTS listings;
DROP SEQUENCE IF EXISTS listings_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    email text,
    password text
);

-- id | name | description | price_per_night | availability  | user_id

CREATE SEQUENCE IF NOT EXISTS listings_id_seq;
CREATE TABLE listings (
    id SERIAL PRIMARY KEY,
    name text,
    description text,
    price int,
    user_id int,
    constraint fk_user foreign key(user_id) references users(id) on delete cascade
);


INSERT INTO users (username, email, password) VALUES ('Harman1', 'h@email.com', 'password123');
INSERT INTO users (username, email, password) VALUES ('Naomi2', 'n@mail.co.uk', 'password123');
INSERT INTO users (username, email, password) VALUES ('Doug3', 'doug@email.com', 'password123');
INSERT INTO users (username, email, password) VALUES ('aaron4', 'aaron@mail.co.uk', 'password123');

INSERT INTO listings(name, description, price, user_id) VALUES ('Alpine Retreat Lodge', 'A cozy, rustic lodge in the mountains featuring three bedrooms, a fireplace, and a hot tub with scenic woodland views.', 220, 4);
INSERT INTO listings(name, description, price, user_id) VALUES ('City Chic Loft', 'A sleek, modern loft in the heart of the city with an open floor plan and panoramic views, ideal for urban adventurers.', 200, 2);
INSERT INTO listings(name, description, price, user_id) VALUES ('Seaside Serenity', 'A peaceful coastal retreat with stunning ocean views, a private balcony, and luxurious modern amenities.', 100, 1);