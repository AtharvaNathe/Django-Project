# 🎬 Film Management System (Django + MySQL + Bootstrap)

A web-based **Film Management System** built using **Django**, **MySQL**, and **Bootstrap**. This application allows users to manage a film database — add new films, search by genre/language, view reports, and delete records.

---

## 🌟 Features

- ✅ **Add New Film** – Input film name, genre, language, release year, and IMDb rating.
- 📋 **Film Report** – Display all films in a tabular format.
- 🔍 **Search by Genre or Language** – Server-side and AJAX-based searches supported.
- 🧹 **Delete Film** – Remove a film by entering its Film ID.
- 🔐 **User Login** – Basic session-based login system.
- ⚙️ **Responsive UI** – Styled with Bootstrap for mobile-friendly design.

---

## 🛠 Tech Stack

| Layer         | Tech                     |
|---------------|--------------------------|
| **Frontend**  | HTML, CSS, Bootstrap     |
| **Backend**   | Django, Python           |
| **Database**  | MySQL (via Aiven)        |
| **AJAX**      | Native JavaScript        |
| **Templating**| Django Template Engine   |

---

## 📁 Folder Structure

├── templates/
│ ├── index.html
│ ├── NewFilm.html
│ ├── FilmsReport.html
│ ├── SearchGenreResult.html
│ ├── DeleteFilm.html
│ ├── Deleted.html
│ └── genre_results_partial.html
├── static/
│ ├── bootstrap.min.css
│ └── images/
├── views.py
├── services.py
├── urls.py
└── README.md




---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/film-management-system.git
cd film-management-system



2️⃣ Install Dependencies
Make sure Python 3 and pip are installed. Then run:

bash
Copy code
pip install -r requirements.txt
If requirements.txt is not present, install manually:

bash
Copy code
pip install django pymysql



3️⃣ Set Up MySQL Connection
Edit the file services.py and update the database credentials:

python
Copy code
con = pymysql.connect(
    host='your_host',
    port=your_port,
    user='your_user',
    password='your_password',
    database='your_database'
)
Make sure your films and users tables are created in the database.



4️⃣ Run the Django Server
bash
Copy code
python manage.py runserver
Visit http://localhost:8000 in your browser.




✍️ Developed By
Atharva Nathe
Built for educational and demonstration purposes.
