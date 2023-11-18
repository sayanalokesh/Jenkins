# Jenkins Installation Guide 👨‍💻🚀

Jenkins is your gateway to seamless automation and continuous integration. Follow this guide to install Jenkins on your Linux-based system with ease! 😃

## Prerequisites 🛠️

Before we begin, make sure you have:

- A Linux-based system (e.g., Ubuntu 22.04 LTS). You can go to the AWS account and launch an Instance using Ubuntu as the operating system.
![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/96aaaa47-0e34-4554-ac5d-ee5c643b0b87)
![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/52442664-d2cd-43d9-97d6-d8f158ac9b9a)

- Once you launch an instance, you must open the 8080 port since Jenkins is set to run.
![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/d6d43d5d-39a5-4a3d-b2a7-19145ec7121b)

- Once these steps are performed, go to the instance and connect to the instance.

## Step 1: Update and Upgrade 🔄

Let's start by ensuring your system is up-to-date:

```bash
sudo apt update
sudo apt upgrade -y
```

## Step 2: Install Java 🍵

Jenkins runs on Java, so let's install OpenJDK 17:

```bash
sudo apt install openjdk-17-jre
```

## Step 3: Add Jenkins Repository 🔑

Add the Jenkins repository key and source to your system:

```bash
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
    /usr/share/keyrings/jenkins-keyring.asc > /dev/null
```

```bash
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
    https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
    /etc/apt/sources.list.d/jenkins.list > /dev/null
```

## Step 4: Update and Install Jenkins 🚀

Update your package list and install Jenkins:

```bash
sudo apt-get update
sudo apt-get install jenkins
```

## Step 5: Enable and Start Jenkins 🏁

Enable Jenkins to start on boot and start the service:

```bash
sudo systemctl enable jenkins
sudo systemctl start jenkins
```

## Step 6: Verify Jenkins Status 🚦

Make sure Jenkins is up and running:

```bash
sudo systemctl status jenkins
```

## Step 7: Access Jenkins 🌐

Open your web browser and navigate to:

```
http://<instanceIPaddress>:8080
```

## Step 8: Get Your Initial Admin Password 🤖

To unlock Jenkins, you need the initial admin password. Retrieve it using this command:

```bash
cat /var/lib/jenkins/secrets/initialAdminPassword
```
![image](https://github.com/sayanalokesh/Jenkins/assets/105637305/1c268480-02ee-443a-8b3c-a1555b4afea5)

Now you're all set to configure Jenkins and start automating your workflows! Enjoy your journey with Jenkins! 🎉👩‍💻👨‍💻
