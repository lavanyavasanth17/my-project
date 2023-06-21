

1.To install the program we need to have python installed in the local machine.
 # Yum install -y python3

2. I wrote the python code as per the requirement and mentioned the configuration and build steps required for the deployment in Github.
4. I set up the entire CI/CD pipeline on AWS cloud by using the resources available like codepipeline and EC2 instance.
5. I integrated the github with the pipeline on AWS cloud.
6. So, as soon as i make changes and commit the code on github the pipeline on AWS cloud gets triggered and source code is drawn for building.
7. After the code gets built, it goes into the deployment stage and the application gets deployed.
8. I then established a connection with the Ec2 instance used the CLI mode to run the application.
9. ##Pipeline Check3
To run the application please run the following commands:

           # cd /home/ec2-user/demo-repo/
           # python3 main.py

10.Screenshots from the aws pipeline:
The Whole Pipeline:
 ![image](https://github.com/lavanyavasanth17/my-project/assets/121149803/844f09f2-cf67-4969-b737-0e5b078b7ccf)

Scource Code:
 ![image](https://github.com/lavanyavasanth17/my-project/assets/121149803/33bc814c-ce37-42bd-9de5-bbf1d26134be)

Running code in the ec2 instance:
![image](https://github.com/lavanyavasanth17/my-project/assets/121149803/c3d462cd-d357-4409-bd74-f53f51a7f60e)


            
11.To improve my task I would use the following technologies:
           * Docker (Host the application : containerisation )
           * Kubernetes (Cluster for different environments like prod,dev,test )
           * Terraform (Infrastructure Customization :  different cloud intergration)
           * Ansible (Felexible : Paraller executions)
           * Jenkins (Pipeline )
   Apart from these, i can also use other tools such a Graddle/Maven for building the code,Sonarqube for code review,Jfrof for running tests on Artifacts,Nexus for the backup of configuration file,Grafana and Prometheus for monitoring the Kubernetes cluster,Tomcat as a webserver and many other monitoring and data logging tools like Datadog,CloudWatch,cloudtrail,splunk etc..       
