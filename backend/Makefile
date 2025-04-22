# Makefile for managing backend (FastAPI + LangChain) service

install:
	poetry install

run:
	poetry run uvicorn main:app --reload

shell:
	poetry shell

init-db:
	curl http://127.0.0.1:8000/init

ask:
	curl -X POST http://127.0.0.1:8000/ask \
	-H "Content-Type: application/json" \
	-d '{"question": "What is in the sample doc?"}'

start: install run