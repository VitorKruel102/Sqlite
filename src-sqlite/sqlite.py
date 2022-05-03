import sqlite3 as sql


def create_db():
    """
    Utilizado para criação do bando de dados.
    """
    conn = sql.connect('teste.db')
    conn.commit()
    conn.close()


def create_table():
    """
    Utilizado para criação da tabela no banco.
    """
    conn = sql.connect('teste.db')
    cursor = conn.cursor()
    cursor.execute(
        """ CREATE TABLE tickes(
            ticker TEXT,
            Data INTEGER,
            Abertura REAL,
            Maxima REAL,
            Minima REAL,
            Fechamento REAL
        )"""
    )
    conn.commit()
    conn.close()


def insertRows():
    """
    Utilizado para adicionar dados na tabela no banco.
    """
    conn = sql.connect('teste.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tickes VALUES(?, ?, ?, ?, ?, ?)",
                   ('WDONAFUT', 20220502, 5.650, 5.660, 5.5650, 5.490)
                   )
    conn.commit()
    conn.close()


def readRows():
    """
    Utilizado para ler dados na tabela no banco.
    """
    conn = sql.connect('teste.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tickes ")
    date = cursor.fetchall()
    conn.commit()
    conn.close()

    print(date)


def readOrdered():
    """
    Utilizado para ordenar dados na tabela no banco.
    """
    conn = sql.connect('teste.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tickes ORDER BY Data DESC")
    date = cursor.fetchall()
    conn.commit()
    conn.close()

    print(date)


def search():
    """
    Utilizado para selecionar dados especificos na tabela no banco.
    """
    conn = sql.connect('teste.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tickes WHERE Data > 20220505")
    date = cursor.fetchall()
    conn.commit()
    conn.close()

    print(date)


def UpdateFields():
    """
    Utilizado para atualizar dados especificos na tabela no banco.
    """
    conn = sql.connect('teste.db')
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tickes SET Data=20220304 WHERE ticker like 'WDONAFUT'")
    conn.commit()
    conn.close()


def DeleteRows():
    """
    Utilizado para deletar linhas na tabela no banco.
    """
    conn = sql.connect('teste.db')
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM tickes WHERE Data=20220505")
    conn.commit()
    conn.close()


if __name__ == '__main__':
    UpdateFields()
