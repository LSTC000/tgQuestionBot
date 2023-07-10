from data.paths import (
    AVENGERS_QUESTION_IMAGE_PATH_0,
    AVENGERS_RESULT_IMAGE_PATH_0,
    AVENGERS_RESULT_IMAGE_PATH_1,
    AVENGERS_RESULT_IMAGE_PATH_2,
    AVENGERS_RESULT_IMAGE_PATH_3,
    AVENGERS_RESULT_IMAGE_PATH_4,
    AVENGERS_RESULT_IMAGE_PATH_5,
    AVENGERS_RESULT_IMAGE_PATH_6,
    AVENGERS_RESULT_IMAGE_PATH_7,
    AVENGERS_RESULT_IMAGE_PATH_8,
    AVENGERS_RESULT_IMAGE_PATH_9,
)


# 0 - Тор
# 1 - Халк
# 2 - Железный Человек
# 3 - Черная Вдова
# 4 - Капитан Америка
# 5 - Черная Пантера
# 6 - Вижн
# 7 - Ванда
# 8 - Сокалиный глаз
# 9 - Кейт Бишоп

AVENGERS_NAME = 'Кто ты из Мстителей?'
AVENGERS_RESULTS_DATA = {
    'finder_method': 'best_weight',
    0: {
        'image': {
            'path': AVENGERS_RESULT_IMAGE_PATH_0,
            'bytes': None,
            'url': None
        },
        'description': 'Ты Тор'
    },
    1: {
        'image': {
            'path': AVENGERS_RESULT_IMAGE_PATH_1,
            'bytes': None,
            'url': None
        },
        'description': 'Ты Халк'
    },
    2: {
        'image': {
            'path': AVENGERS_RESULT_IMAGE_PATH_2,
            'bytes': None,
            'url': None
        },
        'description': 'Ты Железный Человек'
    },
    3: {
        'image': {
            'path': AVENGERS_RESULT_IMAGE_PATH_3,
            'bytes': None,
            'url': None
        },
        'description': 'Ты Черная Вдова'
    },
    4: {
        'image': {
            'path': AVENGERS_RESULT_IMAGE_PATH_4,
            'bytes': None,
            'url': None
        },
        'description': 'Ты Капитан Америка'
    },
    5: {
        'image': {
            'path': AVENGERS_RESULT_IMAGE_PATH_5,
            'bytes': None,
            'url': None
        },
        'description': 'Ты Черная Пантера'
    },
    6: {
        'image': {
            'path': AVENGERS_RESULT_IMAGE_PATH_6,
            'bytes': None,
            'url': None
        },
        'description': 'Ты Вижн'
    },
    7: {
        'image': {
            'path': AVENGERS_RESULT_IMAGE_PATH_7,
            'bytes': None,
            'url': None
        },
        'description': 'Ты Скарлетт Ванда'
    },
    8: {
        'image': {
            'path': AVENGERS_RESULT_IMAGE_PATH_8,
            'bytes': None,
            'url': None
        },
        'description': 'Ты Сокалиный глаз'
    },
    9: {
        'image': {
            'path': AVENGERS_RESULT_IMAGE_PATH_9,
            'bytes': None,
            'url': None
        },
        'description': 'Ты Кейт Бишоп'
    },
}
AVENGERS_QUESTIONS_DATA = {
    0: {
        'image': {
            'path': AVENGERS_QUESTION_IMAGE_PATH_0,
            'bytes': None,
            'url': None
        },
        'question': 'Привет! Если ты фанат франшизы "Мстители", то этот тест для тебя! Ответь на несколько вопросов, и '
                    'мы определим, кто из Мстителей тебе наиболее близок. Готов проверить свои знания и узнать, кто ты '
                    'из команды Мстителей?',
        'answers': {
            'Начать 🦸‍♂️': {}
        }
    },
    1: {
        'image': {
            'path': AVENGERS_QUESTION_IMAGE_PATH_0,
            'bytes': None,
            'url': None
        },
        'question': 'Какая способность тебе ближе всего?',
        'answers': {
            'Сверхсила': {0: 1, 1: 1},
            'Интеллект и технические навыки': {2: 1, 3: 1},
            'Быстрота и гибкость': {4: 1, 5: 1},
            'Телекинез или телепатия': {6: 1, 7: 1},
            'Стрелковые навыки': {8: 1, 9: 1}
        }
    },
    2: {
        'image': {
            'path': AVENGERS_QUESTION_IMAGE_PATH_0,
            'bytes': None,
            'url': None
        },
        'question': 'Каким стилем сражения ты предпочитаешь?',
        'answers': {
            'Ближний бой': {0: 1, 1: 1},
            'Использование технологий': {2: 1, 3: 1},
            'Чистое боевое мастерство': {4: 1, 5: 1},
            'Магические возможности': {6: 1, 7: 1},
            'Меткость и стрелковые навыки': {8: 1, 9: 1}
        }
    },
    3: {
        'image': {
            'path': AVENGERS_QUESTION_IMAGE_PATH_0,
            'bytes': None,
            'url': None
        },
        'question': 'Что для тебя важнее всего?',
        'answers': {
            'Защита мира': {0: 1, 2: 1},
            'Борьба с преступностью': {3: 1, 4: 1},
            'Восстановление мира': {1: 1, 6: 1},
            'Изучение себя': {5: 1, 7: 1},
            'Опасные миссии': {8: 1, 9: 1}
        }
    },
    4: {
        'image': {
            'path': AVENGERS_QUESTION_IMAGE_PATH_0,
            'bytes': None,
            'url': None
        },
        'question': 'Какими чертами характера ты обладаешь?',
        'answers': {
            'Преданность друзьям': {3: 1, 4: 1},
            'Изобретательность': {2: 1, 7: 1},
            'Бесконечная сила': {0: 1, 1: 1},
            'Духовная сила': {5: 1, 6: 1},
            'Сноровка и проницательность': {8: 1, 9: 1}
        }
    },
    5: {
        'image': {
            'path': AVENGERS_QUESTION_IMAGE_PATH_0,
            'bytes': None,
            'url': None
        },
        'question': 'Какой цвет ты предпочитаешь?',
        'answers': {
            'Красный': {2: 1, 7: 1},
            'Синий': {4: 1, 6: 1},
            'Зеленый': {1: 1, 8: 1},
            'Черный': {3: 1, 5: 1},
            'Золотой': {0: 1, 9: 1}
        }
    },
    6: {
        'image': {
            'path': AVENGERS_QUESTION_IMAGE_PATH_0,
            'bytes': None,
            'url': None
        },
        'question': 'Какое место предпочитаешь для жизни?',
        'answers': {
            'Асгард': {0: 1},
            'Нью-Йорк': {2: 1, 3: 1},
            'Ваканда': {5: 1},
            'Квартира в городе': {4: 1},
            'Личное уединение': {6: 1, 7: 1},
            'Дикая природа': {1: 1, 8: 1, 9: 1},
        }
    },
    7: {
        'image': {
            'path': AVENGERS_QUESTION_IMAGE_PATH_0,
            'bytes': None,
            'url': None
        },
        'question': 'Какой транспорт предпочитаешь?',
        'answers': {
            'Свои ноги': {4: 1, 5: 1},
            'Истребитель': {2: 1, 6: 1},
            'Молот Тора': {0: 1},
            'Мотоцикл': {3: 1, 8: 1},
            'Стрела и лук': {9: 1}
        }
    },
    8: {
        'image': {
            'path': AVENGERS_QUESTION_IMAGE_PATH_0,
            'bytes': None,
            'url': None
        },
        'question': 'Какую одежду предпочитаешь?',
        'answers': {
            'Боевой костюм': {3: 1, 4: 1},
            'Элегантные наряды': {2: 1, 5: 1},
            'Кожаная куртка': {8: 1, 9: 1},
            'Мантия': {0: 1, 6: 1},
            'Магический наряд': {7: 1}
        }
    },
    9: {
        'image': {
            'path': AVENGERS_QUESTION_IMAGE_PATH_0,
            'bytes': None,
            'url': None
        },
        'question': 'Какой тип задачи ты предпочитаешь решать?',
        'answers': {
            'Борьба с преступностью': {3: 1, 4: 1},
            'Спасение мира': {0: 1, 2: 1},
            'Защита и восстановление': {1: 1, 6: 1},
            'Исследование': {5: 1, 7: 1},
            'Скрытная операция': {8: 1, 9: 1}
        }
    },
    10: {
        'image': {
            'path': AVENGERS_QUESTION_IMAGE_PATH_0,
            'bytes': None,
            'url': None
        },
        'question': 'Какую команду предпочитаешь?',
        'answers': {
            'Одинокий волк': {3: 1, 8: 1},
            'Команда лидеров': {4: 1, 5: 1},
            'Семья': {1: 1, 7: 1},
            'Друзья и партнеры': {9: 1},
            'Другое': {0: 1, 2: 1, 6: 1}
        }
    },
    11: {
        'image': {
            'path': AVENGERS_QUESTION_IMAGE_PATH_0,
            'bytes': None,
            'url': None
        },
        'question': 'Какой гаджет ты бы выбрал?',
        'answers': {
            'Репульсоры': {2: 1, 6: 1},
            'Молот Тора': {0: 1},
            'Серебряные стрелы': {8: 1, 9: 1},
            'Щит': {4: 1},
            'Нано-костюм': {5: 1}
        }
    }
}

