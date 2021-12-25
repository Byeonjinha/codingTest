from abc import *
 
class DeliveryStore(metaclass=ABCMeta):
    @abstractmethod
    def set_order_list(self, order_list):
        pass
    
    @abstractmethod
    def get_total_price(self):
        pass
    
class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# class PizzaStore@@@: 2021/12/25  피자스토어 -> 딜리버리 스토어 상속
class PizzaStore(DeliveryStore):
    def __init__(self):
        menu_names = ["Cheese", "Potato", "Shrimp", "Pineapple", "Meatball"]
        menu_prices = [11100, 12600, 13300, 21000, 19500];
        self.menu_list = []
        for i in range(5):
            self.menu_list.append(Food(menu_names[i], menu_prices[i]))
        
        self.order_list = []
    
    # def @@@: ->  order_list에 하나씩 꺼내서 order_list에 추가해주는 역할은 set_order_list
    def set_order_list(self, order_list):
        for order in order_list:
            self.order_list.append(order)

    # def @@@:  -> total_price 반환하는 역할 get_total_price
    def get_total_price(self):
        total_price = 0
        for order in self.order_list:
            for menu in self.menu_list:
                if order == menu.name:
                    total_price += menu.price
        return total_price 
            
def solution(order_list):
    delivery_store = PizzaStore()
    
    delivery_store.set_order_list(order_list)
    total_price = delivery_store.get_total_price()
    return total_price

#The following is code to output testcase.
order_list = ["Cheese", "Pineapple", "Meatball"]
ret = solution(order_list)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")