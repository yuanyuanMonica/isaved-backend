from app import app

from datetime import datetime


# """TODO"""
# @app.route('/tag/addItem')
# def add_item():
#     """Description of function TODO
#
#     TODO
#
#     Args:
#         TODO
#
#
#     Returns:
#         TODO
#     """
#
#     tag = database.UserTagTable(1, 1)
#
#
#     return "adding item"


"""TODO"""
# @app.route('/tag/removeItem')
# def add_item():
#     """Description of function TODO
#
#     TODO
#
#     Args:
#         TODO
#
#
#     Returns:
#         TODO
#     """
#
#     return "removing item"



@app.route('/tag/modifyItem')
def modify_item():
    """Update modification of users to database

    This function return status code(100 = successful, 200 = failed)

    Args:
        userID: corresponding to current user
        itemID:
        LastUpdateTime:
        Title(optional):
        tag(optional):


    Returns:
        TODO
    """

    lastUpdateTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return str(lastUpdateTime)
