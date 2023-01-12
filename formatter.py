import xlsxwriter
import aiofiles
from aiocsv import AsyncWriter
from fpdf import FPDF


async def save_csv(data, title):
    async with aiofiles.open(f"{title}.csv", "w", newline="", encoding="utf-8") as file:
        writer = AsyncWriter(file)
        await writer.writerow(["title", "description", "price", "photo", "main_photo"])
        await writer.writerows(data)
    print(f"We used async def save_csv")
    print(f"Data was saved to file {title}.csv")


def save_pdf(data: list, title: str):
    pdf = FPDF(format="A4")
    pdf.add_font("DejaVu", "", "font/DejaVuSansCondensed.ttf", True)
    pdf.set_font("DejaVu", size=10)
    count_4 = 0
    n = 0
    for data_block in data:
        if count_4 == 4:
            count_4 = 0
            n = 0
        count_4 += 1
        if count_4 == 1:
            pdf.add_page()
        pdf.text(11, 15 + n, f"title : {data_block[0]}")
        pdf.text(11, 20 + n, f"price : {data_block[2]}zl")
        pdf.set_y(25 + n)
        pdf.multi_cell(70, 5, f"descriptions : {data_block[1]}")
        pdf.image(data_block[3], x=85, y=10 + n, h=50)
        if len(data_block) == 5:
            pdf.image(data_block[4], x=140, y=10 + n, h=50)
        n += 70
    print(f"We used def save_pdf")
    print(f"Data was saved to file {title}.pdf")
    pdf.output(f"{title}.pdf")


def save_xlsx(data, title):
    workbook = xlsxwriter.Workbook(f"{title}.xlsx")
    worksheet = workbook.add_worksheet("Sheet1")
    header = ["title", "description", "price", "photo", "main_photo"]

    for i, entry in enumerate(header):
        worksheet.write(0, i, entry)
    for index, entry in enumerate(data):
        for i in range(5):
            worksheet.write(index + 1, i, entry[i])
    workbook.close()
    print(f"We used def save_xlsx")
    print(f"Data was saved to file {title}.xlsx")


FORMATTER_DICT = {
    "csv": save_csv,
    "pdf": save_pdf,
    "xlsx": save_xlsx,
}


def formatter_manu(FORMATTER_DICT):
    formatter_menu_list = [(index, formatter) for index, formatter in enumerate(FORMATTER_DICT.keys(), start=1)]
    return formatter_menu_list
