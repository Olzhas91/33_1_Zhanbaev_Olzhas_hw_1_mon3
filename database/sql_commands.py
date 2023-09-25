import sqlite3
from database import sql_quer


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()

    def sql_create_tables(self):
        if self.connection:
            print('Database connected successfully')

        self.connection.execute(sql_quer.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_quer.CREATE_BAN_USER_TABLE_QUERY)
        self.connection.execute(sql_quer.CREATE_USER_FORM_TABLE_QUERY)
        self.connection.execute(sql_quer.CREATE_LIKE_USER_FORM_TABLE_QUERY)
        self.connection.execute(sql_quer.CREATE_REFERRAL_SYSTEM_TABLE_QUERY)

    def sql_insert_user_command(self, telegram_id, username, first_name, last_name):
        self.cursor.execute(
            sql_quer.INSERT_USER_QUERY,
            (None, telegram_id, username, first_name, last_name,)
        )

        self.connection.commit()

    def sql_insert_ban_user_command(self, telegram_id):
        self.cursor.execute(
            sql_quer.INSERT_BAN_USER_QUERY,
            (None, telegram_id, 1,)
        )
        self.connection.commit()

    def sql_select_ban_user_command(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'count': row[2],
        }
        return self.cursor.execute(
            sql_quer.SELECT_BAN_USER_QUERY,
            (telegram_id,)
        ).fetchall()

    def sql_update_ban_user_count_command(self, telegram_id):
        self.cursor.execute(
            sql_quer.UPDATE_BAN_USER_COUNT_QUERY,
            (telegram_id,)
        )

    def sql_insert_user_form_command(self, telegram_id, nickname, bio,
                                     age, occupation, married, photo):
        self.cursor.execute(
            sql_quer.INSERT_USER_FORM_QUERY,
            (None, telegram_id, nickname, bio, age, occupation, married, photo,)
        )
        self.connection.commit()

    def sql_select_user_form_command(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "bio": row[3],
            "age": row[4],
            "occupation": row[5],
            "married": row[6],
            "photo": row[7],
        }
        return self.cursor.execute(
            sql_quer.SELECT_USER_FORM_QUERY,
            (telegram_id,)
        ).fetchall()
    def sql_insert_like_command(self, liker, liked):
        self.cursor.execute(
            sql_quer.INSERT_LIKE_QUERY,
            (None, liker, liked,)
        )
        self.connection.commit()

        def sql_insert_reference_user_command(self, owner, referral):
            self.cursor.execute(
                sql_quer.INSERT_REFERRAL_USER_QUERY,
                (None, owner, referral,)
            )
            self.connection.commit()

        def sql_select_owner_by_link_command(self, link):
            self.cursor.row_factory = lambda cursor, row: {
                'telegram_id': row[0],
            }
            return self.cursor.execute(
                sql_quer.SELECT_OWNER_BY_LINK_QUERY,
                (link,)
            ).fetchall()

        def sql_select_list_referral_by_owner_id_command(self, owner):
            self.cursor.row_factory = lambda cursor, row: {
                'referral_id': row[0],
            }
            return self.cursor.execute(
                sql_quer.SELECT_LIST_REFERRAL_BY_OWNER_ID_QUERY,
                (owner,)
            ).fetchall()