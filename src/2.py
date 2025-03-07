def get_projects(username):
    # Connect to database
    conn = psycopg2.connect("dbname=schoolproject")
    cur = conn.cursor()

    # Get projects for the given username
    cur.execute("SELECT * FROM projects WHERE owner=%s", (username,))
    projects = cur.fetchall()

    # Close database connection
    cur.close()
    conn.close()

    return projects
