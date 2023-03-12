# Ansible Playbook for Bonsai

## Structure
### inventory/
Sample inventory definitions

### roles/
#### bonsai-exporter
Deploys a bonsai exporter to a host

#### bonsai-stack
Deploys the complete bonsai stack to a host

## Deployment
`ansible-playbook -i inventory/hosts.yml -b install.yml --ask-vault-pass`
