import os
import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    "Загружает данные из CSV-файла"
    try:
        df = pd.read_csv(file_path)
        print("Данные успешно загружены!")
        print("Размер таблицы:", df.shape)
        return df
    except FileNotFoundError:
        print("Ошибка: файл не найден. Убедитесь, что train.csv лежит рядом.")
        return None


def show_basic_info(df):
    "Показывает базовую информацию о данных"
    print("\nПервые 5 строк таблицы:")
    print(df.head())

    print("\nИнформация о столбцах:")
    print(df.info())

    print("\nСтатистика по числовым столбцам:")
    print(df.describe())


def plot_survival(df):
    "Строит график выживаемости (выжил / погиб)."
    # Считаем, сколько было выживших (1) и погибших (0)
    survived_counts = df['Survived'].value_counts()

    plt.figure(figsize=(6, 4))
    plt.bar(['Погиб', 'Выжил'], survived_counts, color=['red', 'green'])
    plt.title('Количество выживших и погибших пассажиров')
    plt.xlabel('Статус')
    plt.ylabel('Количество человек')
    plt.grid(axis='y')
    plt.show()


def plot_age_distribution(df):
    "Строит гистограмму распределения возрастов."
    plt.figure(figsize=(8, 5))

    # Берем столбец Age и убираем пустые значения
    ages = df['Age'].dropna()

    plt.hist(ages, bins=20, color='skyblue', edgecolor='black')
    plt.title('Распределение возраста пассажиров')
    plt.xlabel('Возраст (лет)')
    plt.ylabel('Количество человек')
    plt.grid(axis='y')
    plt.show()


def plot_survival_by_sex(df):
    "Строит график выживаемости в зависимости от пола."
    # Группируем данные по полу и статусу выживания
    grouped = df.groupby(['Sex', 'Survived']).size().unstack()

    # Строим сгруппированную столбчатую диаграмму
    grouped.plot(kind='bar', figsize=(8, 5), color=['red', 'green'])

    plt.title('Выживаемость пассажиров по полу')
    plt.xlabel('Пол')
    plt.ylabel('Количество человек')
    plt.xticks(rotation=0)  # Чтобы подписи "male" и "female" не наклонялись
    plt.legend(['Погиб', 'Выжил'])
    plt.grid(axis='y')
    plt.show()


if __name__ == "__main__":
    # Эта команда автоматически определяет папку, в которой лежит файл 5.3.py
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Склеиваем путь к папке с именем файла
    file_path = os.path.join(current_dir, 'train.csv')
    
    # Передаем этот путь в функцию загрузки
    data = load_data(file_path)

    if data is not None:
        show_basic_info(data)
        plot_survival(data)
        plot_age_distribution(data)
        plot_survival_by_sex(data)
