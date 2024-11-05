# /k8s/makefile
DOCKER_IMAGE = your_dockerhub_username/fastapi-app:latest
K8S_MANIFEST = fast-k8s.yml

.PHONY: build push deploy clean

build:
	docker build -t $(DOCKER_IMAGE) -f ../Dockerfile .

push: build
	docker push $(DOCKER_IMAGE)

deploy: push
	kubectl apply -f $(K8S_MANIFEST)

clean:
	kubectl delete -f $(K8S_MANIFEST)
