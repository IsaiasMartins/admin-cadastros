import connect
import models

def exec_list_users():
    con = connect.connect_mysql_dev()
    cursor = con.cursor()
    select = models.select_users()

    cursor.execute(select)

    row = cursor.fetchone()
    if not row:
        con.commit()
        con.close()
        return {'usersCount': 0}
    
    array = []
    while row:
        DIC = {
            'id_pessoa':int(row[0]),
            'nome':str(row[1]),
            'rg':str(row[2]),
            'cpf':str(row[3]),
            'data_nascimento':str(row[4]),
            'data_admissao':str(row[5]),
            'funcao':str(row[6]),
        }
        array.append(DIC)
        row = cursor.fetchone()

    con.commit()
    con.close()

    return {'usersCount': len(array), 'users': array}

def exec_create_user(nome, rg, cpf, data_nascimento, data_admissao, funcao):
    if not nome or not rg or not cpf or not data_nascimento or not data_admissao:
        return {"create": False, "message": "Campos obrigatórios não podem estar vazios."}
    
    if not funcao:
        funcao = None

    con = connect.connect_mysql_dev()
    cursor = con.cursor()
    insert = models.insert_user(nome, rg, cpf, data_nascimento, data_admissao, funcao)
    
    try:
        cursor.execute(insert)
        con.commit()
        con.close()
        return {"create": True, "message": "Criação bem-sucedida."}
    except Exception as e:
        con.rollback()
        con.close()
        return {"create": False, "message": f"Erro durante a criação: {str(e)}"}
    
def exec_edit_user(id_pessoa,nome,rg,cpf,data_nascimento,data_admissao,funcao):
    if not nome or not rg or not cpf or not data_nascimento or not data_admissao:
        return {"create": False, "message": "Campos obrigatórios não podem estar vazios."}
    
    if not funcao:
        funcao = None

    con = connect.connect_mysql_dev()
    cursor = con.cursor()
    update = models.update_user(id_pessoa,nome,rg,cpf,data_nascimento,data_admissao,funcao)
    
    try:
        cursor.execute(update)
        con.commit()
        con.close()
        return {"update": True, "message":"Atualização bem-sucedida."}
    except Exception as e:
        con.rollback()
        con.close()
        return {"update": True, "message":"Erro durante a atualização"}
    
def exec_delete_user(id_pessoa):
    con = connect.connect_mysql_dev()
    cursor = con.cursor()
    delete = models.delete_user(id_pessoa)
    
    try:
        cursor.execute(delete)
        con.commit()
        con.close()
        return {"delete": True, "message":"Exclusão bem-sucedida."}
    except Exception as e:
        con.rollback()
        con.close()
        return {"delete": True, "message":"Erro durante a exclusão"}