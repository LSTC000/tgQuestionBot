from data.paths import NARUTO_IMAGE_PATH_0


NARUTO_NAME = 'Naruto'
NARUTO_DATA = {
    0: {
        'image': {
            'path': NARUTO_IMAGE_PATH_0,
            'bytes': None,
            'url': None
        },
        'question': 'Вопрос 1',
        'answers': ['A', 'B', 'C', 'D']
    },
    1: {
        'image': None,
        'question': 'Вопрос 2',
        'answers': ['A', 'B', 'C', 'D']
    }
}
NARUTO_QUESTIONS_COUNT = len(NARUTO_DATA)
