import hashlib
import json
from pathlib import Path
import requests
from bs4 import BeautifulSoup

encod = 'utf-8'


def writing(dir_name, file_name, file, extension='json'):
    print(f'Начало работы функции "writing". Параметры: file_name "{file_name}.{extension}"')
    if extension == 'json':
        try:
            with open(Path(f'{dir_name}', f'{file_name}.{extension}'), 'w', encoding=encod) as f:
                json.dump(file, f, indent=4, ensure_ascii=False)
            print('function', 'DONE',
                  f'Файл {file_name}.{extension} сохранен в папке {dir_name}', 'writing')
        except Exception as e:
            print(f'{e}')
    else:
        try:
            with open(Path(f'{dir_name}', f'{file_name}.{extension}'), 'w', encoding=encod) as f:
                f.write(str(file))
            print(f'Файл {file_name}.{extension} сохранен в папке {dir_name}')
        except Exception as e:
            print(f'{e}')


def auth(login, password, server_data):
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest()
    url = (f'{server_data["protocol"]}://{server_data["server"]}:{server_data["port"]}'
           f'/resto/api/auth?login={login}&pass={sha1pass}')
    print('Отправлен запрос на получение token')
    print(f'URL: {url}')
    try:
        token = requests.get(url)
        print(f'Получен token {token.text}')
    except Exception as e:
        token = None
        print(f'{e}')
    return token


def logout(token, server_data):
    url = f'{server_data["protocol"]}://{server_data["server"]}:{server_data["port"]}/resto/api/logout?key={token.text}'
    print('Отправлен запрос на закрытие token')
    print(f'URL: {url}')
    try:
        result = requests.get(url)
        print(f'Выход из token {token.text}')
    except Exception as e:
        result = None
        print(f'{e}')
    return result.text


def save_data(token, server_data, data_type='None'):
    base_url = f'{server_data["protocol"]}://{server_data["server"]}:{server_data["port"]}/resto/api/'
    if data_type == 'Products' or data_type == 'Stocks':
        if data_type == 'Products':
            url = f'{base_url}products?key={token.text}'
        elif data_type == 'Stocks':
            url = f'{base_url}corporation/stores?key={token.text}'
        else:
            url = None
        print(f'Адрес запроса: {url}')
        try:
            response = requests.get(url)
        except Exception as e:
            response = None
            print(f'{e}')
        soup = BeautifulSoup(response.content, 'xml')
        print('Ответ получен, формирование списка из xml-ответа')
        if data_type == 'Products':
            res = []
            for productDto in soup.find_all('productDto'):
                try:
                    id = productDto.find('id').string
                except AttributeError:
                    id = 'None'
                try:
                    parentId = productDto.find('parentId').string
                except AttributeError:
                    parentId = 'None'
                try:
                    num = productDto.find('num').string
                except AttributeError:
                    num = 'None'
                try:
                    code = productDto.find('code').string
                except AttributeError:
                    code = 'None'
                try:
                    name = productDto.find('name').string
                except AttributeError:
                    name = 'None'
                try:
                    productType = productDto.find('productType').string
                except AttributeError:
                    productType = 'None'
                try:
                    cookingPlaceType = productDto.find('cookingPlaceType').string
                except AttributeError:
                    cookingPlaceType = 'None'
                try:
                    mainUnit = productDto.find('mainUnit').string
                except AttributeError:
                    mainUnit = 'None'
                try:
                    productCategory = productDto.find('productCategory').string
                except AttributeError:
                    productCategory = 'None'
                eta = {
                    "id": id,
                    "parentId": parentId,
                    "num": num,
                    "code": code,
                    "name": name,
                    "productType": productType,
                    "cookingPlaceType": cookingPlaceType,
                    "mainUnit": mainUnit,
                    "productCategory": productCategory
                }
                res.append(eta)
        elif data_type == 'Stocks':
            res = []
            for corporateItemDto in soup.find_all('corporateItemDto'):
                store = {
                    "id": corporateItemDto.find('id').string,
                    "parentId": corporateItemDto.find('parentId').string,
                    "code": corporateItemDto.find('code').string,
                    "name": corporateItemDto.find('name').string,
                    "type": corporateItemDto.find('type').string
                }
                res.append(store)
        else:
            res = None
    # elif data_type == 'Assembled':
    #     check_id = id_list.copy()
    #     res = []
    #     for i in check_id:
    #         name = find('name', i, "Products")
    #         logwrite('function', 'INFO', f'Отправляю запрос на получение {name}', 'save_data')
    #         url = (f'{base_url}v2/assemblyCharts/getAssembled?date={server_data["date_for_ttk"]}'
    #                f'&productId={i}&key={token.text}')
    #         logwrite('requests', 'INFO', f'Адрес запроса:\n{url}', 'save_data')
    #         try:
    #             result = requests.get(url).json()["assemblyCharts"][0]
    #             logwrite('requests', 'DONE', f'Ответ:\n{result}', 'save_data')
    #         except Exception as e:
    #             result = None
    #             logwrite('requests', 'ERRO', f'{e}', 'save_data')
    #         # items = [j["productId"] for j in result["items"]]
    #         if data_type == 'Assembled':
    #             try:
    #                 assembled = {
    #                     "id": i,
    #                     "name": name,
    #                     "items": [j["productId"] for j in result["items"]]
    #                 }
    #                 logwrite('function', 'DONE', f'Позиция {name} добавлена', 'save_data')
    #                 res.append(assembled)
    #             except Exception as e:
    #                 logwrite('function', 'ERRO',
    #                          f'При обработке {name} возникла ошибка:\n{tab}{e}', 'save_data')
    #
    # elif data_type == 'Need':
    #     logwrite('function', 'INFO',
    #              'Сбор позиций из папок, заданных в config.json запущен', 'save_data')
    #     dirs = [find('id', i, "Products") for i in list_dirs_name]
    #     dishes = []
    #     products = reading('data', 'Products')
    #     for product in products:
    #         for id in dirs:
    #             if product['parentId'] == id:
    #                 if product['productType'] == 'None':
    #                     dirs.append(product['id'])
    #                 else:
    #                     dishes.append(product['id'])
    #     for product in products:
    #         for id in dirs:
    #             if product['parentId'] == id:
    #                 if product["id"] not in dishes:
    #                     dishes.append(product['id'])
    #     res = []
    #     for product in products:
    #         for one in dishes:
    #             if product['id'] == one and product['productType'] != 'None':
    #                 res.append(product)
    else:
        print(f'Отправляю запрос на получение {data_type}')
        url = f'{base_url}v2/entities/list?key={token.text}&rootType={data_type}'
        print(f'Адрес запроса:\n{url}')
        try:
            result = requests.get(url).json()
        except Exception as e:
            result = None
            print(f'{e}')
        res = result
        # for item in result:
        #     res.append({"id": item['id'], "name": item['name']})
    writing('data', f'{data_type}', res)
    return res
