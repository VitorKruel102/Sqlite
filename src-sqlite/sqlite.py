import sqlite3

def create_db():
    """
    Utilizado para criação do bando de dados.
    """
    conn = sqlite3.connect('teste.db')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_db()

