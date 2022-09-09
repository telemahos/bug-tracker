- python3 -m venv env_078 
- ./ngrok http 8000 
- ngrok http 8000 (on Windows)
- .\env_078\Scripts\activate.bat (On windows)
- source env_078/bin/activate
- pip install --upgrade pip
- pip install -r requirements.txt
- uvicorn backend.main:app --reload
- npm run serve
- npm run 


- pip install fastapi-pagination[all]
- https://www.learmoreseekmore.com/2021/02/vue3-vue-tailwind-pagination.html
    npm install --save @ocrv/vue-tailwind-pagination
- npm install vue-chartjs chart.js@2.9.4

- VS Theme: "Noctis Azureus", 'Bluloco Dark theme', 'NoctisUva', 'Viow Flat', "Adapta Nikto"
- requirements => fastapi==0.66.0 αν θέλουμε μια συξκερκιμένη έκδοση

--------------
routers -> controller
repository -> model
--------------
User Roles:
Admin -> 0
Developer -> 1
QA Analyst -> 2
Business Analyst -> 3
Product Manager -> 4
Technology Manager -> 5
--------------
Issue, Bug, Priority:
Low -> 1
Medium -> 2
High -> 3
Critical -> 4
--------------
Cases:
Issue -> 1
Bug -> 2
Note -> 3
--------------
Team:
id, user_id, project_id, team_role, assign_date, active, note

--------------
Git to work on Win10 with VS Code:
Step 1 in your project folder run start-ssh-agent
Step 2 add your id_rsa or whatever name of your private RSA key password
Step 3 in the same directory open the cmd or power shell and run code
--------------
FRONTEND:
eslint Fehlemeldung -> Loesung fuer Windows:
.\node_modules\.bin\eslint src\** --fix
-> Loesung fuer Mac:
npm run lint -- --fix
--------------

--------------