__all__ = [
    'get_users_alert',
    'add_user_alert',
    'add_user_info',
    'add_game_info',
    'add_test_info',
    'add_user_review',
    'add_users_n_games',
    'add add_users_n_tests.py',
    'delete_user_alert',
    'update_user_opened_games',
    'update_user_completed_games',
    'update_user_opened_tests',
    'update_user_completed_tests',
    'update_user_likes',
    'update_user_dislikes',
    'update_game_attempts',
    'update_game_completed_attempts',
    'update_game_likes',
    'update_game_dislikes',
    'update_test_attempts',
    'update_test_completed_attempts',
    'update_test_likes',
    'update_test_dislikes',
    'check_user_alert',
    'check_user_info',
    'check_game_info',
    'check_test_info'
]


# Alerts.
from .get_users_alert import get_users_alert
from .add_user_alert import add_user_alert
from .delete_user_alert import delete_user_alert
from .check_user_alert import check_user_alert
# UsersInfo.
from .add_user_info import add_user_info
from .update_user_opened_games import update_user_opened_games
from .update_user_completed_games import update_user_completed_games
from .update_user_opened_tests import update_user_opened_tests
from .update_user_completed_tests import update_user_completed_tests
from .update_user_likes import update_user_likes
from .update_user_dislikes import update_user_dislikes
from .check_user_info import check_user_info
# GamesInfo.
from .add_game_info import add_game_info
from .update_game_attempts import update_game_attempts
from .update_game_completed_attempts import update_game_completed_attempts
from .update_game_likes import update_game_likes
from .update_game_dislikes import update_game_dislikes
from .check_game_info import check_game_info
# TestsInfo.
from .add_test_info import add_test_info
from .update_test_attempts import update_test_attempts
from .update_test_completed_attempts import update_test_completed_attempts
from .update_test_likes import update_test_likes
from .update_test_dislikes import update_test_dislikes
from .check_test_info import check_test_info
# Reviews
from .add_user_review import add_user_review
# UsersAndGames.
from .add_users_n_games import add_users_n_games
# UsersAndTests.
from .add_users_n_tests import add_users_n_tests
