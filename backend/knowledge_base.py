SKILL_BENCHMARKS = [
    {
        "id": "backend_mid",
        "text": """
Role: Backend Engineer
Level: Mid (2-4 years experience)
Expected Technical Skills: REST API design, relational databases (SQL), basic caching, unit testing, Git workflows, one backend framework (e.g. Express, Django, Spring)
Expected Soft Skills: clear code reviews, following existing architecture decisions, asking clarifying questions before implementation
Key Responsibilities at This Level: owns individual features end-to-end with some guidance, writes maintainable code, participates in code reviews
Typical Next Step: Senior Backend Engineer
What Distinguishes This Level from One Below: works with less hand-holding, can debug production issues independently, understands tradeoffs of basic design decisions
""",
    },
    {
        "id": "backend_senior",
        "text": """
Role: Backend Engineer
Level: Senior (5-8 years experience)
Expected Technical Skills: distributed systems design, database optimization and indexing strategy, API design at scale, caching strategies (Redis, CDN), message queues, observability and monitoring, security fundamentals
Expected Soft Skills: mentoring junior engineers, cross-team technical communication, writing design documents, owning incident response
Key Responsibilities at This Level: owns system-level decisions, designs solutions for ambiguous problems, reviews architecture proposals from others
Typical Next Step: Staff Engineer (IC track) or Engineering Manager (management track)
What Distinguishes This Level from One Below: works on ambiguous problems with minimal guidance, considers long-term maintainability and scale, influences technical direction beyond own tasks
""",
    },
    {
        "id": "backend_staff",
        "text": """
Role: Backend Engineer
Level: Staff (8+ years experience)
Expected Technical Skills: large-scale system architecture, cross-service design tradeoffs, capacity planning, deep expertise in at least one specialized domain (e.g. databases, infra, security)
Expected Soft Skills: influencing technical strategy across multiple teams, mentoring senior engineers, driving org-wide technical initiatives without direct authority
Key Responsibilities at This Level: sets technical direction for a whole domain or product area, resolves cross-team architectural conflicts
Typical Next Step: Principal Engineer or Engineering Director
What Distinguishes This Level from One Below: impact spans multiple teams, not just one system; sought out for the hardest technical problems in the org
""",
    },
    {
        "id": "frontend_mid",
        "text": """
Role: Frontend Engineer
Level: Mid (2-4 years experience)
Expected Technical Skills: React or equivalent framework, component design, state management (Redux/Context), responsive design, basic accessibility, REST/GraphQL API integration
Expected Soft Skills: collaborating with designers, giving/receiving code review feedback
Key Responsibilities at This Level: builds full features from design mockups with moderate guidance, writes reusable components
Typical Next Step: Senior Frontend Engineer
What Distinguishes This Level from One Below: can independently break down a design into components, handles edge cases and error states without being told to
""",
    },
    {
        "id": "frontend_senior",
        "text": """
Role: Frontend Engineer
Level: Senior (5-8 years experience)
Expected Technical Skills: performance optimization (bundle size, rendering), design systems and component libraries, complex state management architecture, accessibility (WCAG), testing strategy (unit/e2e)
Expected Soft Skills: mentoring, driving frontend architecture decisions, partnering closely with product/design leadership
Key Responsibilities at This Level: owns frontend architecture for a product area, sets patterns other engineers follow
Typical Next Step: Staff Frontend Engineer or Engineering Manager
What Distinguishes This Level from One Below: thinks beyond a single feature to the overall frontend architecture and long-term maintainability
""",
    },
    {
        "id": "fullstack_mid",
        "text": """
Role: Full-Stack Engineer
Level: Mid (2-4 years experience)
Expected Technical Skills: comfortable across one frontend framework and one backend framework, basic database design, deployment basics (CI/CD, Docker)
Expected Soft Skills: context-switching between frontend/backend concerns, communicating tradeoffs to non-technical stakeholders
Key Responsibilities at This Level: ships complete features across the stack with moderate oversight
Typical Next Step: Senior Full-Stack Engineer
What Distinguishes This Level from One Below: can independently decide where logic belongs (frontend vs backend) for a given feature
""",
    },
    {
        "id": "fullstack_senior",
        "text": """
Role: Full-Stack Engineer
Level: Senior (5-8 years experience)
Expected Technical Skills: system design across the full stack, infrastructure decisions (hosting, scaling), security across both frontend and backend, mentoring on both ends of the stack
Expected Soft Skills: driving end-to-end technical decisions, balancing speed vs correctness for a whole product area
Key Responsibilities at This Level: owns entire products or major product areas end-to-end, often in smaller/startup-style teams
Typical Next Step: Staff Engineer, Engineering Manager, or founding-engineer type roles
What Distinguishes This Level from One Below: comfortable owning ambiguous, cross-cutting problems without a dedicated specialist team
""",
    },
    {
        "id": "data_ml_mid",
        "text": """
Role: Data/ML Engineer
Level: Mid (2-4 years experience)
Expected Technical Skills: Python data tooling (pandas, numpy), SQL, basic ML model training and evaluation, data pipeline basics (Airflow or equivalent)
Expected Soft Skills: communicating model results to non-technical stakeholders, documenting data assumptions
Key Responsibilities at This Level: builds and maintains data pipelines, trains models under senior guidance
Typical Next Step: Senior Data/ML Engineer
What Distinguishes This Level from One Below: can independently debug data quality issues and understands basic model evaluation tradeoffs
""",
    },
    {
        "id": "data_ml_senior",
        "text": """
Role: Data/ML Engineer
Level: Senior (5-8 years experience)
Expected Technical Skills: ML system design (training + serving at scale), feature engineering strategy, model monitoring and drift detection, MLOps practices, deep understanding of tradeoffs between model types
Expected Soft Skills: mentoring, translating business problems into ML problems, driving experimentation culture
Key Responsibilities at This Level: owns ML systems end-to-end including production reliability, not just model accuracy
Typical Next Step: Staff ML Engineer or ML Engineering Manager
What Distinguishes This Level from One Below: thinks about production reliability and business impact, not just model performance in isolation
""",
    },
    {
        "id": "devops_mid",
        "text": """
Role: DevOps/SRE Engineer
Level: Mid (2-4 years experience)
Expected Technical Skills: CI/CD pipelines, Docker, basic Kubernetes, cloud fundamentals (AWS/GCP/Azure), monitoring/alerting setup, scripting (Bash/Python)
Expected Soft Skills: clear incident communication, documenting runbooks
Key Responsibilities at This Level: maintains existing infrastructure, handles routine incidents with escalation support
Typical Next Step: Senior DevOps/SRE Engineer
What Distinguishes This Level from One Below: can independently triage and resolve most production incidents without escalating
""",
    },
    {
        "id": "devops_senior",
        "text": """
Role: DevOps/SRE Engineer
Level: Senior (5-8 years experience)
Expected Technical Skills: infrastructure-as-code (Terraform), advanced Kubernetes, capacity planning, cost optimization, security hardening, designing for high availability and disaster recovery
Expected Soft Skills: driving reliability culture across engineering teams, mentoring, leading incident postmortems
Key Responsibilities at This Level: designs infrastructure strategy, sets SLOs/SLIs, owns org-wide reliability initiatives
Typical Next Step: Staff SRE or Infrastructure Engineering Manager
What Distinguishes This Level from One Below: thinks in terms of system-wide reliability and cost, not just keeping individual services up
""",
    },
    {
        "id": "engineering_manager",
        "text": """
Role: Engineering Manager
Level: Transition from Senior IC
Expected Technical Skills: enough hands-on depth to review architecture and unblock teams, though less day-to-day coding
Expected Soft Skills: performance management, hiring and interviewing, project prioritization, conflict resolution, career coaching for reports
Key Responsibilities at This Level: owns team output and health, translates business goals into technical roadmaps, manages up and across
Typical Next Step: Senior Engineering Manager or Director of Engineering
What Distinguishes This Level from IC Track: success is measured by team output and growth, not personal code output
""",
    },
    {
        "id": "product_engineer",
        "text": """
Role: Product Engineer
Level: Mid-Senior (generalist, startup-style)
Expected Technical Skills: broad full-stack competence, fast prototyping ability, comfort with ambiguous or shifting requirements, basic product sense
Expected Soft Skills: direct collaboration with founders/product leads, making pragmatic tradeoffs under time pressure
Key Responsibilities at This Level: ships end-to-end product features fast, often owning both technical and some product decisions
Typical Next Step: Senior Product Engineer, Founding Engineer, or specialize into a track (Frontend/Backend/Full-stack Senior)
What Distinguishes This Role: values speed and product judgment as much as deep technical specialization
""",
    },
    {
        "id": "qa_test_engineer",
        "text": """
Role: QA/Test Engineer
Level: Mid-Senior
Expected Technical Skills: test automation frameworks (Selenium, Playwright, Cypress), API testing, CI/CD test integration, basic scripting, performance/load testing basics
Expected Soft Skills: clear bug reporting, collaborating with developers on root cause analysis, advocating for quality culture
Key Responsibilities at This Level: designs test strategy for a product area, builds and maintains automated test suites, not just manual testing
Typical Next Step: QA Lead, SDET (Software Development Engineer in Test) specialization, or transition into general Backend/Full-stack roles
What Distinguishes This Level: owns test strategy and automation architecture, not just executing test cases
""",
    },
]