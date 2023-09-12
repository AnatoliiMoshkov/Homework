import logging
import ast
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler

TOKEN_BOT = "6694074415:AAEVjZgExAbUGLbGTBAVw6417iREQAK6B58"

file_data = open("data.txt", 'r')
data_from_file = file_data.read()
file_data.close()
if data_from_file == '':
    user_data = dict()
else:
    user_data = ast.literal_eval(data_from_file)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


class Expenses:
    def __init__(self, price: int):
        self.price = price


class Food(Expenses):
    def __init__(self, food: str, price: int):
        super().__init__(price)
        self.food = food

    def __str__(self):
        return f'{self.food} {self.price}$ | {datetime.now().strftime("%Y.%m.%W.%d")}'


class Oil(Expenses):
    def __init__(self, oil: str, price: int):
        super().__init__(price)
        self.oil = oil

    def __str__(self):
        return f'{self.oil} {self.price}$ | {datetime.now().strftime("%Y.%m.%W.%d")}'


class Clothes(Expenses):
    def __init__(self, clothes: str, price: int):
        super().__init__(price)
        self.clothes = clothes

    def __str__(self):
        return f'{self.clothes} {self.price}$ | {datetime.now().strftime("%Y.%m.%W.%d")}'


class Income:
    def __init__(self, category: str, price: int):
        self.category = category
        self.price = price

    def __str__(self):
        return f'{self.category} {self.price}$ | {datetime.now().strftime("%Y.%m.%W.%d")}'


class OpenFile:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


def sumcategory(category: list):
    summa = 0
    for x in category:
        if not isinstance(x, list):
            summa += x
        else:
            summa += sumcategory(x)
    return summa


async def start(update: Update, context: CallbackContext) -> None:
    logging.info('Command start was triggered!')
    user_id = update.message.from_user.id
    await update.message.reply_text(
        "Welcome to my TestAnatolii_telbot!\n"
        "Commands: \n"
        "▪️Adding expenses: /add_expenses <Category> <Price>\n"
        "▪️Adding incomes: /add_income <Category> <Price>\n"
        "▪️Remove expenses: /remove_expenses <Date format: year.month.day> <Category> <Price>\n"
        "▪️Remove income: /remove_income <Date format: year.month.day> <Category> <Price>\n"
        "▪️List of available categories of Expenses: /list_expenses\n"
        "▪️View Total Expenses for the specified period: /expenses_total <Period> <Number of Period>\n"
        "📅e.g: month 09\n"
        "▪️View Expenses for the specified period: /statistic_expenses <Period> <Number of Period>\n"
        "📅e.g: month 03 || only for day: day 2023.09.11\n"
        "▪️View Incomes for the specified period: /statistic_income <Period> <Number of Period>\n"
        "📅e.g: week 35 || only for day: day 2023.08.15\n"
        "▪️List tasks: /list\n"
    )


# додавання витрат
async def add_expenses(update: Update, context: CallbackContext) -> None:
    """
        Format of Expenses command
        /add_expenses Category Price
    """
    user_id = update.message.from_user.id
    exp_parts = " ".join(context.args).split(" ")
    exp_category = exp_parts[0].strip()
    price = int(exp_parts[1].strip())
    data_now_add = datetime.now().strftime("%Y.%m.%W.%d")

    if not user_data.get(user_id):
        user_data[user_id] = {data_now_add: {'expenses': {'food': [], 'oil': [], 'clothes': []},
                                             'income': {}
                                             }
                              }

    if exp_category == "Food" or exp_category == "food":
        exp = Food(exp_category, price)
        if not user_data[user_id].get(data_now_add):
            user_data[user_id].update({data_now_add: {'expenses': {'food': [], 'oil': [], 'clothes': []},
                                                      'income': {}
                                                      }
                                       })
            user_data[user_id][data_now_add]['expenses']['food'].append(price)
        else:
            user_data[user_id][data_now_add]['expenses']['food'].append(price)

        with OpenFile('data.txt', 'w+') as f:
            f.write(f'{user_data}')

        await update.message.reply_text(f"Expenses: {exp} was successfully added!")

    if exp_category == "Oil" or exp_category == "oil":
        exp = Food(exp_category, price)
        if not user_data[user_id].get(data_now_add):
            user_data[user_id].update({data_now_add: {'expenses': {'food': [], 'oil': [], 'clothes': []},
                                                      'income': {}
                                                      }
                                       })
            user_data[user_id][data_now_add]['expenses']['oil'].append(price)
        else:
            user_data[user_id][data_now_add]['expenses']['oil'].append(price)

        with OpenFile('data.txt', 'w+') as f:
            f.write(f'{user_data}')

        await update.message.reply_text(f"Expenses: {exp} was successfully added!")

    if exp_category == "Clothes" or exp_category == "clothes":
        exp = Food(exp_category, price)
        if not user_data[user_id].get(data_now_add):
            user_data[user_id].update({data_now_add: {'expenses': {'food': [], 'oil': [], 'clothes': []},
                                                      'income': {}
                                                      }
                                       })
            user_data[user_id][data_now_add]['expenses']['clothes'].append(price)
        else:
            user_data[user_id][data_now_add]['expenses']['clothes'].append(price)

        with OpenFile('data.txt', 'w+') as f:
            f.write(f'{user_data}')

        await update.message.reply_text(f"Expenses: {exp} was successfully added!")

    print(user_data[user_id])


