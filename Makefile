PROJECT_ID = handsome-493022
REGION     = us-east4
IMAGE      = $(REGION)-docker.pkg.dev/$(PROJECT_ID)/handsome/app:latest
GCS_BUCKET = gs://handsome-static

deploy:
	gcloud builds submit --tag $(IMAGE) --project $(PROJECT_ID) .
	gcloud run deploy handsome \
		--image $(IMAGE) \
		--region $(REGION) \
		--project $(PROJECT_ID) \
		--allow-unauthenticated

run:
	docker build -t handsome-local .
	docker run --rm -p 8080:8080 \
		-e GCS_BASE_URL=https://storage.googleapis.com/handsome-static/static \
		handsome-local

upload-static:
	gsutil -m cp -r static/ $(GCS_BUCKET)/

.PHONY: deploy run upload-static
