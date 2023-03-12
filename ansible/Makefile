install:
	ansible-galaxy install -r requirements.yml

deploy:
	ansible-playbook -i inventory/hosts.yml -b install.yml
	
dev:
	ansible-playbook -i inventory/hosts.yml -b dev.yml

monitoring:
	ansible-playbook -i inventory/hosts.yml -b monitoring.yml

bonsai:
	ansible-playbook -i inventory/hosts.yml -b bonsai.yml