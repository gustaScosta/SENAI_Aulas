import streamlit as st
import sqlite3
import pandas as pd



conn = sqlite3.connect('Aula 18 - Pacotes e Frameworks/tarefas.db', check_same_thread=False)
c = conn.cursor()

c.execute('''
        CREATE TABLE IF NOT EXISTS tarefas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'pendente'
          
    )
''')
conn.commit()

st.title('GERENCIADOR DE TAREFAS')
st.subheader('streamlit + sqlite3')

st.markdown('+++ NOVA TAREFA')
nova_tarefa = st.text_input('o que você precisa fazer? ')

if st.button('add tarefa'):
    if nova_tarefa == '':
        st.warning('digite algo...')
    else:
        c.execute('INSERT INTO tarefas (nome, status) Values(?,?)',(nova_tarefa, 'pendente'))
        conn.commit()
        st.success('tarefa adicionada com sucesso')

st.write('---')
st.markdown('SUAS TAREFAS')
c.execute('SELECT id, nome, status from tarefas')

dados = c.fetchall()

if dados:
    df = pd.DataFrame(dados, columns=['ID','tarefas','status'])
    st.dataframe(df, use_container_width=True, hide_index=True)
    col1, col2 = st.columns(2)

    with col1:
        tarefa_selecionada = st.selectbox('escolha pelo id', df['ID'])
    with col2:
        acao = st.radio('ação',['concluir', 'excluir'])
    
    if st.button('confirmar...'):
        if acao == 'concluir':
            c.execute("UPDATE tarefas SET status = 'concluida' where id=? ",(tarefa_selecionada,))
            st.success('tarefa concluida')
        elif acao == 'EXCLUIR':
            c.execute("UPDATE tarefas SET status = 'excluida' where id=? ",(tarefa_selecionada,))
            st.success('tarefa excluida')
        conn.commit()
        st.rerun()
else:
    st.info('digite algo')