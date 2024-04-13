import requests

if __name__ == '__main__':
    # выполняем POST-запрос на сервер по эндпоинту add с параметром json
    sqft = float(input('Введите sqft: '))
    zipcode = int(input('Введите zipcode: '))
    baths = float(input('Введите количество ванных комнат: '))
    Year_built = int(input('Введите год постройки: '))
    school_rating_mean = float(input('Введите срединий рейтинг школ: '))
    school_dist_min = float(input('Средняя дистанция до школ: '))
    city = str(input('Введите город: '))
    status = str(input('Введите статус продажи: '))
    state = str(input('Введите штат: '))
    Type = str(input('Введите тип недвижимости: '))
    pool_encoded = bool(input('Введите наличие бассейна (True\False): '))
    Heating_encoded = bool(input('Введите наличие отопления (True\False): '))
    Cooling_encoded = bool(input('Введите наличие кондиционера (True\False): '))
    Parking_encoded = bool(input('Введите наличие парковки (True\False): '))
    fireplace_encoded = bool(input('Введите наличие камина (True\False): '))
    
    
    r = requests.post('http://localhost:5000/predict', json=[sqft, zipcode, baths, Year_built, school_rating_mean, school_dist_min, city, status, state, Type,pool_encoded, Heating_encoded,Cooling_encoded,Parking_encoded,fireplace_encoded])
    # выводим статус запроса
    print('Status code: {}'.format(r.status_code))
    # реализуем обработку результата
    if r.status_code == 200:
        # если запрос выполнен успешно (код обработки=200),
        # выводим результат на экран
        print('Prediction: {}'.format(r.json()['prediction']))
    else:
        # если запрос завершён с кодом, отличным от 200,
        # выводим содержимое ответа
        print(r.text)