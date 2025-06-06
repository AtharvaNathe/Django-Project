from django.shortcuts import render, redirect
from django.contrib import messages
from .services import FilmOperations

def home(request):
    return render(request, "index.html", {'developer': 'Atharva', 'company': 'Predator Services'})

def newfilm(request):
    return render(request, "NewFilm.html")

def addfilm(request):
    if request.method == "POST":
        try:
            nm = request.POST.get("filmname")
            yr = int(request.POST.get("relyear"))
            gn = request.POST.get("genre")
            ln = request.POST.get("language")
            rt = float(request.POST.get("imdbrating"))
           
            obj = FilmOperations()
            mess = obj.addnewfilmtodb(nm, yr, gn, ln, rt)
            print(mess)
            messages.success(request, 'Film added successfully!')
        except Exception as e:
            print(f'Error in data: {e}')
            messages.error(request, 'Failed to add film!')
    return render(request, "FilmAdded.html")

def filmreport(request):
    obj = FilmOperations()
    data = obj.retrieveallfilmsdata()
    return render(request, "FilmsReport.html", {"filmsdata": data})

def genresearch(request):
    if request.method == "POST":
        gen = request.POST.get("genre")
        obj = FilmOperations()
        dic = obj.searchfilmsongenre(gen)
        return render(request, "SearchGenreResult.html", dic)
    return render(request, "SearchGenreResult.html", {})

def langsearch(request):
    return render(request, "LanguageSearch.html")

def searchonlang(request, lang):
    obj = FilmOperations()
    dic = obj.findfilmsonlang(lang)
    return render(request, "ShowFilmsOnLanguage.html", dic)

def linkgenresearch(request):
    return render(request, "LinksForGenreSearch.html")

def login(request):
    if request.method == "POST":
        id = request.POST.get("userid")
        ps = request.POST.get("password")
        obj = FilmOperations()
        stat = obj.authenticate(id, ps)

        if stat == "success":
            request.session["userid"] = id
            return redirect('home')  
        else:
            messages.error(request, "Invalid credentials, please try again.")
            return render(request, "Failure.html", {"user": id})

    return render(request, "Login.html") 

def delete(request):
    return render(request, "DeleteFilm.html")

def delfilm(request):
    status = "not submitted"
    if request.method == "POST":
        try:
            fid = int(request.POST.get("filmId"))
            obj = FilmOperations()
            status = obj.deletefilm(fid)
            if status == "success":
                messages.success(request, "Film deleted successfully!")
            else:
                messages.error(request, "Failed to delete film.")
        except Exception as e:
            print("Deletion error:", e)
            status = "failed"
            messages.error(request, "An error occurred while deleting.")
    
    uid = request.session.get("userid", "unknown")
    return render(request, "Deleted.html", {"status": status, "userid": uid})


def ajaxgenresearch(request):
    return render(request, 'ajaxgenresearch.html')

def ajaxgen(request, gen):
    obj = FilmOperations()
    dic = obj.searchfilmsongenre(gen)
    return render(request, "genre_results_partial.html", dic)

