# Convenience targets. Run `make help` for the list.
.PHONY: help test run serve draft docker-build docker-run

help:
	@echo "make test         - run the test suite (no install needed)"
	@echo "make draft        - generate a draft package from the sample project"
	@echo "make serve        - start the HTTP engine on :8000"
	@echo "make docker-build - build the Docker image"
	@echo "make docker-run   - run the engine in Docker on :8000"

test:
	python3 -m unittest discover -s tests -v

draft:
	python3 -m app.cli examples/sample_project.json

serve:
	python3 -m app.server

docker-build:
	docker build -t payapp-engine:latest .

docker-run:
	docker run --rm -p 8000:8000 payapp-engine:latest
