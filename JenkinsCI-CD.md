# Jenkins Pipeline for Flask Application

# Table of Contents

1. [Overview](#overview)

2. [Prerequisites](#prerequisites)

    a. [Plugins Installation](#plugins-installation)

    b. [Configuring Email Notifications](#configuring-email-notifications)

3. [Pipeline Stages](#pipeline-stages)

    a. [Screenshots](#screenshots)

    b. [Jenkinsfile Configuration](#jenkinsfile-configuration)
4. [Poll SCM](#poll-scm)
5. [Email Notifications](#email-notifications)
6. [Overall Workflow](#overall-workflow)


## Overview

This Jenkins pipeline automates the build, test, and deployment of a Flask application. It fetches the application code from a GitHub repository, installs dependencies, runs unit tests, and deploys to a staging environment.

### Prerequisites

#### Plugins Installation

To support this pipeline, install the following plugins:

- ![Alt text](image.png)
- ![Alt text](image-1.png)

#### Configuring Email Notifications

Configure email notifications by navigating to `Manage Jenkins` > `System` > `E-mail Notification` (scroll to bottom) and set up as shown below:

![Alt text](image-2.png)
![Alt text](image-3.png)
![Alt text](image-4.png)

If configured correctly, you'll see "Email was successfully sent."
![Alt text](image-5.png)

### Pipeline Stages

The pipeline includes these stages:

1. **Checkout:** Retrieves the application code from the GitHub repository.
2. **Build:** Installs application dependencies using `pip`.
3. **Test:** Runs unit tests for the application with `pytest`.
4. **Deploy:** Deploys the application to a staging environment if tests pass.

#### Screenshots

1. ![Alt text](image-6.png)
2. ![Alt text](image-7.png)
3. ![Alt text](image-8.png)
4. ![Alt text](image-9.png)
5. To generate Git syntax for Jenkinsfile, click on `Pipeline Syntax`.
6. ![Alt text](image-10.png)

### Jenkinsfile Configuration

The Jenkinsfile defines pipeline stages and steps:

- `agent any`: Allows the pipeline to run on any available Jenkins agent.
- `git`: Fetches application code from GitHub repository using `git-cred` credentials.
- `pip install`: Installs dependencies from `requirements.txt`.
- `pytest`: Runs unit tests using the `pytest` framework.
- `gunicorn`: Installs and starts the Gunicorn WSGI server to run the Flask application.

[Jenkinsfile Link](https://github.com/sayanalokesh/Jenkins/blob/main/Jenkinsfile)

#### Poll SCM

Poll SCM checks for new commits in Git and automatically triggers the build process to deploy code to the EC2 server.

![Alt text](image-11.png)
![Alt text](image-12.png)
![Alt text](image-13.png)
![Alt text](image-14.png)
![Alt text](image-15.png)

### Email Notifications

The pipeline sends email notifications to `lokesh.sayana@email.com` upon successful or failed builds, with customized subject lines and body content.

![Alt text](image-16.png)
![Alt text](image-17.png)
![Alt text](image-18.png)

### Overall Workflow

1. Checkout code from GitHub repository.
2. Install dependencies using pip.
3. Run unit tests with pytest.
4. Deploy application to staging using Gunicorn.
5. Send email notification indicating build status.
