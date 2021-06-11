import random
import peewee

database = 'oracle.db'


class BaseTable(peewee.Model):
    class Meta:
        database = peewee.SqliteDatabase(database)


class Oracle(BaseTable):
    oracle = peewee.CharField()


class SexFull(BaseTable):
    how_sex = peewee.CharField()
    where_sex = peewee.CharField()


class Alcohol(BaseTable):
    alcohol = peewee.CharField()


def do_oracle(query):
    if query == 'oracle':
        oracle = [oracle_.oracle for oracle_ in Oracle.select()]
        oracle_ = random.choice(oracle)
        return f'{oracle_}'
    elif query == 'sex_full':
        where = [oracle.where_sex for oracle in SexFull.select()]
        how = [oracle.how_sex for oracle in SexFull.select()]
        how_list = []
        for sex in how:
            if sex is not None:
                how_list.append(sex)
        where = random.choice(where)
        how = random.choice(how_list)
        return f'{how} {where}'
    elif query == 'sex_where':
        where_sex = [oracle.where_sex for oracle in SexFull.select()]
        where_sex = random.choice(where_sex)
        return f'{where_sex}'
    elif query == 'sex_how':
        how_sex = [oracle.how_sex for oracle in SexFull.select()]
        how_list = []
        for sex in how_sex:
            if sex is not None:
                how_list.append(sex)
        how_sex = random.choice(how_list)
        return f'{how_sex}'
    elif query == 'alcohol_choice':
        drink = [drink.alcohol for drink in Alcohol.select()]
        drink = random.choice(drink)
        return f'{drink}'
