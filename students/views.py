from django.http import HttpResponse, Http404

STUDENTS = [
    {"id": 1, "name": "Abd", "age": 22, "ville": "Kebemer"},
    {"id": 2, "name": "Moussa", "age": 23, "ville": "Dakar"},
    {"id": 3, "name": "Fatou", "age": 21, "ville": "Louga"},
]

TEACHERS = [
    {"id": 1, "name": "Mr Diallo", "matiere": "Maths"},
    {"id": 2, "name": "Mme Sow", "matiere": "Info"},
]

def home(request):
    return HttpResponse("<h1>Bienvenue a abd</h1><a href='/students/'>Etudiants</a> | <a href='/teachers/'>Enseignants</a> | <a href='/about/'>About</a>")

def students_list(request):
    html = "<h1>Liste des etudiants</h1><ul>"
    for s in STUDENTS:
        html += f"<li><a href='/students/{s['id']}/'>{s['name']}</a></li>"
    html += "</ul>"
    return HttpResponse(html)

def students_detail(request, id):
    for s in STUDENTS:
        if s['id'] == id:
            return HttpResponse(f"<h1>{s['name']}</h1><p>Ville: {s['ville']}</p><a href='/students/'>Retour</a>")
    raise Http404("Not found")

def teachers_list(request):
    html = "<h1>Enseignants</h1><ul>"
    for t in TEACHERS:
        html += f"<li>{t['name']} - {t['matiere']}</li>"
    html += "</ul><a href='/'>Accueil</a>"
    return HttpResponse(html)

def about(request):
    return HttpResponse("<h1>Ecole Kebemer</h1><p>Projet Abd 2026</p><a href='/'>Accueil</a>")