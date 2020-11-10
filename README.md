# Project Overview

This project demonstrates how to perform continuous delivery for a Python-based machine learning application using the Flask web framework.

We use a sklearn model, pre-trained to predict housing prices in Boston according to several features, such as average rooms in a home and data about highway access, teacher-to-pupil ratios, and more.

The project uses a flask app, `app.py` that serves out predictions (inference) about housing prices through API calls.  

  

![App diagram](/screenshots/appdiag.PNG)  
  
  


## Setup the Environment

### Step 1: Launch Cloud Shell

Go to the Azure Console and launch a bash shell:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Launch Cloud Shell](/screenshots/screenshot_cloudshell.PNG)


### Step 2: Clone the Repo and Create a Flask ML Service

1. Clone the Repo:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`git clone git@github.com:mhaywardhill/sklearn-flask-webapp.git`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Clone Repo](/screenshots/screenshot_clone.PNG)


2. Set up the Python virtual environment:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`python3 -m venv ~/.Dev-Ops`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`source ~/.Dev-Ops/bin/activate`

3. Run `make all`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![output make all](/screenshots/screenshot_make_all.PNG)


4. Create an app service and deploy the app in the Cloud Shell:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`az webapp up -n <your-appservice> --sku FREE`  
  
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![App Services](/screenshots/screenshot_app_services.PNG)  
  
  

5. Verify the deployed application works by browsing to the deployed url:

Go to `https://<your-appservice>.azurewebsites.net/` and you should see the same output as in the screenshot below:  


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Service URL](/screenshots/screenshot_url.PNG)  


### Step 3: Perform Prediction

Change the line in make_predict_azure_app.sh to match the deployed prediction:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_-X POST https://<yourappname\>.azurewebsites.net:$PORT/predict_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`./make_predict_azure_app.sh`  

A successful prediction will look like this:  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Prediction](/screenshots/screenshot_perform_prediction.png)  


### Step 4: Deploy project to a Azure Pipeline  

Next, we'll need to create an Azure DevOps project and pipeline. Please refer to [the offical documentation for more detail](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).
  
   
    
## Performance Testing 

Below is a screenshot of the performance testing using Locust.  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![locust](/screenshots/screenshot_locust.png)  


## Improvements  

Both CI and CD streams run in parallel; this not ideal as we should only deploy the application if it passes the tests, in GitHub Actions.






