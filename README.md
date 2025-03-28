# Monitoring

This repo is used for monitoring metrics on host node (e. g. CPU usage, RAM usage, free disk space, etc.). It is also used for alerting in case of any troubles.

### Prerequisites:
1. Add your telegram bot API token and chat id in `alertmanager/alertmanager.yml`
2. Edit / add alerts in `prometheus/alert_rules.yml` (not necessary) 

### Running
Go to root directory and run `$ docker compose up -d`. You'll be able to access services 
- Prometheus    localhost:9090
- Grafana       localhost:3000
- Alertmanager  localhost:9093

In order to stress test your system and alerting system run python script `load_test.py`

### Maintaining repo

Feel free to create PRs with helpful alerts or any enhancements on the system overall
