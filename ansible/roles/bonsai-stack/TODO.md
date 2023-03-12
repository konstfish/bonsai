## fortigate-exporter
prometheus_fortigate:
build: ./fortigate_exporter
ports:
    - 9710:9710
volumes:
    - ./fortigate_exporter/fortigate-key.yaml:/opt/fortigate-key.yaml
restart: unless-stopped

## proxmox
prometheus_proxmox:
image: prompve/prometheus-pve-exporter
ports:
    - 9221:9221
volumes:
    - ./pve.yml:/etc/pve.yml

## pihole
  prometheus_pihole:
    image: ekofr/pihole-exporter:latest
    ports:
      - 9617:9617
    environment:
       - PIHOLE_HOSTNAME=10.0.1.2
       - PIHOLE_PASSWORD=Piho.4664
       - INTERVAL=120s
       - PORT=9617
    restart: unless-stopped

## speedtest (unnötig tbh)
  prometheus_speedtest:
    image: jraviles/prometheus_speedtest:latest
    ports:
      - 9516:9516/tcp
    restart: unless-stopped

### old prometheus config
global:
  scrape_interval: 10m
  scrape_timeout: 3m

scrape_configs:
- job_name: 'speedtest'
  metrics_path: /probe
  static_configs:
  - targets:
    - prometheus_speedtest:9516
- job_name: 'pihole'
  scrape_interval: 2m
  scrape_timeout: 1m
  static_configs:
    - targets: ['prometheus_pihole:9617']
- job_name: 'fortigate_exporter'
  metrics_path: /probe
  scrape_interval: 45s
  scrape_timeout: 30s
  static_configs:
    - targets:
      - https://10.0.0.1
  relabel_configs:
    - source_labels: [__address__]
      target_label: __param_target
    - source_labels: [__param_target]
      target_label: instance
      # Drop the https:// and port (if specified) for the 'instance=' label
      regex: '(?:.+)(?::\/\/)([^:]*).*'
    - target_label: __address__
      replacement: 'prometheus_fortigate:9710'
- job_name: 'ssl_exporter'
  metrics_path: /probe
  scrape_interval: 120m
  scrape_timeout: 60s
  static_configs:
    - targets:
      - bitwarden.konst.fish:443
  relabel_configs:
    - source_labels: [__address__]
      target_label: __param_target
    - source_labels: [__param_target]
      target_label: instance
      # Drop the https:// and port (if specified) for the 'instance=' label
      regex: '(?:.+)(?::\/\/)([^:]*).*'
    - target_label: __address__
      replacement: 'prometheus_ssl_exporter:9219'
- job_name: 'pve'
  scrape_interval: 4m
  scrape_timeout: 60s
  static_configs:
    - targets:
      - 10.0.1.6
  metrics_path: /pve
  params:
    module: [default]
  relabel_configs:
    - source_labels: [__address__]
      target_label: __param_target
    - source_labels: [__param_target]
      target_label: instance
    - target_label: __address__
      replacement: prometheus_proxmox:9221
- job_name: 'minecraft'
  scrape_interval: 1m
  scrape_timeout: 60s
  static_configs:
    - targets: ['10.0.1.103:9225']
      labels:
        server_name: 'Primary Server'
- job_name: 'ssh_honeypot'
  scrape_interval: 10m
  scrape_timeout: 5m
  static_configs:
    - targets: ['prometheus_ssh_honeypot:5000']