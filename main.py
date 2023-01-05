from entity.courier import Courier
from entity.exceptions import BaseError
from entity.request import Request
from entity.shop import Shop
from entity.store import Store


shop = Shop(
    items={
        'печенька': 3,
        'ноутбук': 3,
    }
)

store = Store(
    items={
        'печенька': 10,
        'ноутбук': 20,
    }
)

storages = {
    'магазин': shop,
    'склад': store,
}


def main():
    while True:
        # TODO: Вывести содержимое складов.
        for storage_name in storages:
            print(f'В {storage_name} хранится: {storages[storage_name].get_items()}')

        # TODO: Запросить у пользователя строку.

        user_input = input(
            'Введите строку в формате "Доставить 3 печенька из склад в магазин".\n'
            'Введите "stop" или "стоп", чтобы продолжить:\n',
        )

        if user_input in ('stop', 'стоп'):
            break

        # TODO: Обработать строку, проверить на ошибки, определить товар, количество, точки отправления и назначения.
        try:
            request = Request(request_str=user_input, storages=storages)

            # TODO: Доставить товар.
            courier = Courier(request=request, storages=storages)
            courier.move()
        except BaseError as error:
            print(error.message)



if __name__ == '__main__':
    main()

