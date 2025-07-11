**Projeto: FinBank Flow**

---

### ✨ CONTEXTO
O "FinBank Flow" é uma plataforma de análise e simulação de operações bancárias cotidianas (daily banking), que busca integrar boas práticas de desenvolvimento com DevOps, monitoramento de produtividade, BI, e visualização de dados em tempo real. O projeto está sendo construído com foco didático e prático, permitindo a exploração de conceitos como lead time, pipeline CI/CD, ETL, banco de dados relacional e dashboards.

---

### 🔗 JUSTIFICATIVA
Com o crescimento do setor financeiro digital e o aumento da demanda por experiências bancárias mais eficientes e visíveis, a necessidade de monitorar o desempenho das operações e a jornada dos clientes se torna estratégica. Este projeto visa ser uma base de aprendizado para ferramentas modernas e workflows aplicados em fintechs reais, promovendo o desenvolvimento de soluções modulares, escaláveis e monitoráveis.

---

### 🌟 OBJETIVOS
**Objetivo Geral:**
Construir uma aplicação fullstack simulada de uma fintech, com backend em Flask, frontend em React, banco PostgreSQL via Docker, monitoramento de produtividade, e BI com QuickSight ou alternativa equivalente.

**Objetivos Específicos:**
- Simular operações bancárias comuns (Pix, depósito, saque, pagamento).
- Capturar e registrar tempo de execução (lead time) de cada transação.
- Construir um backend desacoplado e modular com Flask e SQLAlchemy.
- Criar um frontend responsivo com React e React Router.
- Armazenar logs e transações para posterior ETL.
- Construir dashboards interativos via QuickSight ou Metabase.

---

### ✅ PREMISSAS
- O projeto funcionará localmente e em nuvem.
- Serão utilizadas ferramentas modernas e de uso gratuito sempre que possível.
- A estrutura será modular e pronta para deploy em ambientes produtivos (Docker, CI/CD).
- O armazenamento de dados será feito em PostgreSQL.
- O banco estará preparado para operações CRUD e queries analíticas.

---

### ❌ RESTRIÇÕES
- O uso do Amazon QuickSight está condicionado à ativação de uma conta AWS em agosto.
- Limitações orçamentárias impedem integração com APIs bancárias reais.

---

### 💼 STAKEHOLDERS
- **Desenvolvedor (Hugo)**: Principal executor e idealizador.
- **Mentores / Instrutores**: Suporte técnico e didático (caso envolvido em curso).
- **Usuário Simulado (cliente do banco)**: Representa o beneficiado pelas operações.
- **Entidades educacionais**: Caso o projeto seja parte de avaliação acadêmica ou estudo.

---

### 🧩 DETALHAMENTO TÉCNICO DAS ETAPAS

#### 🔧 1. Backend - API Flask + PostgreSQL
- Estrutura com Blueprints e SQLAlchemy.
- Banco PostgreSQL rodando via Docker.
- Rotas: `/login`, `/cadastro`, `/saldo`, `/deposito`, `/saque`, `/pix`, `/historico`
- Integração de JWT para login seguro.
- Middleware para validação de token nas rotas protegidas.

#### 🌐 2. Frontend - React + React Router
- Telas: Login, Cadastro, Home, Depósito, Saque, Pix, Histórico.
- Roteamento com React Router DOM.
- Consumo da API com `axios`.
- Armazenamento de token JWT no `localStorage`.
- Estilização modular ou com TailwindCSS.

#### 🧪 3. Scripts Python auxiliares
- **ETL**: coleta registros de logs e transações, exporta para CSV e move para um bucket local ou AWS S3.
- **Simulador de eventos**: executa interações automáticas simuladas (cadastro, transação, erro) e registra o tempo.

#### 📊 4. Métricas e Log
- Registro de `lead time` de cada endpoint (tempo entre entrada e resposta).
- Salvamento em tabela `logs` com status e timestamp.
- Dados serão base para os dashboards.

#### 📈 5. Dashboards e BI
- No frontend: KPIs principais e gráficos (ex: saldo total, número de transações, sucesso/falha).
- No Metabase: dashboards detalhados (lead time médio, jornada de cliente, % sucesso).
- Posteriormente: migração para Amazon QuickSight com dados de S3 ou RDS.

---



