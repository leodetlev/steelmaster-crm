# Constituição do Produto — Steel Master

## 🏗️ Invariantes Arquiteturais
- **Stack:** Twenty CRM (Front) + Supabase/Postgres (Database) + n8n (Backend/Automação)
- **Arquitetura:** P.D.S. em Containers. Testado estritamente de forma local no Docker (porta 4433 e 8585) e posteriormente deployado via Coolify.
- **Padrões de Código:** Fluxos JSON do n8n auto-contidos consumindo GraphQL e Webhooks do Twenty.

## 👥 Permissões e Regras de Acesso (RLS)
- O Twenty CRM gerencia suas próprias permissões e roles internamente. O banco Supabase em produção não deve expor tabelas diretamente ao público sem chaves de API.

## 📊 Modelo de Dados (Database Schema)
- **Data Model:** Paradigma Relacional.
- **Companies:** Armazena CNPJ, Nome, Ramo de Atividade (Custom Select).
- **People:** Contatos com os quais os robôs se comunicarão.
- **Opportunities:** Painel Kanban gerencial com os 4 estágios da operação.

## 🧠 Regras de Negócio Críticas
- **Funil de 4 Fases:** 1. Contato | 2. Envio de Proposta | 3. Follow Up | 4. Fechamento.
- **Ocultação de Valor:** O campo valor financeiro só é cobrado nas etapas secundárias da negociação.
- **A Geladeira (Adormecimento):** Leads marcados para contato futuro saem do Kanban de vista. O n8n é o responsável exclusivo por acordar leads no dia exato e voltar a oportunidade para a fase de "Contato".
- **Gatilho de Venda:** A alteração do card para a fase "Fechamento" dispara e-mail automatizado para a separação dos tubos na fábrica.