# додавання доходів
async def add_income(update: Update, context: CallbackContext) -> None:
    """
        Format of Incomes command
        /add_expenses Category Price
    """
    user_id = update.message.from_user.id
    income_parts = " ".join(context.args).split(" ")
    income_category = income_parts[0].strip()
    price = int(income_parts[1].strip())
    data_now_add = datetime.now().strftime("%Y.%m.%W.%d")

    if not user_data.get(user_id):
        user_data[user_id] = {data_now_add: {'expenses': {'food': [], 'oil': [], 'clothes': []},
                                             'income': {}
                                             }
                              }

    if not user_data[user_id].get(data_now_add):
        user_data[user_id].update({data_now_add: {'expenses': {'food': [], 'oil': [], 'clothes': []},
                                                  'income': {}
                                                  }
                                   })

    income = Income(income_category, price)

    if user_data[user_id][data_now_add].get('income') == {}:
        user_data[user_id][data_now_add].update({'income': {income_category: [price]}})
    elif not user_data[user_id][data_now_add]['income'].get(income_category):
        user_data[user_id][data_now_add]['income'].update({income_category: [price]})
    else:
        user_data[user_id][data_now_add]['income'][income_category].append(price)

    with OpenFile('data.txt', 'w+') as f:
        f.write(f'{user_data[user_id]}')

    await update.message.reply_text(f"Expenses: {income} was successfully added!")
    print(user_data[user_id])
    print(user_data)


async def remove_expenses(update: Update, context: CallbackContext) -> None:
    """
        Format of Expenses command
        /remove_expenses year.month.day Category Price
    """
    user_id = update.message.from_user.id
    exp_parts = " ".join(context.args).split(" ")
    exp_category = exp_parts[1].strip()
    price = int(exp_parts[2].strip())

    string_date = exp_parts[0].strip()
    year, month, day = string_date.split('.')
    year = int(year)
    month = int(month)
    day = int(day)
    date_from_user = datetime(year, month, day).strftime("%Y.%m.%W.%d")

    if exp_category == "Food" or exp_category == "food":

        if date_from_user in user_data[user_id].keys():

            if price in user_data[user_id][date_from_user]['expenses'].get('food'):
                user_data[user_id][date_from_user]['expenses']['food'].remove(price)

                with OpenFile('data.txt', 'w+') as f:
                    f.write(f'{user_data}')

                await update.message.reply_text(
                    f"{date_from_user} Expenses: {exp_category} {price}$ was successfully removed!")
            else:
                await update.message.reply_text(
                    f"There is no such price for expenses OR an incorrect price was entered!")

        else:
            await update.message.reply_text(
                f"No expenses in this date: {date_from_user} OR an incorrect date!")

    if exp_category == "Oil" or exp_category == "oil":

        if date_from_user in user_data[user_id].keys():

            if price in user_data[user_id][date_from_user]['expenses'].get('oil'):
                user_data[user_id][date_from_user]['expenses']['oil'].remove(price)

                with OpenFile('data.txt', 'w+') as f:
                    f.write(f'{user_data}')

                await update.message.reply_text(
                    f"{date_from_user} Expenses: {exp_category} {price}$ was successfully removed!")
            else:
                await update.message.reply_text(
                    f"There is no such price for expenses OR an incorrect price was entered!")

        else:
            await update.message.reply_text(
                f"No expenses in this date: {date_from_user} OR an incorrect date!")

    if exp_category == "Clothes" or exp_category == "clothes":

        if date_from_user in user_data[user_id].keys():

            if price in user_data[user_id][date_from_user]['expenses'].get('clothes'):
                user_data[user_id][date_from_user]['expenses']['clothes'].remove(price)

                with OpenFile('data.txt', 'w+') as f:
                    f.write(f'{user_data}')

                await update.message.reply_text(
                    f"{date_from_user} Expenses: {exp_category} {price}$ was successfully removed!")
            else:
                await update.message.reply_text(
                    f"There is no such price for expenses OR an incorrect price was entered!")

        else:
            await update.message.reply_text(
                f"No expenses in this date: {date_from_user} OR an incorrect date!")


