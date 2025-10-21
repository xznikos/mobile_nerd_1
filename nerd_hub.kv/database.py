# database.py
import sqlite3
import os
import hashlib

DB_PATH = os.path.join("banco", "produtos.db")

# --------------------------------------------------------
# Funções básicas
# --------------------------------------------------------
def conectar():
    os.makedirs("banco", exist_ok=True)
    return sqlite3.connect(DB_PATH)

def criar_tabelas():
    conn = conectar()
    cur = conn.cursor()

    # Tabela de produtos
    cur.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        descricao TEXT,
        imagem TEXT
    )
    """)

    # Tabela de usuários
    cur.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        senha_hash TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

# --------------------------------------------------------
# Usuários
# --------------------------------------------------------
def hash_senha(senha_plain):
    return hashlib.sha256(senha_plain.encode("utf-8")).hexdigest()

def cadastrar_usuario(nome, email, senha_plain):
    conn = conectar()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO usuarios (nome, email, senha_hash) VALUES (?, ?, ?)",
                    (nome, email, hash_senha(senha_plain)))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verificar_login(email, senha_plain):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT id, nome, email FROM usuarios WHERE email = ? AND senha_hash = ?",
                (email, hash_senha(senha_plain)))
    usuario = cur.fetchone()
    conn.close()
    return usuario

# --------------------------------------------------------
# Produtos
# --------------------------------------------------------
def adicionar_produto(nome, preco, descricao, imagem):
    conn = conectar()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO produtos (nome, preco, descricao, imagem) VALUES (?, ?, ?, ?)",
        (nome, preco, descricao, imagem)
    )
    conn.commit()
    conn.close()

def listar_produtos():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT id, nome, preco, descricao, imagem FROM produtos")
    produtos = cur.fetchall()
    conn.close()
    return produtos
