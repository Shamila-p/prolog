
<!DOCTYPE html>
<html>
<head>
  
</head>
<body style="background-color: #f3f3f3; padding: 20px; font-family: Arial, sans-serif;">

<h1 style="color: #333;">Prolog</h1>

<p>This project aims to a college management system. I have build the frontend using html, css, bootstrap, js and the backend using Python-django Framework. Here I provided different dashboard for Teachers and Student. The Teacher again comes to different division like Principal(Admin), HOD, Tutors. I have incorporated MySQL as database for storing all information.  </p>

<h2 style="color: #555;">Features</h2>

<ul>
  <li>Role based Login which direct to respective dashboard.</li>
  <li>Admin page(Principal) can add Departments, Teachers, Fee structure, assign HOD to each deaprtment, can send notification. All crud operations are done. </li>
  <li>HOD can add different Semesters, Classes and they assign teachers to each department.</li>
  <li>Students can download assignments, Study materials, Time table etc.</li>
  <li>Payment gateways such as paypal and Razorpay.</li>
</ul>

<h2 style="color: #555;">Pre-requisite</h2>

<p>Before running this application, ensure you have the following dependencies installed:</p>

<ol>
  <li>Python 3.7+</li>
  <li>pip3</li>
  <li>MySQL</li>
</ol>
<h2 style="color: #555;">Installation</h2>

<ol>
  
   <li>Create virtual environment</li>
   <pre><code>python -m venv “name of environment”</code></pre>
  
  <li>Connect to the virtual environment</li>
  <pre><code>source name_of_environment/bin/activate</code></pre>

  <li>Clone this repository to your local machine.</li>
  <pre><code>git clone https://github.com/your-username/your-repo.git</code></pre>

  <li>Install the required Python packages using pip.</li>
  <pre><code>pip install -r requirements.txt</code></pre>

  <li>Create a database in MySQL</li>
  <li>Create a .env file inside the root directory.Provide the required values for each environment variable in the .env.example file.</li>
  <li>Migrate the models created onto database.</li>
  <pre><code>python manage.py makemigrations</code></pre>
  <pre><code>python manage.py migrate</code></pre>

  <li>Create a superuser(Principal)</li>
  <pre><code>python manage.py createsuperuser</code></pre>

  <li>Run the application on djangos default port 8000</li>
  <pre><code>python manage.py runserver</code></pre>
  
</ol>

</body>
</html>
