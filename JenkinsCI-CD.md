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

- ![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/fe102b73-0e09-4f70-a2d4-4e72cb1d52b6)
- ![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/0d524f70-af4b-4037-b475-3e3f3bca4862)


#### Configuring Email Notifications

Configure email notifications by navigating to `Manage Jenkins` > `System` > `E-mail Notification` (scroll to the bottom) and set up as shown below:

![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/4023a0d5-66e3-44a4-b3cc-61b5e17b5f34)
![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/566c9828-1519-44c6-8faf-f62945b2883b)
![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/c22f0ed7-75ec-4f31-952f-e08236baf8ce)
Scroll to the bottom of the page and find App passwords as shown in the screenshot
![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/66842aea-e328-447f-9818-97364166a947)
![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/3573b380-bf52-4c22-ab26-0621a8555405)
![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/fd6eabe8-5158-4b82-8b74-5aef3eb57f32)

Copy and paste the code in the password section.
![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/5500dabb-892e-45bd-8734-1b471aa4ff6a)
![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/09d0fecb-80bb-46be-ac34-6d283721140f)

If configured correctly, you'll see "Email was successfully sent."
![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/413c32fc-639c-41ec-be54-efc974c956cb)


### Pipeline Stages

The pipeline includes these stages:

1. **Checkout:** Retrieves the application code from the GitHub repository.
2. **Build:** Installs application dependencies using `pip`.
3. **Test:** Runs unit tests for the application with `pytest`.
4. **Deploy:** Deploys the application to a staging environment if tests pass.

#### Screenshots

1. ![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/d661ba08-9566-4036-816b-339ebcf19c92)
2. ![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/bffc00bb-e4da-4919-aaae-1e18fb9d90d0)
3. We need to click on `settings` in the GitHub repository, check for `Webhooks`, and give the instance `public IP address:8080/github-webhook/` as shown below.
4. ![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/83c036b0-8a02-4f09-abd3-62c55251c0bc)
5. ![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/988bec3c-1cf1-4a8f-9645-d6ab096cd7e6)
6. ![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/1b2cc8c6-e88c-477e-9ffe-4e2e8e8532ad)
7. To generate Git syntax for Jenkinsfile, click on `Pipeline Syntax`.
8. ![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/59354843-7216-43b2-85c4-cb63fe848d18)

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

![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/b8d911b2-3b32-4299-9f0d-cec0b6fd9ccd)
![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/44db720d-f903-427c-b58f-be7aee0f9c7b)
![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/e9e4a009-af18-4512-9b40-0790d450c16d)
![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/a38f31c6-09b2-427c-a21c-a6128b9d40b1)
![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/373cd1fa-789f-454b-a892-e5315e7109d3)

### Email Notifications

The pipeline sends email notifications to `lokesh.sayana@email.com` upon successful or failed builds, with customized subject lines and body content.

![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/2a2c298f-d1be-44f0-8ef0-f7f772cbae1f)
![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/2fcf4b86-0ff1-46c1-9060-8f073db8c999)
![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/8564462f-d15d-4951-b78c-31583ac9ddf2)


### Overall Workflow

1. Checkout code from GitHub repository.
2. Install dependencies using pip.
3. Run unit tests with pytest.
4. Deploy application to staging using Gunicorn.
5. Send email notification indicating build status.
