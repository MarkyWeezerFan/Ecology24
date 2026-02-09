from django.shortcuts import render, redirect
from django.contrib import messages
from main.services import get_all_rows
from datetime import datetime

def index(request):
    return render(request, 'main/index.html')

def achievement(request):
    achievements = get_all_rows("Достижения")
    return render(request, 'main/achievement.html', {'photos': achievements})

def public(request):
    publications = get_all_rows("Публикации")
    return render(request, 'main/public.html', {'photos': publications})

def project(request):
    projects = get_all_rows("Проекты")
    return render(request, 'main/projects.html', {'photos': projects})

def projects_details(request, ID):
    projects_details = get_all_rows("Проекты")
    projects = next((item for item in projects_details if item['ID'] == ID), None)
    context = {
        'projects': projects
    }
    return render(request, 'main/project_detail.html', context)

def people(request):
    people = get_all_rows("Сотрудники")
    return render(request, 'main/people.html', {'photos': people})

def people_details(request, ID):
    people_details = get_all_rows("Сотрудники")
    people = next((item for item in people_details if item['ID'] == ID), None)
    context = {
        'people': people
    }
    return render(request, 'main/people_detail.html', context)

def news(request):
    news = get_all_rows("Новости")
    return render(request, 'main/news.html', {'photos': news})

def news_details(request, ID):
    news_details = get_all_rows("Новости")
    news = next((item for item in news_details if item['ID'] == ID), None)
    context = {
        'news': news
    }
    return render(request, 'main/news_detail.html', context)

def media(request):
    media = get_all_rows("СМИ")
    return render(request, 'main/media.html', {'photos': media})

def login(request):
    if request.method == 'POST':
        login_value = request.POST.get('login')  # Получаем значение по имени поля
        password_value = request.POST.get('password')
        if login_value == 'SFUAdmin' and password_value == '242424':
            return redirect('analytics')
        else:
            messages.error(request, 'Неверный логин или пароль, попробуйте ещё раз!')
    return render(request, 'main/login.html')

def analytics(request, employee_id=None):
    current_year = datetime.now().date()
    people = get_all_rows("Сотрудники")
    public = get_all_rows("Публикации")
    proj = get_all_rows("Проекты")
    selected_employee = None
    young = 0
    pub_count = 0
    proj_count = 0
    if request.GET.get('employee_id'):
        ID = request.GET.get('employee_id')
        selected_employee = next(
            (emp for emp in people if str(emp.get('ID')) == ID),
            None
        )
    if selected_employee and selected_employee.get('Date_of_birth'):
        date_year = selected_employee['Date_of_birth']
        date_year = datetime.strptime(date_year, "%d.%m.%Y").date()
        age = (current_year - date_year).days // 365.25
        if int(age) < 39:
            young = age

    if selected_employee:
        selected_surname = selected_employee.get('Full_Name').split()[0]
        selectname_eng = selected_employee.get('Eng_Name').split()[0]
        if selected_surname:
            for publication in public:
                surnamespub = []
                authors = publication.get('Authors').split(',')
                for a in authors:
                    au = a.split()
                    for abc in au:
                        if abc[-1] != '.':
                            surnamespub.append(abc)
                for author in surnamespub:
                    if str(author) == str(selected_surname) or str(author) == str(selectname_eng):
                        pub_count += 1
            for project in proj:
                partic = project.get("Participator").split(',')
                Direct = project.get("Director")
                if partic:
                    surnamesproj = []
                    for p in partic:
                        part = p.split()
                        for participators in part:
                            if participators[-1] != '.':
                                surnamesproj.append(participators)
                    for dir in Direct:
                        d = dir.split()
                        for director in d:
                            if director[-1] != '.':
                                surnamesproj.append(director)
                    for surname in surnamesproj:
                        if str(surname) == str(selected_surname) or str(surname) == str(selectname_eng):
                            proj_count += 1
    return render(request, 'main/analytics.html', {
        'now': current_year,
        'employees': people,
        'selected_employee': selected_employee,
        'young': young,
        'pub_count': pub_count,
        'proj_count': proj_count,
    })

def contacts(request):
    return render(request, 'main/contacts.html')