from fpdf import FPDF, XPos, YPos


class Formatter:
    def __init__(self, data, title="my_deposit"):
        self.data = data
        self.title = title

    def save_pdf(self):
        pdf = FPDF(format="A4")
        pdf.add_font("DejaVu", "", "font/DejaVuSansCondensed.ttf")
        pdf.set_font("DejaVu", size=10)
        pdf.add_page()
        months = len(self.data) - 1
        for month, value in self.data.items():
            res_text = ""
            if month == 0:
                header = f"Розрахунок депозиту на {months} місяці(в)\n\n"
                pdf.multi_cell(w=0, h=5, txt=header, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            else:
                res_text += f"{month} місяць\n"
            res_text += f'На рахунку {value.get("cash_in_wallet")}₴\n'
            if value.get("get_cash_from_deposit", False):
                res_text += f'    +  Обміняли депозитні $ на суму: {value.get("get_cash_from_deposit")}₴\n'
            if value.get("take_cash_to_deposit", False):
                res_text += f'    --  Витрати коштів на депозит: {value.get("take_cash_to_deposit")}₴\n'
            res_text += f'На депозитному рахунку {value.get("USD_on_deposit")}$\n'
            if value.get("USD_on_deposit_this_month", False):
                res_text += f'    + Купили $ на депозит в цьому місяці: {value.get("USD_on_deposit_this_month")}₴\n'
            if value.get("detail", False):
                res_text += "Деталі:\n"
                for det in value["detail"]:
                    res_text += "   " + det + "\n"
            pdf.multi_cell(w=0, h=5, txt=res_text, align="J", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        result = f'Результат:\nПри вкладенні {"%.2f" % self.data[0]["cash_in_wallet"]}₴ через {len(self.data) - 1} місяці(в) ваш прибуток становитиме {"%.2f" % (self.data[months]["cash_in_wallet"] - self.data[0]["cash_in_wallet"])}₴'
        pdf.multi_cell(w=0, h=5, txt=result, align="J", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        print(f"Data was saved to file {self.title}.pdf")
        pdf.output(f"{self.title}.pdf")
