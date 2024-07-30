
```markdown
# Data Pipeline Project

## Introduction
This project sets up a data pipeline using Docker Compose and Ansible. It includes services for log generation, rsyslog, Kafka, Akhq, FTP, Elasticsearch, and Kibana. The project also includes automated setup of Index Lifecycle Management (ILM) and Kafka retention policies.

## Directory Structure
```
```
```

```
data-pipeline-project/
├── ansible/
│   ├── playbook.yml
│   ├── roles/
│   │   ├── docker/
│   │   │   ├── tasks/
│   │   │   │   └── main.yml
│   │   ├── log_generator/
│   │   │   ├── tasks/
│   │   │   │   └── main.yml
│   │   │   ├── files/
│   │   │   │   └── log_generator.py
│   │   ├── rsyslog/
│   │   │   ├── tasks/
│   │   │   │   └── main.yml
│   │   │   ├── files/
│   │   │   │   └── rsyslog.conf
│   │   ├── ilm/
│   │   │   ├── tasks/
│   │   │   │   └── main.yml
│   │   │   ├── files/
│   │   │   │   └── setup_ilm.py
├── docker-compose.yml
├── README.md
└── .env (optional for environment variables)
```

## Steps to Run the Project

### Using Docker Compose
1. **Clone the repository**:
   ```sh
   git clone <repository-url>
   cd data-pipeline-project
   ```

2. **Start the services using Docker Compose**:
   ```sh
   docker-compose up -d
   ```

3. **Access the services**:
   - **Akhq**: [http://localhost:8080](http://localhost:8080)
   - **Kibana**: [http://localhost:5601](http://localhost:5601)
   - **FTP**: Connect using an FTP client to `localhost` on port `21`.

### Using Ansible
1. **Clone the repository**:
   ```sh
   git clone <repository-url>
   cd data-pipeline-project
   ```

2. **Run the Ansible playbook**:
   ```sh
   ansible-playbook -i inventory ansible/playbook.yml
   ```

3. **Access the services**:
   - **Akhq**: [http://localhost:8080](http://localhost:8080)
   - **Kibana**: [http://localhost:5601](http://localhost:5601)
   - **FTP**: Connect using an FTP client to `localhost` on port `21`.

## Configuration
- The log generator script is located in the `log_generator` directory.
- The rsyslog configuration is located in the `rsyslog` directory.
- Kafka and Zookeeper are configured to run on default ports.

## Monitoring
- Use Akhq to monitor Kafka topics.
- Use Kibana to visualize logs stored in Elasticsearch.

## Index Lifecycle Management (ILM)
To manage the lifecycle of Elasticsearch data, follow these steps:

1. **Create an ILM policy**:
   ```sh
   curl -X PUT "localhost:9200/_ilm/policy/my_policy" -H 'Content-Type: application/json' -d'
   {
     "policy": {
       "phases": {
         "hot": {
           "actions": {
             "rollover": {
               "max_size": "50GB",
               "max_age": "30d"
             }
           }
         },
         "delete": {
           "min_age": "90d",
           "actions": {
             "delete": {}
           }
         }
       }
     }
   }
   '
   ```

2. **Create an index template that uses this policy**:
   ```sh
   curl -X PUT "localhost:9200/_index_template/my_template" -H 'Content-Type: application/json' -d'
   {
     "index_patterns": ["my_index-*"],
     "template": {
       "settings": {
         "index.lifecycle.name": "my_policy",
         "index.lifecycle.rollover_alias": "my_index"
       }
     }
   }
   '
   ```

3. **Create the initial index**:
   ```sh
   curl -X PUT "localhost:9200/my_index-000001" -H 'Content-Type: application/json' -d'
   {
     "aliases": {
       "my_index": {
         "is_write_index": true
       }
     }
   }
   '
   ```

## Kafka Retention Policy
To set a retention policy for Kafka topics, follow these steps:

1. **Set the retention policy**:
   ```sh
   kafka-configs.sh --bootstrap-server localhost:9092 --alter --entity-type topics --entity-name mytopic --add-config retention.ms=10800000
   ```

## Notes
- Ensure Docker and Docker Compose are installed on your system.
- Adjust configurations as needed for your environment.
```

