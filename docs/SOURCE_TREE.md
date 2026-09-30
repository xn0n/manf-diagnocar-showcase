# Дерево приватной реализации

Полный список отслеживаемых файлов приватного репозитория `manf-diagnocar` на момент подготовки витрины, 1 октября 2026 года. Дерево построено по фактическому Git-индексу; оно содержит только названия путей. Содержимое исходников, конфигурации и тестов здесь не публикуется.

Публичный репозиторий `manf-diagnocar-showcase` содержит документацию и самостоятельный пример. Файлы в дереве ниже относятся к приватной реализации, а не к составу витрины. Рабочие данные, адреса сервисов и закрытые подробности не разглашаются.

Количество файлов: **60**.

```text
manf-diagnocar/
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   │   └── orchestrator.py
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── auth.py
│   │   │       ├── cases.py
│   │   │       ├── conclusions.py
│   │   │       ├── datasets.py
│   │   │       ├── health.py
│   │   │       ├── knowledge.py
│   │   │       ├── models.py
│   │   │       ├── router.py
│   │   │       └── runs.py
│   │   ├── catalogs/
│   │   │   └── loader.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── errors.py
│   │   ├── db/
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   └── session.py
│   │   ├── providers/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── demo_provider.py
│   │   │   ├── llm_provider.py
│   │   │   └── openmodel_provider.py
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── case.py
│   │   │   ├── common.py
│   │   │   ├── conclusion.py
│   │   │   ├── dataset.py
│   │   │   ├── knowledge.py
│   │   │   └── run.py
│   │   ├── services/
│   │   │   ├── case_service.py
│   │   │   ├── conclusion_service.py
│   │   │   ├── dataset_service.py
│   │   │   ├── knowledge_service.py
│   │   │   └── run_service.py
│   │   ├── __init__.py
│   │   └── main.py
│   ├── evaluation/
│   │   ├── compare_baseline.py
│   │   ├── run_benchmark.py
│   │   └── run_robustness.py
│   ├── scripts/
│   │   ├── generate_extended_cases.py
│   │   ├── lock_hashes.py
│   │   ├── run_isolated.py
│   │   └── smoke_toyota_p0171.py
│   ├── tests/
│   │   ├── test_api.py
│   │   ├── test_model_router.py
│   │   └── test_supervisor_regressions.py
│   ├── openapi.json
│   ├── README.md
│   ├── requirements.txt
│   └── run_diagnosis.py
├── data/
│   └── README.md
├── evaluation_suite/
│   └── README.md
├── infra/
│   └── .gitkeep
├── src/
│   └── .gitkeep
├── tests/
│   └── .gitkeep
├── .env.example
├── .gitignore
├── dashboard.html
├── docker-compose.yml
├── Dockerfile
└── README.md
```

В приватной очищенной копии `data/README.md` и `evaluation_suite/README.md` обозначают отсутствие официальных данных и материалов оценок. Имена этих директорий не означают, что закрытые наборы включены в репозиторий.

[Описание проекта](../README.md) · [Архитектура](ARCHITECTURE.md)
