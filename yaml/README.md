# Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"


## Обязательная задача 1
Мы выгрузили JSON, который получили через API запрос к нашему сервису:
```
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            }
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }

    { "info" : "Sample JSON output from our service",
        "elements" : [
            { "name" : "first",
            "type" : "server",
            "ip" : "71.75.23.43" 
            },
            { "name" : "second",
            "type" : "proxy",
            "ip" : "71.78.22.43"
            }
        ]
    }

```
  Нужно найти и исправить все ошибки, которые допускает наш сервис

## Обязательная задача 2
В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: `{ "имя сервиса" : "его IP"}`. Формат записи YAML по одному сервису: `- имя сервиса: его IP`. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.

### Ваш скрипт:
```python
#!/usr/bin/env python3
import os
import socket
import urllib.request
import json
import yaml
data = {}
with open("./test.txt", "r+") as file_:
        NewStr = ""
        data["service"] = []
        for item in file_:
                words = item.split()
                if len(words) < 1:
                        continue
                NewIP = socket.gethostbyname(words[0])
                print(words[0] + " - " + NewIP)
                try:
                        response = urllib.request.urlopen("http://" + words[0],timeout=2)
                except:
                        print("[ERROR] http://" +  words[0] + " IP mismatch: " + words[1] + " " + NewIP)
                NewStr += words[0] + "\t" + NewIP + "\n"
                data["service"].append({words[0]: NewIP})
        file_.seek(0)
        file_.write(NewStr)
with open("./test.json","w") as outfile:
        json.dump(data, outfile)
with open("./test.yaml","w") as outfile:
        yaml.dump(data, outfile)

```

### Вывод скрипта при запуске при тестировании:
```
google.com - 142.250.150.101
mail.google.com - 108.177.14.83
drive.google.com - 192.168.250.250
[ERROR] http://drive.google.com IP mismatch: 64.233.165.194 192.168.250.250

```

### json-файл(ы), который(е) записал ваш скрипт:
```json
{"service": [{"google.com": "142.250.150.101"}, {"mail.google.com": "108.177.14.83"}, {"drive.google.com": "192.168.250.250"}]}
```

### yml-файл(ы), который(е) записал ваш скрипт:
```yaml
service:
- google.com: 142.250.150.101
- mail.google.com: 108.177.14.83
- drive.google.com: 192.168.250.250
```

## Дополнительное задание (со звездочкой*) - необязательно к выполнению

Так как команды в нашей компании никак не могут прийти к единому мнению о том, какой формат разметки данных использовать: JSON или YAML, нам нужно реализовать парсер из одного формата в другой. Он должен уметь:
   * Принимать на вход имя файла
   * Проверять формат исходного файла. Если файл не json или yml - скрипт должен остановить свою работу
   * Распознавать какой формат данных в файле. Считается, что файлы *.json и *.yml могут быть перепутаны
   * Перекодировать данные из исходного формата во второй доступный (из JSON в YAML, из YAML в JSON)
   * При обнаружении ошибки в исходном файле - указать в стандартном выводе строку с ошибкой синтаксиса и её номер
   * Полученный файл должен иметь имя исходного файла, разница в наименовании обеспечивается разницей расширения файлов

### Ваш скрипт:
```python
???
```

### Пример работы скрипта:
```
???
```
