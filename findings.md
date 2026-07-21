# Log de Descobertas e Referências - Steel Master

## Benchmarks e Referências de UX
- CRM Pipedrive/Agendor: Pipeline visual Kanban onde o vendedor enxerga a conversão por estágios com metas claras.

## Pesquisas Tecnológicas e Limitações
- Foi inicialmente testado o NocoDB para entregar a visão Tabela/Kanban, porém o usuário sentiu falta de recursos maduros de venda.
- **Descoberta do Twenty CRM:** Migramos do NocoDB para o Twenty CRM. O Twenty exige modelagem relacional rigorosa (Company vs Opportunity) mas entrega uma UX infinitamente superior.
- **MCP e Metadados:** Foi descoberto que o Twenty expõe um servidor MCP na porta `/mcp`, que permite a IAs efetuarem CRUD maciço de contatos (DATABASE_CRUD). No entanto, o sistema proíbe modificação do Schema/Metadados via MCP para evitar corrupção, exigindo configuração manual dos campos.