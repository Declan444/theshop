# **DEPLOYMENT**

## **Table of Contents**

* [**Table of Contents**](#table-of-contents)
* [**Initial Deployment**](#initial-deployment)
    * [**Create and setup repository**](#create-and-setup-repository)
    * [**Create Heroku App**](#create-heroku-app)
    * [**AWS S3 Bucket**](#aws-s3-bucket) 
    

## **Initial Deployment**

### **Create and setup repository**

* Log in your Github account (or register if you don't have one yet) and create a new repository. I use VS Code for all my coding.
* In repository go to 'Projects' tab and click 'Link a project', select 'Create new project' from dopdown menu.
* Click on 'Board' and rename it.
* Click on 'Workflows' and 'Item added' to project and 'Edit'.
* Click 'Issue', 'Pull Request' and unselect pull request (this way it will define item as an issue).
* Set value as 'To Do'. Save and turn on 'Workflow'. Exit workflow.
* Open 'Settings' from ... menu located in the top corner. In 'Danger zone' change board to public (if needed to be accessible by others). Go back to 'Settings' tab.
* Scroll to 'Features', within 'Issues' click 'Set up templates', choose 'Custom template'.
* Preview it and click 'pen item' to edit. Add description using template.
* 'Propose changes' and 'commit'.
* To create user story, click on 'Issues', then 'New Issue', 'Get Started'. Fill in the blanks.
* Click on 'Projects' and select appropriate.
* Click 'Submit new issue'.
* Go to 'Projects' tab, click on 'User Stories Kanban Board' to see the user story in 'ToDo' list.
* Populate board with neccessary User Issues to help with project planning and development.<hr>

* Create a directory with the repository name on your local drive. 
* Open VS Code, select file, new window, select clone git repository, and save it to the newly created directory. This links your local directory to your github repository.
* Click on terminal and click new terminal. in the new terminal type <code>python -m venv 'project name'</code> and enter. Then the command <code>.\prpject name\Scripts\Activate</code>. This activates the virtual environment.
* In terminal type <code>pip3 install Django~ =4.2.1</code>(choose Django version you would like to use)
* Install supporting libraries <code>pip3 install dj_database_url</code>, <code>pip3 install psycopg2</code>
* Install gunicorn <code>pip3 install gunicorn</code>
* Create a file Procfile in root and declare web process followed by command <code>web: gunicorn <YOUR_PROJECT_NAME>.wsgi:application</code>
* Create requirements.txt <code>pip3 freeze -r requirements.txt</code>
* Create .gitignore and env.py file for credentials and partS of project that should be  ignored by git, therefore not pushed to Github.
* Create a project <code>django-admin startproject <YOUR_PROJECT_NAME></code>
* Create Initial commit and push to Github.
* Create an app within the project <code>py manage.py startapp <YOUR_APP_NAME></code>
* Add the new app to the list of installed apps in settings.py
* Migrate changes <code>py manage.py migrate</code>
* Test server to ensure it works locally <code>py manage.py runserver</code>

### **Create Heroku App**

Either login or create an account with [Heroku](https://id.heroku.com/login) and sign in.

* Create a new Heroku app. Click 'New' in the top right corner of the landing page, then click 'Create new app'.
* Choose the app a unique name - this will be part of the URL.
* Select the nearest location for yourself and click 'Create App'.
* On the next page click 'Settings' tab and scroll down to 'Config Vars'. This is the place where you hide things like credentials and API keys.
* Scroll down to Buildpacks. The buildpacks will install further dependencies that are not included in the requirements.txt. For this project, the buildpack required is Python.
* Go to 'Deploy' tab and enable deployment method with Github. You will need authorisation if it's first time deploying to Heroku.
* Find app repository by typing in search bar and click 'Connect' for the correct one.
* Enable 'Automatic Deploys' (unless you prefer to keep it manual) then click 'Deploy'
* Once this is done, a message should appear letting know that the app was successfully deployed with a view button to see the app.
* Add database to the Heroku app:
    * Navigate to the 'Resources' tab of the app dashboard. Under the heading 'Add ons' search for 'Heroku Postgres' and click on it when it appears.
    * Select 'Hobby Dev - Free' from the 'plan name' dropdown menu and click 'Submit Order Form'.

### **AWS S3 Bucket**

Login or create an account with [AWS](https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fus-east-1.console.aws.amazon.com%2Fconsole%2Fhome%3FhashArgs%3D%2523%26isauthcode%3Dtrue%26nc2%3Dh_ct%26region%3Dus-east-1%26skipRegion%3Dtrue%26src%3Dheader-signin%26state%3DhashArgsFromTB_us-east-1_5ebca9aa1f981aaf&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge=tXaJuB6g7gFkIttyTd75shZNQrYlt0B3-zdaKPesuQI&code_challenge_method=SHA-256) and sign in.

* Create a new S3 bucket:
    * Click 'Services' in the top left hand corner of the landing page, click on 'Storage' then click 'S3'.
    * Click 'Create bucket'.
    * Give the bucket a unique name - this will be part of the URL.
    * Select the nearest location for yourself.
    * Under the 'Object Ownership' section, select 'ACLS enabled'.
    * Under the 'Block Public Access settings for this bucket' section, untick 'Block all public access' and tick the box to acknowledge that this will make the bucket public.
    * Click 'Create bucket'.
* Amend Bucket settings:
    * Bucket Properties:
       * Click on the bucket name to open the bucket.
       * Click on the 'Properties' tab.
       * Under the 'Static website hosting' section, click 'Edit'.
       * Under the 'Static website hosting' section select 'Enable'.
       * Under the 'Hosting type' section ensure 'Host a static website' is selected.
       * Under the 'Index document' section enter 'index.html'.
       * Click 'Save changes'.
    * Bucket Permissions:
       * Click on the 'Permissions' tab.
       * Scroll down to the 'CORS configuration' section and click edit.
       * Enter the following snippet into the text box:

       ```JSON
            [
                {
                    "AllowedHeaders": [
                    "Authorization"
                    ],
                    "AllowedMethods": [
                    "GET"
                    ],
                    "AllowedOrigins": [
                    "*"
                    ],
                    "ExposeHeaders": []
                }
            ]
        ```

       * Click 'Save changes'.
       * Scroll back up to the 'Bucket Policy' section and click 'Edit'.
       * Take note of the 'Bucket ARN' click on the 'Policy Generator' button to open the AWS policy generator in a new tab.
       * In the newly opened tab under Step 1 'Select Policy Type' select 'S3 Bucket Policy'. from the drop down menu.
       * Under Step 2 'Add Statement(s)' enter ' * ' in the 'Principal' text box.
       * From the 's3:Action' drop down menu select 's3:GetObject'.
       * Enter the 'ARN' noted from the bucket policy page into the 'Amazon Resource Name (ARN)' text box.
       * Click 'Add Statement'.
       * Under Step 3 'Generate Policy' click 'Generate Policy'.
       * Copy the resultant policy and paste it into the bucket policy text box on the previous tab.
       * In the same text box add '/*' to the end of the resource key to allow access to all resources in this bucket.
       * Click 'Save changes'.
       * When back on the buckets permissions tab, scroll down to the 'Access Control List' section and click 'Edit'.
       * enable 'List' for 'Everyone (public access)', tick the box to accept that 'I understand the effects of these changes on my objects and buckets'  and click 'Save changes'.

* Create AWS static files User and assign to S3 Bucket:
    * Create 'User Group':
        * Click 'Services' in the top left hand corner of the landing page, from the left side of the menu click on 'Security, Identity, & Compliance' and select 'IAM' from the right side of the menu.
        * Under 'Access management' click 'User Groups'.
        * Click 'Create Group'.
        * Enter a user name.
        * Scroll to the bottom of the page and click 'Create Group'.
    * Create permissions policy for the new user group:
        * Click 'Policies' in the left-hand menu.
        * Click 'Create Policy'.
        * Click 'Import managed policy'.
        * Search for 'AmazonS3FullAccess', select this policy, and click 'Import'
        * Click 'JSON' under 'Policy Document' to see the imported policy
        * Copy the bucket ARN from the bucket policy page and paste it into the 'Resource' section of the JSON snippet. Be sure to remove the default value of the resource key ("*") and replace it with the bucket ARN.
        * Copy the bucket ARN a second time into the 'Resource' section of the JSON snippet. This time, add '/*' to the end of the ARN to allow access to all resources in this bucket.
        * Click 'Next: Tags'
        * Click 'Next: Review'
        * Click 'Review Policy'
        * Enter a name for the policy
        * Enter a description for the policy
        * Click 'Create Policy'
    * Attach Policy to User Group:
        * Click 'User Groups' in the left-hand menu
        * Click on the user group name created during the above step
        * Select the 'Permissions' tab
        * Click 'Attach Policy'
        * Search for the policy created during the above step, and select it
        * Click "Attach Policy'
    * Create User:
        * Click 'Users' in the left hand menu
        * Click 'Add user'
        * Enter a 'User name'
        * Select 'Programmatic access' and 'AWS Management Console access'
        * Click 'Next: Permissions'
        * Select 'Add user to group'
        * Select the user group created during the above step
        * Click 'Next: Tags'
        * Click 'Next: Review'
        * Click 'Create user'
        * Take note of the 'Access key ID' and 'Secret access key' as these will be needed to connect to the S3 bucket
        * Click 'Download .csv' to download the credentials.
        * Click 'Close'
* Install required packages to used AWS S3 Bucket in Django <code>pip3 install boto3</code> and <code>pip3 install django-storages</code>
* Add 'storages' to the bottom of the installed apps section of settings.py file:

   ```python
    INSTALLED_APPS = [
    …,
        'storages'
    …,
   ]
   ```


[Back to Readme](README.md)