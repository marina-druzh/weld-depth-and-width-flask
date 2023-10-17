# Flask_ml
## Итоговая аттестация по курсу Аналитик данных/Data Scientist МГТУ им Баумана

### Задача:
Используя результаты выполнения практического кейса «Прогнозирование размеров сварного шва при электронно-лучевой сварке тонкостенных конструкций аэрокосмического назначения» разработать приложение, цель которого прогнозирование ширины и глубины сварного соединения. Приложение может быть любым - консольным, web или GUI. Отчет должен содержать описание функционала приложения, руководство пользователя, демонстрацию работу.

### Описание функционала приложения:
В качестве исходных данных в приложение необходимо ввести:

Величину сварочного тока (IW)
Величину тока фокусировки электронного пучка (IF)
Скорость сварки (VW)
Расстояние от поверхности образцов до электронно-оптической системы (FP)

Исходя из введенных параметров приложение прогнозирует размеры сварных швов:

Глубина шва (Depth)
Ширина шва (Width)

В основу приложения положена модель машинного обучения, обученная на наборе экспериментально полученных данных.

