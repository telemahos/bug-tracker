- python3 -m venv env_079 
- ./ngrok http 8000 
- ngrok http 8000 (on Windows)
- .\env_079\Scripts\activate.bat (On windows)
- source env_079/bin/activate
- pip3 install --upgrade pip
- pip3 install -r docs/requirements.txt
- uvicorn backend.main:app --reload
- npm run serve
- npm run 
- To deploy install node.js server: sudo npm install -g serve --AND THEN-- serve -s dist 


- pip install fastapi-pagination[all]
- https://www.learmoreseekmore.com/2021/02/vue3-vue-tailwind-pagination.html
    npm install --save @ocrv/vue-tailwind-pagination
- npm install vue-chartjs chart.js@2.9.4
- npm install @vueform/multiselect 
- More info on(https://github.com/vueform/multiselect#styling)


- VS Theme: "One Dark Pro Darker", "Noctis Azureus", 'Bluloco Dark theme', 'NoctisUva', 'Viow Flat', "Adapta Nikto"
- requirements => fastapi==0.66.0 αν θέλουμε μια συξκερκιμένη έκδοση

--------------
routers -> controller
repository -> model
--------------
User Roles:
no Role -> 0
Admin -> 1
Frontend Developer -> 2
Backend Developer -> 3
Full Stack Developer -> 4
UI/UX Designer -> 5
QA Analyst -> 6
Business Analyst -> 7
Product Manager -> 8
Technology Manager -> 9
--------------
Issue, Bug, Priority:
Low -> 0
Medium -> 1
High -> 2
Critical -> 3
--------------
Cases:
Issue -> 0
Bug -> 1
Note -> 2
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
Python3 Switch Version
brew unlink python@3.9
brew unlink python@3.8
brew link --force python@3.9
--------------