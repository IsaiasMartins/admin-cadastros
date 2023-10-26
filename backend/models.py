def select_users():

    select = f""" SELECT * FROM pessoas """

    return select

def insert_user(nome, rg, cpf, data_nascimento, data_admissao, funcao):
    if funcao is None:
        insert = f"""INSERT INTO pessoas
            (nome, rg, cpf, data_nascimento, data_admissao)
            VALUES('{nome}', '{rg}', '{cpf}', '{data_nascimento}', '{data_admissao}');"""
    else:
        insert = f"""INSERT INTO pessoas
            (nome, rg, cpf, data_nascimento, data_admissao, funcao)
            VALUES('{nome}', '{rg}', '{cpf}', '{data_nascimento}', '{data_admissao}', '{funcao}');"""
    
    return insert

def update_user(id_pessoa, nome, rg, cpf, data_nascimento, data_admissao, funcao):
    if funcao is None:
        update = f"""UPDATE pessoas
            SET nome='{nome}', rg='{rg}', cpf='{cpf}', data_nascimento='{data_nascimento}', data_admissao='{data_admissao}', funcao=NULL
            WHERE id_pessoa={id_pessoa};"""
    else:
        update = f"""UPDATE pessoas
            SET nome='{nome}', rg='{rg}', cpf='{cpf}', data_nascimento='{data_admissao}', data_admissao='{data_admissao}', funcao='{funcao}'
            WHERE id_pessoa={id_pessoa};"""
    
    return update

def delete_user(id_pessoa):

    delete = f""" DELETE FROM pessoas
    WHERE id_pessoa={id_pessoa}; """

    return delete