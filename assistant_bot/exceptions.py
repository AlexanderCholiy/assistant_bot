class EnvVarsErr(Exception):

    def __init__(self, missing_vars: list[str]) -> None:
        joined_vars = '\n- '.join(missing_vars)
        message = (
            'Ошибка: отсутствуют переменные окружения:\n'
            f'- {joined_vars}'
        )
        super().__init__(message)


class DirExistErr(Exception):

    def __init__(self, missing_dirs: list[str]) -> None:
        joined_dirs = '\n- '.join(missing_dirs)
        message = (
            'Ошибка: не найдены следующие директории:\n'
            f'- {joined_dirs}'
        )
        super().__init__(message)


class FileExistErr(Exception):

    def __init__(self, missing_files: list[str]) -> None:
        joined_files = '\n- '.join(missing_files)
        message = (
            'Ошибка: не найдены следующие файлы:\n'
            f'- {joined_files}'
        )
        super().__init__(message)
