# Симуляция
Симуляция 2D-мира, который может быть наполнен травоядными и хищниками.

Кроме того, он может содержать камни, траву и деревья. Хищники питаются травоядными, а травоядные питаются травой (неожиданно, правда?)

![Screenshot](https://i.imgur.com/dEnA1Xv.png)

## Правила симуляции
- Хищники обозначаются красным цветом
- Травоядные обозначаются белым цветом
- Если поблизости нет еды (на растоянии 10 клеток), любой хищник или травоядное каждый ход симуляции переходит в случайную соседнюю клетку (включая ту, на которой сейчас находится)
- Если еда находится, хищник или травоядное направляется в сторону еды и поедает ее

## Установка и запуск

### Установка
```
git clone https://github.com/lapindanil22/simulation-python.git
cd simulation-python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Запуск
```
python main.py
```