async def remove_income(update: Update, context: CallbackContext) -> None:
    """
        Format of Expenses command
        /remove_income Category Price
    """
    user_id = update.message.from_user.id
    income_parts = " ".join(context.args).split(" ")
    income_category = income_parts[1].strip()
    price = int(income_parts[2].strip())

    string_date = income_parts[0].strip()
    year, month, day = string_date.split('.')
    year = int(year)
    month = int(month)
    day = int(day)
    date_from_user = datetime(year, month, day).strftime("%Y.%m.%W.%d")

    if date_from_user in user_data[user_id].keys():

        if income_category in user_data[user_id][date_from_user]['income'].keys():

            if price in user_data[user_id][date_from_user]['income'].get(income_category):
                user_data[user_id][date_from_user]['income'][income_category].remove(price)

                if len(user_data[user_id][date_from_user]['income'].get(income_category)) == 0:
                    user_data[user_id][date_from_user]['income'].pop(income_category)

                with OpenFile('data.txt', 'w+') as f:
                    f.write(f'{user_data}')

                await update.message.reply_text(
                    f"{date_from_user} Incomes: {income_category} {price}$ was successfully removed!")
            else:
                await update.message.reply_text(
                    f"There is no such price of incomes OR an incorrect price was entered!")

        else:
            await update.message.reply_text(
                f"There is no category of incomes OR an incorrect category was entered!")

    else:
        await update.message.reply_text(
            f"There is no such price for expenses OR an incorrect price was entered!")


async def list_expenses(update: Update, context: CallbackContext) -> None:
    result = 'Categories:\n ✅Food\n ✅Oil\n ✅Clothes\n'
    await update.message.reply_text(result)


