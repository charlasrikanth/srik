#! /usr/bin/env python

import psycopg2

sri = "news"


def act(query):
    """Connects to the database, runs the query 
	and returns the results"""
    db = psycopg2.connect('dbname=' + sri)
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows


def sri_articles():
    """Returns top 3 most read articles"""

    # Build Query String
    query = """
        SELECT articles.title,
                   count(*)
            FROM   log,
                   articles
            WHERE  log.path = '/article/' || articles.slug
            GROUP BY articles.title
            ORDER BY count(*) DESC
            LIMIT 3;
    """

    # Run Query
    results = act(query)

    # Print Results
    print('\nTOP THREE ARTICLES BY PAGE VIEWS:')
    count = 1
    for i in results:
        number = '(' + str(count) + ') "'
        title = i[0]
        views = '" with ' + str(i[1]) + " views"
        print(number + title + views)
        count += 1


def sri_authors():
    """returns top 3 most popular authors"""

    # Build Query String
    query = """
        SELECT authors.name,
                   count(*)
            FROM   log,
                   articles,
                   authors
            WHERE  log.path = '/article/' || articles.slug
              AND articles.author = authors.id
            GROUP BY authors.name
            ORDER BY count(*) DESC;
    """

    # Run Query
    results = act(query)

    # Print Results
    print('\nTOP THREE AUTHORS BY VIEWS:')
    count = 1
    for i in results:
        print('(' + str(count) + ') ' + i[0] + ' with ' + str(i[1]) + " views")
        count += 1


def sri_errors():
    """returns days with more than 1% errors"""

    # Build Query String
    query = """
        SELECT total.day,
          ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent
        FROM (
          SELECT date_trunc('day', time) "day", count(*) AS error_requests
          FROM log
          WHERE status LIKE '404%'
          GROUP BY day
        ) AS errors
        JOIN (
          SELECT date_trunc('day', time) "day", count(*) AS requests
          FROM log
          GROUP BY day
          ) AS total
        ON total.day = errors.day
        WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
        ORDER BY percent DESC;
    """

    # Run Query
    results = act(query)

    # Print Results
    print('\nDAYS WITH MORE THAN 1% ERRORS:')
    for i in results:
        date = i[0].strftime('%B %d, %Y')
        errors = str(round(i[1]*100, 1)) + "%" + " errors"
        print(date + " -- " + errors)

print('Calculating Results...\n')
sri_articles()
sri_authors()
sri_errors()
