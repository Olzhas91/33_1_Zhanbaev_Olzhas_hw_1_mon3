CREATE_USER_TABLE_QUERY = '''
    CREATE TABLE IF NOT EXISTS telegram_users
    (ID INTEGER PRIMARY KEY,
    TELEGRAM_ID INTEGER,
    USERNAME CHAR(50),
    FIRST_NAME CHAR(50),
    LAST_NAME CHAR(50),
    UNIQUE(TELEGRAM_ID)
    )

'''

CREATE_BAN_USER_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS ban_users
        (ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        COUNT INTEGER,
        UNIQUE (TELEGRAM_ID)
        )
"""
CREATE_USER_FORM_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS user_form
    (ID INTEGER PRIMARY KEY,
    TELEGRAM_ID INTEGER,
    NICKNAME CHAR(50),
    BIO TEXT,
    AGE INTEGER,
    OCCUPATION TEXT,
    MARRIED CHAR(50),
    PHOTO TEXT,
    UNIQUE (TELEGRAM_ID)
    )
"""
CREATE_LIKE_USER_FORM_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS like_user_form
    (ID INTEGER PRIMARY KEY,
    LIKER_TELEGRAM_ID INTEGER,
    LIKED_TELEGRAM_ID INTEGER,
    UNIQUE (LIKER_TELEGRAM_ID, LIKED_TELEGRAM_ID)
    )
"""

CREATE_REFERRAL_SYSTEM_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS referral_system
    (ID INTEGER PRIMARY KEY,
    OWNER_TELEGRAM_ID INTEGER,
    REFFERRAL_TELEGRAM_ID INTEGER,
    UNIQUE (OWNER_TELEGRAM_ID, REFFERRAL_TELEGRAM_ID)
    )
"""


INSERT_USER_QUERY = """INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?)"""

INSERT_BAN_USER_QUERY = """INSERT OR IGNORE INTO ban_users VALUES (?,?,?)"""

SELECT_BAN_USER_QUERY = """
SELECT * FROM ban_users WHERE TELEGRAM_ID = ?
"""

UPDATE_BAN_USER_COUNT_QUERY = """
UPDATE ban_users SET COUNT = COUNT + 1 WHERE TELEGRAM_ID = ?
"""

INSERT_USER_FORM_QUERY = """INSERT OR IGNORE INTO user_form VALUES (?,?,?,?,?,?,?,?)"""
SELECT_USER_FORM_QUERY = """
SELECT * FROM user_form WHERE TELEGRAM_ID = ?
"""
INSERT_LIKE_QUERY = """INSERT INTO like_user_form VALUES (?,?,?)"""

UPDATE_USER_FORM_QUERY = """
UPDATE user_form SET NICKNAME = ?, BIO = ?, AGE = ?, OCCUPATION = ?, MARRIED = ?, PHOTO = ?  WHERE TELEGRAM_ID = ?
"""

UPDATE_USER_LINK_GENERATION_QUERY = """
UPDATE telegram_users SET REFERRAL_LINK = ? WHERE TELEGRAM_ID = ?
"""

INSERT_REFERRAL_USER_QUERY = """INSERT INTO referral_system VALUES (?,?,?)"""

SELECT_OWNER_BY_LINK_QUERY = """
SELECT TELEGRAM_ID FROM telegram_users WHERE REFERRAL_LINK = ?
"""

SELECT_LIST_REFERRAL_BY_OWNER_ID_QUERY = """
SELECT REFFERRAL_TELEGRAM_ID FROM referral_system WHERE OWNER_TELEGRAM_ID = ?
"""