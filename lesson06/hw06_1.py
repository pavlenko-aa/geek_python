import time


class TrafficLight:

    _colour = {"Красный": 7, "Желтый": 2, "Зеленый": 7}

    def running(self):
        while True:
            for key in self._colour:
                print(key)
                time.sleep(self._colour[key])


a = TrafficLight()
a.running()
