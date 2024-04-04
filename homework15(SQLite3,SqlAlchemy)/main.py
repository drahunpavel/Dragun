import sqlite3

connection = sqlite3.connect(
    'homework15 (SQLite3,SqlAlchemy)/db/SQLite/example.db')
cursor = connection.cursor()


def get_data_from_db() -> None:
    # При помощи “сырого” запроса вывести все фильмы, которые были сняты с 2015 по 2020 год.
    cursor.execute(
        'SELECT name_movie as name FROM movies WHERE release >= 2015 AND release <=2020')
    movies = cursor.fetchall()
    movies_list = convert_list_tuple_to_list_sting(movies)
    print('task_1: ', movies_list)

    # Использую SQLite3 при помощи “сырого”  запроса вывести актёров и режиссёров, которые не участвовали не в одном из фильмов.
    cursor.execute(
        '''SELECT directors.name || " " || directors.surname AS name
        FROM directors
        LEFT JOIN movies ON directors.director_id = movies.director_id
        WHERE movies.director_id IS NULL

        UNION

        SELECT actors_2.name || " " || actors_2.surname AS name
        FROM actors_2
        LEFT JOIN actors_movies ON actors_2.actors_id = actors_movies.actors_id
        WHERE actors_movies.actors_id IS NULL;''')
    names = cursor.fetchall()
    names_list = convert_list_tuple_to_list_sting(names)
    print('task_2: ', names_list)

    # Используя SQLite3 при помощи “сырого”  запроса вывести все фильмы  которые были сняты после 2000 года и в которых приняло участие более 1 актёра.
    cursor.execute(
        '''SELECT name_movie as name 
        FROM movies 
        JOIN actors_movies ON actors_movies.movie_id = movies.movie_id
        WHERE movies.release > 2000
        GROUP BY name_movie 
        HAVING COUNT(actors_movies.actors_id) > 1;
        ''')
    movies_2 = cursor.fetchall()
    movies_list_2 = convert_list_tuple_to_list_sting(movies_2)
    print('task_3: ', movies_list_2)

    # Используя SQLite3 при помощи “сырого”  запроса вывести первых 5 самых высокооплачиваемых актёров.
    cursor.execute(
        '''
        SELECT actors_2.name || " " || actors_2.surname AS actor_name
        FROM bank_accounts
        JOIN actors_2 ON actors_2.actors_id = bank_accounts.bank_account_id
        ORDER BY bank_accounts.finance DESC LIMIT 5;
        ''')
    high_paid_actors = cursor.fetchall()
    print(high_paid_actors)
    high_paid_actors_list = convert_list_tuple_to_list_sting(high_paid_actors)
    print('task_4: ', high_paid_actors_list)

    # Использую SQLite3 при помощи “сырого”  запроса вывести всех режиссёров и актёров которые были задействованы только в 1 фильме.
    cursor.execute(
        '''
        SELECT actors_2.name || " " || actors_2.surname AS name
        FROM actors_2
        JOIN actors_movies ON actors_movies.actors_id = actors_2.actors_id
        GROUP BY actors_2.actors_id 
        HAVING COUNT(actors_movies.actors_id) = 1

        UNION

        SELECT directors.name || " " ||   directors.surname AS name
        FROM directors
        JOIN movies ON directors.director_id = movies.director_id
        GROUP BY directors.director_id
        HAVING COUNT(movies.movie_id) = 1;
        ''')
    in_one_movie = cursor.fetchall()
    in_one_movie_list = convert_list_tuple_to_list_sting(in_one_movie)
    print('task_5', in_one_movie_list)
    pass


def convert_list_tuple_to_list_sting(list: list[tuple]) -> list[str]:
    return [''.join(i) for i in list]


get_data_from_db()

connection.close()
