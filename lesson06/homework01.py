# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
# осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep
from datetime import datetime as dt


class TrafficLight:
    _states = {"красный": 7, "желтый": 2, "зеленый": 10}
    _color = ""

    def running(self):
        for color, sw_time in self._states.items():
            self._color = color
            start_state_time = dt.now()

            print(f"Светофор переключился на {self._color} "
                  f"на {sw_time} секунд")

            sleep(sw_time)

            print(f"Светофор перестал показывать {self._color} после " 
                  f"{(dt.now() - start_state_time).seconds} секунд")


if __name__ == "__main__":
    tl = TrafficLight()
    tl.running()
