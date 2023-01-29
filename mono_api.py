import datetime
from pprint import pprint
from time import sleep

from monobank import Client
import requests

from formatter import Formatter


class MonoBank(Client):
    def __init__(self, token="token"):
        super().__init__(token)
        self.name = "MonoBank"
        self.money_UAH = 0
        self.money_USD = 0
        self.__data_carrency = None

    def purchase_USD_for_cards(self):
        if self.__data_carrency == None or (self.__data_carrency["time"] - datetime.datetime.now()).seconds <= 300:
            print("We used API")
            data = self.get_currency()[0]
            self.__data_carrency = {"time": datetime.datetime.now(), "data": data}
            return "%.5f" % data["rateSell"]
        else:
            return "%.5f" % self.__data_carrency["data"]["rateSell"]

    def sell_USD_for_cards(self):
        if self.__data_carrency == None or (self.__data_carrency["time"] - datetime.datetime.now()).seconds <= 300:
            print("We used API")
            data = self.get_currency()[0]
            self.__data_carrency = {"time": datetime.datetime.now(), "data": data}
            return "%.5f" % data["rateBuy"]
        else:
            return "%.5f" % self.__data_carrency["data"]["rateBuy"]

    def exchange_rate(self):
        return (
            f"{self.name}\n курс долара\n"
            f"  для карток:\n    продаж {self.sell_USD_for_cards()}\n"
            f"    купівля {self.purchase_USD_for_cards()}\n"
        )


class PrivatBank:
    def __init__(self):
        self.name = "PrivatBank"
        self.money_UAH = 0
        self.money_USD = 0

    def purchase_USD_for_cards(self):
        data = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11")
        return data.json()[1]["sale"]

    def sell_USD_for_cards(self):
        data = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11")
        return data.json()[1]["buy"]

    def purchase_USD_in_the_branch(self):
        data = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
        return data.json()[1]["sale"]

    def sale_USD_in_the_branch(self):
        data = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
        return data.json()[1]["buy"]

    def exchange_rate(self):
        return (
            f"{self.name} курс долара\n"
            f"  для карток:\n    продаж {self.sell_USD_for_cards()}\n"
            f"    купівля {self.purchase_USD_for_cards()}\n"
            f" у відділені:\n    продаж {self.sale_USD_in_the_branch()}\n"
            f"    купівля {self.purchase_USD_in_the_branch()}\n"
        )

    def details(self):
        return (
            "Кладеш нал на Універсальну картку привату через термінал гривні (0% комісія).\n"
            "Відкриваєш валютний депозит в доларах на суму не більше еквіваленнту 100000грн на 3 місяці.\n"
            "Після 60 днів заходиш через додаток і нажимаєш не продовжувати автоматично депозит. \n"
            "За два дні до закінчення терміну валютного депозиту вибираєш отримати нал, вибираєш відділення,\n"
            "приходиш забираєш або варік валюту покласти на доларову картку для виплат.\n"
            "наступний депозит можна відкривати через місяць з дати відкриття попереднього."
        )


my_privat = PrivatBank()
my_mono = MonoBank()


class Wallet:
    def __init__(self, owner="Anonim", money_UAH=0, money_USD=0):
        self.owner = owner
        self.money_UAH = money_UAH
        self.money_USD = money_USD
        self.time = 0

    def manager_money(self, money, month):
        calendar = {}
        for current_month in range(month + 1):
            if current_month == 0:
                calendar[current_month] = {"cash_in_wallet": money}
            else:
                money = calendar[current_month - 1]["cash_in_wallet"] - calendar[current_month - 1].get(
                    "take_cash_to_deposit", 0
                )
                calendar[current_month] = {
                    "cash_in_wallet": money,
                    "USD_on_deposit": calendar[current_month - 1]["USD_on_deposit"],
                }

            if (
                calendar.get(current_month - 3) != None
                and calendar[current_month - 3].get("take_cash_to_deposit", 0) > 0
            ):
                my_uah, detail_purchase_UAH = self.purchase_UAH(
                    calendar[current_month - 3]["USD_on_deposit_this_month"]
                )
                calendar[current_month]["USD_on_deposit"] -= calendar[current_month - 3]["USD_on_deposit_this_month"]
                if calendar[current_month].get("detail") == None:
                    calendar[current_month]["detail"] = [detail_purchase_UAH]
                else:
                    calendar[current_month]["detail"].append(detail_purchase_UAH)
                calendar[current_month]["get_cash_from_deposit"] = my_uah
                calendar[current_month]["cash_in_wallet"] += my_uah

            if current_month <= month - 3:
                if 0 < calendar[current_month]["cash_in_wallet"]:
                    if calendar[current_month]["cash_in_wallet"] < 100000:
                        calendar[current_month]["take_cash_to_deposit"] = calendar[current_month]["cash_in_wallet"]
                    else:
                        calendar[current_month]["take_cash_to_deposit"] = 100000
                    my_usd, detail_purchase_USD = self.purchase_USD(calendar[current_month]["take_cash_to_deposit"])
                    if calendar[current_month].get("detail") == None:
                        calendar[current_month]["detail"] = [detail_purchase_USD]
                    else:
                        calendar[current_month]["detail"].append(detail_purchase_USD)
                    calendar[current_month]["USD_on_deposit_this_month"] = my_usd
                    calendar[current_month]["USD_on_deposit"] = (
                        calendar[current_month].get("USD_on_deposit", 0) + my_usd
                    )
        return calendar

    def purchase_USD(self, UAH=None, bank=my_privat):
        if UAH == None:
            UAH = self.money_UAH
        if self.money_UAH >= UAH:
            self.money_UAH -= UAH
            exchange_rates = float(bank.purchase_USD_for_cards())
            USD = round(UAH / exchange_rates, 2)
            self.money_USD += USD
            detail = "Ви обміняли в {} {:.2f}₴ на {:.2f}$ по курсу {:.2f}".format(bank.name, UAH, USD, exchange_rates)
            return USD, detail

    def purchase_UAH(self, USD=None, bank=my_privat):
        if USD == None:
            USD = self.money_USD
        if self.money_USD >= USD:
            self.money_USD -= USD
            exchange_rates = float(bank.sale_USD_in_the_branch())
            UAH = round(USD * float(exchange_rates), 2)
            self.money_UAH += UAH
            self.time += 3
            detail = "Ви обміняли в {} {:.2f}$ на {:.2f}₴ по курсу {:.2f}".format(bank.name, USD, UAH, exchange_rates)
            return UAH, detail

    def status(self):
        print("{} у вашому гаманці:\n{:.2f}₴ та {:.2f}$".format(self.owner, self.money_UAH, self.money_USD))


my_wallet = Wallet("Artur_Yastrebov", 1000000000000000, 1000000000000)
