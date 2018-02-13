--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.6
-- Dumped by pg_dump version 9.5.6

ALTER TABLE IF EXISTS ONLY public.users DROP CONSTRAINT IF EXISTS pk_user_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.expenses DROP CONSTRAINT IF EXISTS pk_expense_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.exp_categories DROP CONSTRAINT IF EXISTS pk_exp_category_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.incomes DROP CONSTRAINT IF EXISTS pk_income_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.inc_categories DROP CONSTRAINT IF EXISTS pk_inc_category_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.expenses DROP CONSTRAINT IF EXISTS fk_user_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.incomes DROP CONSTRAINT IF EXISTS fk_user_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.expenses DROP CONSTRAINT IF EXISTS fk_exp_category_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.incomes DROP CONSTRAINT IF EXISTS fk_inc_category_id CASCADE;


DROP TABLE IF EXISTS public.users;
DROP SEQUENCE IF EXISTS public.user_id_seq;
CREATE TABLE users (
    id serial NOT NULL,
    name VARCHAR(64),
    username VARCHAR(32),
    password text,
    email text,
    submission_time timestamp without time zone,
    role text
);

DROP TABLE IF EXISTS public.expenses;
DROP SEQUENCE IF EXISTS public.expense_id_seq;
CREATE TABLE expenses (
    id serial NOT NULL,
    name VARCHAR(64),
    exp_category_id INTEGER,
    price INTEGER,
    submission_time timestamp without time zone,
    user_id INTEGER,
    comment VARCHAR(256)
);

DROP TABLE IF EXISTS public.exp_categories;
DROP SEQUENCE IF EXISTS public.exp_category_id_seq;
CREATE TABLE exp_categories (
    id serial NOT NULL,
    name text
);


DROP TABLE IF EXISTS public.incomes;
DROP SEQUENCE IF EXISTS public.income_id_seq;
CREATE TABLE incomes (
    id serial NOT NULL,
    name VARCHAR(64),
    inc_category_id INTEGER,
    price INTEGER,
    submission_time timestamp without time zone,
    user_id INTEGER,
    comment VARCHAR(256)
);

DROP TABLE IF EXISTS public.inc_categories;
DROP SEQUENCE IF EXISTS public.inc_category_id_seq;
CREATE TABLE inc_categories (
    id serial NOT NULL,
    name text
);


ALTER TABLE ONLY users
    ADD CONSTRAINT pk_user_id PRIMARY KEY (id);

ALTER TABLE ONLY expenses
    ADD CONSTRAINT pk_expense_id PRIMARY KEY (id);

ALTER TABLE ONLY exp_categories
    ADD CONSTRAINT pk_exp_category_id PRIMARY KEY (id);

ALTER TABLE ONLY incomes
    ADD CONSTRAINT pk_income_id PRIMARY KEY (id);

ALTER TABLE ONLY inc_categories
    ADD CONSTRAINT pk_inc_category_id PRIMARY KEY (id);

ALTER TABLE ONLY expenses
    ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id);

ALTER TABLE ONLY incomes
    ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id);

ALTER TABLE ONLY expenses
    ADD CONSTRAINT fk_exp_category_id FOREIGN KEY (exp_category_id) REFERENCES exp_categories(id);

ALTER TABLE ONLY incomes
    ADD CONSTRAINT fk_inc_category_id FOREIGN KEY (inc_category_id) REFERENCES inc_categories(id);

INSERT INTO users VALUES (0, 'Kiss Béla', 'Bélus', NULL, 'kiss.bela@citromail.hu', '2017-04-29 09:19:00', NULL);
INSERT INTO users VALUES (1, 'Nagy Józsi', 'Jocó', NULL, 'nagy.jozsef@freemail.com', '2017-04-29 09:19:00', NULL);

INSERT INTO exp_categories VALUES (0, 'Food');
INSERT INTO exp_categories VALUES (1, 'Service');

INSERT INTO expenses VALUES (0, 'Random Étterem', 0, 15000, '2017-04-29 09:19:00', 0, 'Jó szar volt, de legalább drága!!!');
INSERT INTO expenses VALUES (1, 'Masszázs', 1, 19000, '2017-04-29 09:19:00', 1, 'Béna volt a csaj, de legalább csinos');

INSERT INTO inc_categories VALUES (0, 'Work');
INSERT INTO inc_categories VALUES (1, 'Crypto mining');

INSERT INTO incomes VALUES (0, 'Black work', 0, 19000, '2017-04-29 09:19:00', 0, 'Golden shower');
INSERT INTO incomes VALUES (1, 'Doge coin exchange', 1, 19000, '2017-04-29 09:19:00', 1, 'Chinese dark web stock market');

