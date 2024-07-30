
```markdown
## Introduction
This project sets up Nginx with SSL using Let's Encrypt and Certbot. It includes configurations for serving static content with Basic Authentication and redirecting to Google.

## Directory Structure
```
nginx-project/
├── ansible/
│   ├── playbook.yml
│   ├── roles/
│   │   ├── nginx/
│   │   │   ├── tasks/
│   │   │   │   └── main.yml
│   │   │   ├── files/
│   │   │   │   ├── nginx.conf
│   │   │   │   ├── local.html
│   │   │   │   └── htpasswd
├── docker-compose.yml
├── nginx/
│   ├── nginx.conf
│   ├── local.html
│   └── htpasswd
├── README.md
└── .env (optional for environment variables)
```

## Steps to Run the Project

### Using Docker Compose
1. **Clone the repository**:
   ```sh
   git clone <repository-url>
   cd nginx-project
   ```

2. **Start the services using Docker Compose**:
   ```sh
   docker-compose up -d
   ```

3. **Access the services**:
   - **Local Page**: [https://localhost:8090/local](https://localhost:8090/local)
   - **Redirect to Google**: [https://localhost:8008/net](https://localhost:8008/net)

### Using Ansible
1. **Clone the repository**:
   ```sh
   git clone <repository-url>
   cd nginx-project
   ```

2. **Run the Ansible playbook**:
   ```sh
   ansible-playbook -i inventory ansible/playbook.yml
   ```

3. **Access the services**:
   - **Local Page**: [https://localhost:8090/local](https://localhost:8090/local)
   - **Redirect to Google**: [https://localhost:8008/net](https://localhost:8008/net)

## Configuration
- The Nginx configuration is located in the `nginx` directory.
- The static content and authentication files are also located in the `nginx` directory.

## Security
- Nginx version is hidden.
- XSS Protection is enabled.
- MIME Sniffing is disabled.
- HTTPS is enabled for requests.

## Notes
- Ensure Docker and Docker Compose are installed on your system.
- Adjust configurations as needed for your environment.
```



(1) How To Secure Nginx with Let's Encrypt on Ubuntu 20.04. https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04.
(2) How To Secure Nginx with Let's Encrypt on Ubuntu. https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-22-04.
(3) How To Secure Nginx with Let's Encrypt on Rocky Linux 9. https://bing.com/search?q=Nginx+SSL+configuration+with+Let%27s+Encrypt+and+Certbot.
(4) Part 1: Easy TLS / SSL setup using Certbot and Let’s Encrypt - Serverwise. https://www.ssdnodes.com/blog/nginx-tls-setup-certbot-lets-encrypt/.
(5) Install Let’s Encrypt SSL with Certbot on Nginx - AZDIGI Blog. https://azdigi.com/blog/en/linux-server-en/install-lets-encrypt-ssl-with-certbot-on-nginx/.
