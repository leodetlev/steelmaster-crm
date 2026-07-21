# Plano de Tarefas (Automação RPA / IA) — Steel Master

## 🗺️ Roadmap de Módulos (Fases)

### Fase 0 — Discovery
- [x] **1. Reunião de Kickoff** | Responsável: Gestor | Tipo: Checkbox
- [x] **2. Levantamento de requisitos com o cliente** | Responsável: Gestor | Tipo: Checkbox
- [x] **3. Mapear processo AS-IS: quem faz, frequência, tempo** | Responsável: Dev | Tipo: Checkbox
- [ ] **4. Identificar sistemas envolvidos (ERP, planilhas, portais)** | Responsável: Dev | Tipo: Texto longo -> *Armazenar em docs/inputs/0-discovery/*
- [ ] **5. Levantar volume de transações por mês** | Responsável: Gestor | Tipo: Checkbox
- [x] **6. Identificar exceções e variações do processo** | Responsável: Dev | Tipo: Checkbox
- [ ] **7. Calcular ROI estimado (horas economizadas × custo hora)** | Responsável: Comercial | Tipo: Checkbox
- [ ] **8. Validar acesso técnico aos sistemas do cliente** | Responsável: Dev | Tipo: Texto longo -> *Verificar docs/inputs/3-credenciais/*

### Fase 1 — Proposta
- [x] **1. Definir escopo: o que faz e o que NÃO faz** | Responsável: Gestor | Tipo: Checkbox
- [x] **2. Estimar horas com buffer de 20%** | Responsável: Dev | Tipo: Checkbox
- [ ] **3. Redigir proposta (escopo, prazo, preço, SLA, exclusões)** | Responsável: Comercial | Tipo: Checkbox
- [ ] **4. Enviar proposta e agendar alinhamento** | Responsável: Comercial | Tipo: Checkbox
- [ ] **5. Contrato de prestação de serviço assinado** | Responsável: Comercial | Tipo: Upload -> *Verificar docs/inputs/1-proposta/*
- [ ] **6. NDA assinado (quando aplicável)** | Responsável: Comercial | Tipo: Upload -> *Verificar docs/inputs/1-proposta/*

### Fase 2 — Design (PDD)
- [x] **1. Criar PDD (Process Design Document) — fluxo detalhado** | Responsável: Dev | Tipo: Upload -> *Salvar em docs/inputs/2-design_pdd/*
- [x] **2. Mapear cada passo: input, ação, output, condição de erro** | Responsável: Dev | Tipo: Checkbox
- [x] **3. Definir regras de negócio e exceções tratadas** | Responsável: Dev | Tipo: Checkbox
- [ ] **4. Documentar credenciais e acessos necessários** | Responsável: Dev | Tipo: Texto longo (cofre de senhas)
- [x] **5. Dicionário de dados simplificado** | Responsável: Dev | Tipo: Upload -> *Salvar em docs/inputs/2-design_pdd/*
- [x] **6. Estruturação do banco (Postgres/NocoDB)** | Responsável: Dev | Tipo: Texto longo (link + credenciais)
- [ ] **7. PDD aprovado pelo cliente** | Responsável: Gestor | Tipo: Upload -> *Verificar docs/inputs/2-design_pdd/*
- [ ] **8. Critérios de aceite definidos** | Responsável: Gestor | Tipo: Checkbox

### Fase 3 — Desenvolvimento
- [x] **1. Setup inicial Docker/Infra** | Responsável: Dev | Tipo: Texto longo (link do ambiente)
- [x] **2. Construção do fluxo principal (happy path)** | Responsável: Dev | Tipo: Checkbox
- [x] **3. Construção da lógica no n8n** | Responsável: Dev | Tipo: Checkbox
- [ ] **4. Criação de prompts para IA (quando aplicável)** | Responsável: Dev | Tipo: Texto longo
- [ ] **5. Implementar tratamento de erros e exceções** | Responsável: Dev | Tipo: Checkbox
- [ ] **6. Configurar logs de execução e alertas de falha** | Responsável: Dev | Tipo: Checkbox
- [ ] **7. Versionamento no GitHub (branch do projeto)** | Responsável: Dev | Tipo: Link (URL do repo)
- [ ] **8. Status report semanal ao cliente** | Responsável: Gestor | Tipo: Checkbox

### Fase 4 — Testes (UAT)
- [ ] **1. Executar testes unitários em cada etapa do fluxo** | Responsável: Dev | Tipo: Checkbox
- [ ] **2. Testar cenários de exceção mapeados no PDD** | Responsável: Dev | Tipo: Checkbox
- [ ] **3. Teste de volume com dados reais do cliente** | Responsável: Dev | Tipo: Checkbox
- [ ] **4. Execução da matriz de testes** | Responsável: Dev | Tipo: Upload (relatório) -> *Salvar em docs/inputs/4-testes/*
- [ ] **5. Ajuste de fallbacks e loops** | Responsável: Dev | Tipo: Checkbox
- [ ] **6. Relatório de performance (tempo, taxa de erro)** | Responsável: Dev | Tipo: Texto longo
- [ ] **7. Conduzir sessão de UAT com usuário-chave do cliente** | Responsável: Gestor | Tipo: Checkbox
- [ ] **8. Documentar bugs encontrados e correções aplicadas** | Responsável: Dev | Tipo: Texto longo
- [ ] **9. Termo de aceite assinado pelo cliente** | Responsável: Gestor | Tipo: Upload -> *Verificar docs/inputs/4-testes/*

### Fase 5 — Deploy & Handover
- [ ] **1. Migrar bot para ambiente de produção (Coolify)** | Responsável: Dev | Tipo: Checkbox
- [ ] **2. Configurar agendamento (scheduler)** | Responsável: Dev | Tipo: Checkbox
- [ ] **3. Dashboard de monitoramento ativo** | Responsável: Dev | Tipo: Link
- [ ] **4. Manual de operação (POP) finalizado** | Responsável: Dev | Tipo: Upload
- [ ] **5. Configuração de handoff humano** | Responsável: Dev | Tipo: Checkbox
- [ ] **6. Treinar usuário responsável no cliente** | Responsável: Gestor | Tipo: Checkbox
- [ ] **7. Definir canal de suporte pós-entrega** | Responsável: Gestor | Tipo: Checkbox
- [ ] **8. Agendar check-in de 30 dias** | Responsável: CS / Gestor | Tipo: Checkbox