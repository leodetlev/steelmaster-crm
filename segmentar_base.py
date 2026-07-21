import pandas as pd
import os

print("Lendo a base de dados...")
df = pd.read_excel('base_steel.xlsx', sheet_name='Base_Prospeccao')

colunas_candidatas = ['Ramo de Atividade', 'Categoria Cliente', 'Categoria Específica']
melhor_coluna = colunas_candidatas[0]
menos_nulos = len(df)

print("Analisando preenchimento das colunas...")
for col in colunas_candidatas:
    if col in df.columns:
        nulos = df[col].isna().sum()
        print(f" - {col}: {nulos} vazios de {len(df)}")
        if nulos < menos_nulos:
            menos_nulos = nulos
            melhor_coluna = col

print(f"\nColuna escolhida para segmentação: {melhor_coluna}")

output_dir = "output_segmentacao"
os.makedirs(output_dir, exist_ok=True)

# Limpeza e preenchimento de nulos
df[melhor_coluna] = df[melhor_coluna].fillna('Indefinido')
df['nicho_clean'] = df[melhor_coluna].astype(str).str.strip()
df['nicho_clean'] = df['nicho_clean'].str.replace('/', '_').str.replace(r'[^\w\s-]', '', regex=True)

grupos = df.groupby('nicho_clean')
resumo = []

for nome, grupo in grupos:
    if not nome or str(nome).lower() == 'nan':
        nome = "Sem_Nicho"
    
    # Nome seguro para arquivo
    nome_arquivo = f"{nome[:50]}.xlsx"
    caminho = os.path.join(output_dir, nome_arquivo)
    
    # Exportar apenas as empresas daquele nicho
    grupo.drop(columns=['nicho_clean']).to_excel(caminho, index=False)
    resumo.append({'Nicho': nome, 'Quantidade': len(grupo)})

df_resumo = pd.DataFrame(resumo).sort_values(by='Quantidade', ascending=False)
df_resumo.to_excel(os.path.join(output_dir, '_Resumo_Volumetria.xlsx'), index=False)

print("\n--- Volumetria (Top 10 Nichos) ---")
print(df_resumo.head(10).to_string(index=False))
print(f"\nSegmentação concluída! Foram geradas {len(grupos)} planilhas na pasta '{output_dir}'.")
