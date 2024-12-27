
# **Polynome Microservices with Spring Boot, React, and Flutter**

This platform enables polynomial calculations, factorization, and analysis through a microservices-based architecture. The backend is built with Spring Boot, while the frontend is implemented using React and Flutter.

---

## **Table of Contents**
- [Overview](#overview)
- [Software Architecture](#software-architecture)
- [Docker Configuration](#docker-configuration)
- [Frontend](#frontend)
- [Backend](#backend)
- [Getting Started](#getting-started)
- [Video Demonstration](#video-demonstration)
- [Usage](#usage)
- [Contributing](#contributing)

---

## **Overview**

This project implements:
- Polynomial calculations using microservices.
- Integration of React and Flutter frontends with Spring Boot backend.
- Scalable architecture using Docker containers for deployment.

---

## **Software Architecture**


Explore the interactive architecture here: [Software Architecture](https://app.eraser.io/workspace/ckNFDmpsj8GlPOET39RP?origin=share)

The architecture consists of:
- **Backend**: Spring Boot with MySQL for storage.
- **Frontends**:
  - React: For web-based interaction.
  - Flutter: For mobile applications.

---

## **Docker Configuration**

Below is the `docker-compose.yml` configuration for deploying all services (MySQL, backend, React frontend, Flutter frontend, and PhpMyAdmin).

```yaml
version: '3.8'

services:
  mysql:
    image: mysql:5.7
    container_name: mysql
    ports:
      - "8080:3306" # Maps MySQL's default port 3306 to 8080 on host
    environment:
      MYSQL_DATABASE: polynomes
      MYSQL_ALLOW_EMPTY_PASSWORD: 'yes' # No password for MySQL root user

  backend:
    build:
      context: ./CalculPolynome-backend
      dockerfile: Dockerfile
    container_name: backend
    ports:
      - "8081:8081"
    environment:
      SPRING_DATASOURCE_URL: jdbc:mysql://mysql:3306/polynomes
      SPRING_DATASOURCE_USERNAME: root
      SPRING_DATASOURCE_PASSWORD:
    depends_on:
      - mysql

  react-frontend:
    build:
      context: ./polynome_front_react
      dockerfile: Dockerfile
    container_name: react-frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend

  flutter-frontend:
    build:
      context: ./polynome_front_flutter
      dockerfile: Dockerfile
    container_name: flutter-frontend
    ports:
      - "8088:80"
    environment:
      API_BASE_URLS: |
        http://10.0.2.2:8081
    depends_on:
      - backend

  phpmyadmin:
    image: phpmyadmin/phpmyadmin
    container_name: phpmyadmin
    ports:
      - "8089:80"
    environment:
      PMA_HOST: mysql
      MYSQL_ALLOW_EMPTY_PASSWORD: 'yes' # No password for MySQL root user
```

---

## **Frontend**

### React Frontend:
- **Technologies**: React, JavaScript, HTML, CSS.
- **Port**: `http://localhost:3000`
- **Setup**:
  - Navigate to `polynome_front_react`.
  - Install dependencies:
    ```bash
    npm install
    ```
  - Start the development server:
    ```bash
    npm start
    ```

### Flutter Frontend:
- **Technologies**: Flutter, Dart.
- **Port**: `http://localhost:8088`
- **Setup**:
  - Navigate to `polynome_front_flutter`.
  - Ensure Flutter is installed:
    ```bash
    flutter doctor
    ```
  - Run the application:
    ```bash
    flutter run
   


 ```

````

## **Backend**

### **Technologies**:
- Spring Boot
- MySQL

### **Setup**:
1. **Install Dependencies**:
   ```bash
   mvn clean install
   ```
2. **Run Backend**:
   ```bash
   mvn spring-boot:run
   ```
3. Access the backend API at:
   ```
   http://localhost:8081
   ```

### **Backend Project Structure**

#### **Overall Structure**
The backend consists of multiple microservices organized into different modules, each focusing on a specific domain of polynomial calculations. Below is the structure of the key components:

- **`api-gateway`**:
  - Serves as the unified entry point for all client requests.
  - Routes incoming requests to the appropriate microservices.
  - Handles load balancing and service discovery integration with Eureka.

- **`eureka-server`**:
  - Acts as the service registry for all microservices.
  - Ensures dynamic discovery of microservices for seamless communication.

- **`service-factorisation`**:
  - Focuses on polynomial factorization operations.
  - **Sub-packages**:
    - **`controller`**: Exposes RESTful endpoints for polynomial factorization.
    - **`service`**: Implements the core business logic for factorization.
    - **`model`**: Defines the data structures representing polynomial factors.
    - **`repository`**: Provides interfaces for database operations related to factors.

- **`service-polynome`**:
  - Handles general polynomial operations like creation, updates, and retrieval.
  - **Sub-packages**:
    - **`controller`**: Defines REST endpoints for polynomial management.
    - **`service`**: Implements the business logic for managing polynomials.
    - **`model`**: Defines the data structures and entities representing polynomials.
    - **`repository`**: Contains interfaces for interacting with the database to manage polynomial data.

- **`service-racines`**:
  - Focuses on finding roots of polynomials.
  - **Sub-packages**:
    - **`controller`**: Handles HTTP endpoints for polynomial root operations.
    - **`service`**: Encapsulates the logic for computing polynomial roots.
    - **`model`**: Defines entities related to polynomial roots.
    - **`repository`**: Interfaces for data persistence related to polynomial roots.

---

### **General Notes**:
- Each microservice in the backend follows a modular design pattern, with clearly defined layers for **controller**, **service**, **model**, and **repository**.
- Communication between microservices is managed through REST APIs and registered via the **Eureka Server**.
- The **API Gateway** serves as a unified entry point for all client requests, forwarding them to the appropriate microservices.


## **Getting Started**

### **Prerequisites**:
1. **Git**: Download from [git-scm.com](https://git-scm.com/).
2. **Node.js**: Use NVM to install Node.js (version 14.11.0).
3. **Flutter**: Install Flutter SDK.

### **Steps**:
1. Clone the repository:
   ```bash
   git clone https://github.com/Neha-ETTALEBY/CalculPolynomial-microservices-springboot-react-flutter.git
   ```
2. Start Docker:
   ```bash
   docker-compose up
   ```

---
---

## **Video Demonstration**

Click the links below to watch the application in action:
- [Backend & Frontend Demonstration](https://github.com/user-attachments/assets/6e781dda-6457-4a27-8ae5-c62f4d223c9d)
- [Flutter Mobile Demonstration](https://github.com/user-attachments/assets/68736cf1-891f-4c27-a825-03b8cb6e1e44)

---

