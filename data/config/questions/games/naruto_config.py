from data.paths import (
    NARUTO_QUESTION_IMAGE_PATH_0,
    NARUTO_QUESTION_IMAGE_PATH_1,
    NARUTO_QUESTION_IMAGE_PATH_2,
    NARUTO_QUESTION_IMAGE_PATH_3,
    NARUTO_QUESTION_IMAGE_PATH_4,
    NARUTO_QUESTION_IMAGE_PATH_5,
    NARUTO_QUESTION_IMAGE_PATH_6,
    NARUTO_QUESTION_IMAGE_PATH_7,
    NARUTO_QUESTION_IMAGE_PATH_8,
    NARUTO_QUESTION_IMAGE_PATH_9,
    NARUTO_QUESTION_IMAGE_PATH_10,
    NARUTO_QUESTION_IMAGE_PATH_11,
    NARUTO_RESULT_IMAGE_PATH_0,
    NARUTO_RESULT_IMAGE_PATH_1,
    NARUTO_RESULT_IMAGE_PATH_2,
)


NARUTO_NAME = 'Кто ты из Наруто?'
NARUTO_RESULTS_DATA = {
    0: {
        'image': {
            'path': NARUTO_RESULT_IMAGE_PATH_0,
            'bytes': None,
            'url': None
        },
        'description': 'Ты Наруто'
    },
    1: {
        'image': {
            'path': NARUTO_RESULT_IMAGE_PATH_1,
            'bytes': None,
            'url': None
        },
        'description': 'Ты Саске'
    },
    2: {
        'image': {
            'path': NARUTO_RESULT_IMAGE_PATH_2,
            'bytes': None,
            'url': None
        },
        'description': 'Ты Сакура'
    },
}
NARUTO_QUESTIONS_DATA = {
    0: {
        'image': {
            'path': NARUTO_QUESTION_IMAGE_PATH_0,
            'bytes': None,
            'url': None
        },
        'question': 'Привет! Если ты фанат аниме "Наруто", то этот тест для тебя! Ответь на несколько вопросов и наша '
                    'нейросеть определит, кто из персонажей этого удивительного мира тебе наиболее близок. '
                    'Готов проверить свои знания и узнать, кто ты из "Наруто"?',
        'answers': {
            'Начать 🥷': {},
        }
    },
    1: {
        'image': {
            'path': NARUTO_QUESTION_IMAGE_PATH_1,
            'bytes': None,
            'url': None
        },
        'question': 'Какой ваш возраст?',
        'answers': {
            'Молодой (18-26)': {0: 1, 1: 1, 2: 1},
            'Подросток(12-18)': {0: 1, 1: 1, 2: 1},
            'Взрослый (26-40)': {0: 1, 1: 1, 2: 1},
            'Пожилой (40-...)': {0: 1, 1: 1, 2: 1},
        }
    },
    2: {
        'image': {
            'path': NARUTO_QUESTION_IMAGE_PATH_2,
            'bytes': None,
            'url': None
        },
        'question': 'Насколько вы доверяете людям?',
        'answers': {
            'Я легко доверяю людям': {0: 1, 1: 1, 2: 1},
            'Я вообще им не доверяю': {0: 1, 1: 1, 2: 1},
            'Я не особо доверчив': {0: 1, 1: 1, 2: 1},
            'Доверяю но проверяю': {0: 1, 1: 1, 2: 1},
        }
    },
    3: {
        'image': {
            'path': NARUTO_QUESTION_IMAGE_PATH_3,
            'bytes': None,
            'url': None
        },
        'question': 'Как бы вы предпочли бы провести свободное время?',
        'answers': {
            'Тренироватся': {0: 1, 1: 1, 2: 1},
            'Читать': {0: 1, 1: 1, 2: 1},
            'Бездельничать': {0: 1, 1: 1, 2: 1},
            'Гулять, развлекатся': {0: 1, 1: 1, 2: 1},
            'У меня нет свободного времени': {0: 1, 1: 1, 2: 1},
        }
    },
    4: {
        'image': {
            'path': NARUTO_QUESTION_IMAGE_PATH_4,
            'bytes': None,
            'url': None
        },
        'question': 'Что для вас значит слово "друг"?',
        'answers': {
            'Тот с кем всегда можно поболтать': {0: 1, 1: 1, 2: 1},
            'Тот на кого можно положится': {0: 1, 1: 1, 2: 1},
            'Для меня это почти как семья': {0: 1, 1: 1, 2: 1},
            'Для меня это союзник': {0: 1, 1: 1, 2: 1},
            'Это просто слово': {0: 1, 1: 1, 2: 1},
        }
    },
    5: {
        'image': {
            'path': NARUTO_QUESTION_IMAGE_PATH_5,
            'bytes': None,
            'url': None
        },
        'question': 'В какой кампании вы бы хотели присутствовать?',
        'answers': {
            'Клан Учиха': {0: 0, 1: 10, 2: 0},
            'Команда №7': {0: 1, 1: 1, 2: 1},
            'Акацуки': {0: 0, 1: 10, 2: 0},
            'Анбу': {0: 1, 1: 1, 2: 1},
            'Ни в одной из них': {0: 1, 1: 1, 2: 1},
            'Клан Узумаки': {0: 10, 1: 0, 2: 0},
            'Каге': {0: 1, 1: 1, 2: 1},
            'Клан Хьюга': {0: 1, 1: 1, 2: 1},
        }
    },
    6: {
        'image': {
            'path': NARUTO_QUESTION_IMAGE_PATH_6,
            'bytes': None,
            'url': None
        },
        'question': 'Какой тип ведения боя предпочитаете?',
        'answers': {
            'Ниндзюцу': {0: 1, 1: 1, 2: 1},
            'Тайдзюцу': {0: 1, 1: 1, 2: 1},
            'Гендзюцу': {0: 1, 1: 1, 2: 1},
        }
    },
    7: {
        'image': {
            'path': NARUTO_QUESTION_IMAGE_PATH_7,
            'bytes': None,
            'url': None
        },
        'question': 'Какой ваш биологический пол?',
        'answers': {
            'Мужчина': {0: 10, 1: 10, 2: 0},
            'Женщина': {0: 0, 1: 0, 2: 10},
        }
    },
    8: {
        'image': {
            'path': NARUTO_QUESTION_IMAGE_PATH_8,
            'bytes': None,
            'url': None
        },
        'question': 'Чего вы больше боитесь?',
        'answers': {
            'Смерти': {0: 1, 1: 1, 2: 1},
            'Быть бесполезным': {0: 1, 1: 1, 2: 1},
            'Быть одиноким': {0: 1, 1: 1, 2: 1},
            'Быть слабым': {0: 1, 1: 1, 2: 1},
            'Быть забытым': {0: 1, 1: 1, 2: 1},
        }
    },
    9: {
        'image': {
            'path': NARUTO_QUESTION_IMAGE_PATH_9,
            'bytes': None,
            'url': None
        },
        'question': 'Какое слово вас лучше описывает?',
        'answers': {
            'Любовь': {0: 1, 1: 1, 2: 1},
            'Свобода': {0: 1, 1: 1, 2: 1},
            'Интеллект': {0: 1, 1: 1, 2: 1},
            'Жадность': {0: 1, 1: 1, 2: 1},
            'Рассудительность': {0: 1, 1: 1, 2: 1},
            'Рассудительность': {0: 1, 1: 1, 2: 1},
        }
    },
    10: {
        'image': {
            'path': NARUTO_QUESTION_IMAGE_PATH_10,
            'bytes': None,
            'url': None
        },
        'question': 'Что вы делаете когда что-то не выходит?',
        'answers': {
            'Брошу дело': {0: 1, 1: 1, 2: 1},
            'Я обычно справляюсь с первого раза': {0: 1, 1: 1, 2: 1},
            'Попрошу у кого-нибудь помощи': {0: 1, 1: 1, 2: 1},
            'Отдохну и снова за работу': {0: 1, 1: 1, 2: 1},
            'Буду трудится пока не выйдет': {0: 1, 1: 1, 2: 1},
        }
    },
    11: {
        'image': {
            'path': NARUTO_QUESTION_IMAGE_PATH_11,
            'bytes': None,
            'url': None
        },
        'question': 'Какой характер больше на вас похож?',
        'answers': {
            'Замкнутый, бесстрастный': {0: 1, 1: 1, 2: 1},
            'Непредсказуемый': {0: 1, 1: 1, 2: 1},
            'Спокойный, позитивный': {0: 1, 1: 1, 2: 1},
            'Жизнерадостный, общительный ': {0: 1, 1: 1, 2: 1},
            'Беземоциональный': {0: 1, 1: 1, 2: 1},
            'Резкий, агрессивный': {0: 1, 1: 1, 2: 1},
        }
    },
}