async def expenses_total(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_message = " ".join(context.args).split(" ")
    user_period = user_message[0]
    category_food = []
    category_oil = []
    category_clothes = []

    if user_period == 'all' or user_period == 'All':
        for date, balance in user_data[user_id].items():
            for exp_inc, category_exp in user_data[user_id][date].items():
                if exp_inc == 'expenses':
                    for category, value in user_data[user_id][date][exp_inc].items():
                        if category == 'food':
                            category_food.append(value)
                        if category == 'oil':
                            category_oil.append(value)
                        if category == 'clothes':
                            category_clothes.append(value)
        food_sum = sumcategory(category_food)
        oil_sum = sumcategory(category_oil)
        clothes_sum = sumcategory(category_clothes)
        all_sum = food_sum + oil_sum + clothes_sum
        await update.message.reply_text(f"All expenses💵: {all_sum}$")

    if user_period == 'Month' or user_period == 'month':
        for date, balance in user_data[user_id].items():
            month = date.split('.')
            user_date = user_message[1]
            if month[1] == user_date:
                for exp_inc, category_exp in user_data[user_id][date].items():
                    if exp_inc == 'expenses':
                        for category, value in user_data[user_id][date][exp_inc].items():
                            if category == 'food':
                                category_food.append(value)
                            if category == 'oil':
                                category_oil.append(value)
                            if category == 'clothes':
                                category_clothes.append(value)
        food_sum = sumcategory(category_food)
        oil_sum = sumcategory(category_oil)
        clothes_sum = sumcategory(category_clothes)
        all_sum = food_sum + oil_sum + clothes_sum
        await update.message.reply_text(f"Expenses per month💵: {all_sum}$")

    if user_period == 'week' or user_period == 'Week':
        for date, balance in user_data[user_id].items():
            week = date.split('.')
            user_date = user_message[1]
            if week[2] == user_date:
                for exp_inc, category_exp in user_data[user_id][date].items():
                    if exp_inc == 'expenses':
                        for category, value in user_data[user_id][date][exp_inc].items():
                            if category == 'food':
                                category_food.append(value)
                            if category == 'oil':
                                category_oil.append(value)
                            if category == 'clothes':
                                category_clothes.append(value)
        food_sum = sumcategory(category_food)
        oil_sum = sumcategory(category_oil)
        clothes_sum = sumcategory(category_clothes)
        all_sum = food_sum + oil_sum + clothes_sum
        await update.message.reply_text(f"Expenses per week💵: {all_sum}$")


async def statistic_expenses(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_message = " ".join(context.args).split(" ")
    user_period = user_message[0]
    category_food = []
    category_oil = []
    category_clothes = []

    if user_period == 'day' or user_period == 'Day':
        user_date = user_message[1]
        string_date = user_date.strip()
        year, month, day = string_date.split('.')
        year = int(year)
        month = int(month)
        day = int(day)
        date_from_user = datetime(year, month, day).strftime("%Y.%m.%W.%d")
        for date, balance in user_data[user_id].items():
            if date == date_from_user:
                for exp_inc, category_exp in user_data[user_id][date].items():
                    if exp_inc == 'expenses':
                        for category, value in user_data[user_id][date][exp_inc].items():
                            if category == 'food':
                                category_food.append(value)
                            if category == 'oil':
                                category_oil.append(value)
                            if category == 'clothes':
                                category_clothes.append(value)
        food_sum = sumcategory(category_food)
        oil_sum = sumcategory(category_oil)
        clothes_sum = sumcategory(category_clothes)
        await update.message.reply_text(
            f"Expenses per day💵:\n"
            f"Food🍽: {food_sum}$\n"
            f"Oil🚗: {oil_sum}$\n"
            f"Clothes👕: {clothes_sum}$")

    if user_period == 'week' or user_period == 'Week':
        for date, balance in user_data[user_id].items():
            week = date.split('.')
            user_date = user_message[1]
            if week[2] == user_date:
                for exp_inc, category_exp in user_data[user_id][date].items():
                    if exp_inc == 'expenses':
                        for category, value in user_data[user_id][date][exp_inc].items():
                            if category == 'food':
                                category_food.append(value)
                            if category == 'oil':
                                category_oil.append(value)
                            if category == 'clothes':
                                category_clothes.append(value)
        food_sum = sumcategory(category_food)
        oil_sum = sumcategory(category_oil)
        clothes_sum = sumcategory(category_clothes)
        await update.message.reply_text(
            f"Expenses per week💵:\n"
            f"Food🍽: {food_sum}$\n"
            f"Oil🚗: {oil_sum}$\n"
            f"Clothes👕: {clothes_sum}$")

    if user_period == 'Month' or user_period == 'month':
        for date, balance in user_data[user_id].items():
            month = date.split('.')
            user_date = user_message[1]
            if month[1] == user_date:
                for exp_inc, category_exp in user_data[user_id][date].items():
                    if exp_inc == 'expenses':
                        for category, value in user_data[user_id][date][exp_inc].items():
                            if category == 'food':
                                category_food.append(value)
                            if category == 'oil':
                                category_oil.append(value)
                            if category == 'clothes':
                                category_clothes.append(value)
        food_sum = sumcategory(category_food)
        oil_sum = sumcategory(category_oil)
        clothes_sum = sumcategory(category_clothes)
        await update.message.reply_text(
            f"Expenses per month💵:\n"
            f"Food🍽: {food_sum}$\n"
            f"Oil🚗: {oil_sum}$\n"
            f"Clothes👕: {clothes_sum}$")

    if user_period == 'Year' or user_period == 'year':
        for date, balance in user_data[user_id].items():
            year = date.split('.')
            user_date = user_message[1]
            if year[0] == user_date:
                for exp_inc, category_exp in user_data[user_id][date].items():
                    if exp_inc == 'expenses':
                        for category, value in user_data[user_id][date][exp_inc].items():
                            if category == 'food':
                                category_food.append(value)
                            if category == 'oil':
                                category_oil.append(value)
                            if category == 'clothes':
                                category_clothes.append(value)
        food_sum = sumcategory(category_food)
        oil_sum = sumcategory(category_oil)
        clothes_sum = sumcategory(category_clothes)
        await update.message.reply_text(
            f"Expenses per Year💵:\n"
            f"Food🍽: {food_sum}$\n"
            f"Oil🚗: {oil_sum}$\n"
            f"Clothes👕: {clothes_sum}$")


async def statistic_income(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_message = " ".join(context.args).split(" ")
    user_period = user_message[0]

    if user_period == 'day' or user_period == 'Day':
        user_date = user_message[1]
        string_date = user_date.strip()
        year, month, day = string_date.split('.')
        year = int(year)
        month = int(month)
        day = int(day)
        date_from_user = datetime(year, month, day).strftime("%Y.%m.%W.%d")
        income_dict = dict()
        for date, balance in user_data[user_id].items():
            if date == date_from_user:
                for exp_inc, category_income in user_data[user_id][date].items():
                    if exp_inc == 'income':
                        for key, value in user_data[user_id][date][exp_inc].items():
                            if key in income_dict.keys():
                                next_value = income_dict.get(key)
                                income_dict.update({key: next_value + value})
                            else:
                                income_dict[key] = value

        message = 'Incomes per day💵:\n'
        for key, value in income_dict.items():
            message += f"{key}: {sum(value)}$\n"
        await update.message.reply_text(message)

    if user_period == 'week' or user_period == 'Week':
        income_dict = dict()
        for date, balance in user_data[user_id].items():
            week = date.split('.')
            user_date = user_message[1]
            if week[2] == user_date:
                for exp_inc, category_income in user_data[user_id][date].items():
                    if exp_inc == 'income':
                        for key, value in user_data[user_id][date][exp_inc].items():
                            if key in income_dict.keys():
                                next_value = income_dict.get(key)
                                income_dict.update({key: next_value + value})
                            else:
                                income_dict[key] = value

        message = 'Incomes per week💵:\n'
        for key, value in income_dict.items():
            message += f"{key}: {sum(value)}$\n"
        await update.message.reply_text(message)

    if user_period == 'Month' or user_period == 'month':
        income_dict = dict()
        for date, balance in user_data[user_id].items():
            month = date.split('.')
            user_date = user_message[1]
            if month[1] == user_date:
                for exp_inc, category_income in user_data[user_id][date].items():
                    if exp_inc == 'income':
                        for key, value in user_data[user_id][date][exp_inc].items():
                            if key in income_dict.keys():
                                next_value = income_dict.get(key)
                                income_dict.update({key: next_value + value})
                            else:
                                income_dict[key] = value

        message = 'Incomes per month💵:\n'
        for key, value in income_dict.items():
            message += f"{key}: {sum(value)}$\n"
        await update.message.reply_text(message)

    if user_period == 'Year' or user_period == 'year':
        income_dict = dict()
        for date, balance in user_data[user_id].items():
            year = date.split('.')
            user_date = user_message[1]
            if year[0] == user_date:
                for exp_inc, category_income in user_data[user_id][date].items():
                    if exp_inc == 'income':
                        for key, value in user_data[user_id][date][exp_inc].items():
                            if key in income_dict.keys():
                                next_value = income_dict.get(key)
                                income_dict.update({key: next_value + value})
                            else:
                                income_dict[key] = value

        message = 'Incomes per year💵:\n'
        for key, value in income_dict.items():
            message += f"{key}: {sum(value)}$\n"
        await update.message.reply_text(message)


def run():
    app = ApplicationBuilder().token(TOKEN_BOT).build()
    logging.info('Application build successfully!')

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("add_expenses", add_expenses))
    app.add_handler(CommandHandler("add_income", add_income))
    app.add_handler(CommandHandler("remove_expenses", remove_expenses))
    app.add_handler(CommandHandler("remove_income", remove_income))
    app.add_handler(CommandHandler("list_expenses", list_expenses))
    app.add_handler(CommandHandler("expenses_total", expenses_total))
    app.add_handler(CommandHandler("statistic_expenses", statistic_expenses))
    app.add_handler(CommandHandler("statistic_income", statistic_income))

    app.run_polling()


if __name__ == "__main__":
    run()
