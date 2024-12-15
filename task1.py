import doctest
# TODO Написать 3 класса с документацией и аннотацией типов

class Pencil:
    """
    Класс хранящий данные о карандаше

    >>> pencil = Pencil("red", 10, "HB")
    >>> pencil.color
    'red'
    """

    def __init__(self, color: str, length: float, hardness: str):
        """
        Создание и подготовка к работе объекта "Карандаш"

        :param color: Цвет карандаша
        :param length: Длина карандаша в см
        :param hardness: Твёрдость грифеля карандаша (например, "2B", "HB", "2H")
        :raises TypeError: Если длина не является числом
        :raises ValueError: Если длина не положительная
        """

        self.color = color
        if not isinstance(length, (int, float)):
            raise TypeError("Длина должна быть числом")
        if length <= 0:
            raise ValueError("Длина должна быть положительной")
        self.length = length
        self.hardness = hardness

    def sharpen(self, amount: float) -> None:
        """
        Затачивает карандаш, уменьшая его длину

        :param amount: Величина, на которую необходимо заточить карандаш, в см.
        :raises TypeError: Если сумма не является числом
        :raises ValueError: Если сумма не положительная или не больше длины карандаша
        >>> pencil = Pencil("red", 10, "HB")
        >>> pencil.sharpen(1)

        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self.length:
             raise ValueError("Сумма не может быть больше длины карандаша")
        ...


    def write(self, paper) -> None:
        """
        Пишет на листе бумаги карандашом

        :param paper: Бумага — предмет, на котором можно писать
        >>> pencil = Pencil("red", 10, "HB")
        >>> paper = Paper("A4", 210, 297)
        >>> pencil.write(paper)
        """
        ...

    def erase(self, paper) -> None:
        """
        Стирает надписи на листе бумаги

        :param paper: Объект «Бумага», на котором нужно стереть надпись.
        >>> pencil = Pencil("red", 10, "HB")
        >>> paper = Paper("A4", 210, 297)
        >>> pencil.erase(paper)

        """
        ...




class Paper:
    """
    Класс храняший данные о листе бумаги

    >>> paper = Paper("A4", 210, 297)
    >>> paper.size
    'A4'
    """
    def __init__(self, size: str, width: float, height: float):
        """
        Создание и подготовка к работе объекта "Бумага"

        :param size: Размер бумаги (например, "A4", "Letter").
        :param width: Ширина бумаги в мм.
        :param height: Высота бумаги в мм.
        :raises TypeError: Если ширина или высота не являются числами.
        :raises ValueError: Если ширина или высота не являются положительными
        """

        self.size = size
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина должна быть числом")
        if width <= 0:
            raise ValueError("Ширина должна быть положительной")
        self.width = width
        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть числом")
        if height <= 0:
            raise ValueError("Высота должна быть положительной")
        self.height = height


    def fold(self, folds_count: int) -> None:
        """
        Складывает бумагу. Каждый сгиб уменьшает ширину или высоту пополам
        :param folds_count: Количество сгибов
        :raises TypeError: Если folds_count не является целым числом
        :raises ValueError: Если folds_count отрицательный
        >>> paper = Paper("A4", 210, 297)
        >>> paper.fold(2)
        """
        if not isinstance(folds_count, int):
            raise TypeError("Количество складок должно быть целым числом")
        if folds_count < 0:
            raise ValueError("Количество складок не может быть отрицательным")
        ...

    def write_on_paper(self, text: str) -> None:
        """
        Пишет текст на бумаге

        :param text: Текст, который нужно написать.
        >>> paper = Paper("A4", 210, 297)
        >>> paper.write_on_paper("Hello")
        """
        ...


    def tear(self, pieces: int) -> None:
        """
        Разрывает бумагу на несколько частей

        :param pieces: Количество кусочков, на которые нужно разорвать бумагу
        :raises TypeError: Если pieces не является целым числом
        :raises ValueError: Если Число должно быть целым числом не является положительным числом
        >>> paper = Paper("A4", 210, 297)
        >>> paper.tear(2)
        """
        if not isinstance(pieces, int):
            raise TypeError("Pieces должно быть целым числом.")
        if pieces <= 0:
            raise ValueError("Pieces должен быть положительным")
        ...

class Balloon:
    """
    Класс хранящий данные о воздушном шарике
    >>> balloon = Balloon("red", 10, "round")
    >>> balloon.color
    'red'
    """

    def __init__(self, color: str, size: float, shape: str):
        """
        Создание и подготовка к работе объекта "Воздушный шарик"

        :param color: Цвет воздушного шара
        :param size: Размер воздушного шара в см (диаметр, если он круглый, иначе самая длинная сторона)
        :param shape: Форма воздушного шара (например, длинный, круглый)
        :raises TypeError: Если размер не является числом
        :raises ValueError: Если размер не положительный

        """
        self.color = color
        if not isinstance(size, (int, float)):
             raise TypeError("Размер должен быть числом")
        if size <= 0:
            raise ValueError("Размер должен быть положительным")

        self.size = size
        self.shape = shape
        self.inflated = False

    def inflate(self, amount: float) -> None:
        """
        Надувает шарик

        :param amount: Количество воздуха для надувания в дм^3
        :raises TypeError: Если количество воздуха не является числом
        :raises ValueError: Если количество воздуха является отрицательным
        >>> balloon = Balloon("red", 10, "round")
        >>> balloon.inflate(5)
        """

        if not isinstance(amount, (int, float)):
             raise TypeError("Количество воздуха должно быть числом")
        if amount < 0 :
            raise ValueError("Количество воздуха не должно быть отрицательным")
        ...

    def deflate(self, amount: float) -> None:
        """
        Сдувает воздушный шар

        :param amount: Количество воздуха, которое необходимо спустить в см^3
        :raises TypeError: Если количество воздуха не является числом
        :raises ValueError:  Если количество воздуха является отрицательным

        >>> balloon = Balloon("red", 10, "round")
        >>> balloon.inflate(5) # Сначала надуваем для примера
        >>> balloon.deflate(2)

        """
        if not isinstance(amount, (int, float)):
             raise TypeError("оличество воздуха должно быть числом")
        if amount < 0 :
            raise ValueError("Количество воздуха не должно быть отрицательным")
        ...


    def tie(self) -> None:
        """
        Завязывание шарика, чтобы воздух не выходил

        >>> balloon = Balloon("red", 10, "round")
        >>> balloon.tie()

        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
