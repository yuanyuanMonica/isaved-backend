from app import app
from app import database

@app.route('/example_query')
def example_query():
    """This is an example of query

    This function return all rows in user_tag_table to the webpage.

    Args:
        None

    Returns:
        str, the string converted from the result of query all rows from the
        user_tag_table.
    """
    example = database.UserTagTable.query.filter().all()
    return str(example)
