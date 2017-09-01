all: delete create

delete:
	helm delete --purge pji-grupo1
	kubectl delete -f PersistentVolumeClaim.yaml
	kubectl delete -f PersistentVolume.yaml

create:
	kubectl create -f PersistentVolume.yaml
	kubectl create -f PersistentVolumeClaim.yaml
	helm install --name pji-grupo1 --namespace ensino -f values.yaml stable/mariadb
