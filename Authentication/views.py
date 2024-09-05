from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from Authentication.models import Report


from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape, A3
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from .models import Report  # Make sure this is the correct import

# Create your views here.

def HomePage(request):
    return render(request,'user.html')

def SignupPage(request):
    from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def AdminPage(request):
    return render(request, 'admin.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')


    # Render signup form if not POST
    return render(request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        # if user is not None and username!='admin':
        #     login(request,user)
        #     return redirect("index")
        # elif user is not None and username=='admin' and password=='admin123':
        #     login(request,user)
        #     return redirect("adminUser")
        if user:
            if username == "admin" and password == "admin123":
                login(request,user)
                return redirect("admin") 
            else:
                login(request,user)
                return redirect("index")
        else:
            return HttpResponse("Username or Password Incorrect!!")
    return render(request,'index.html')
def LogoutPage(request):
    logout(request)
    return redirect('index') 

def report_view(request):
    if request.method == "POST":
        dept = request.POST['dept']
        numStudents = request.POST['numStudents']
        deptAvg= request.POST['deptAvg']
        publications = request.POST['publications']
        patents = request.POST['patents']
        achievements = request.POST['achievements']
        awards = request.POST['awards']
        alumniAchievements = request.POST['alumniAchievements']
        startups = request.POST['startups']
        # print(dept,numStudents,deptAvg,publications,patents,achievements,awards,alumniAchievements,startups)  
        ins = Report(dept=dept, numStudents=numStudents, deptAvg=deptAvg, publications=publications, patents=patents, achievements=achievements, awards=awards, alumniAchievements=alumniAchievements, startups=startups)
        ins.save()
        print("Data written to the db")

    return render(request,'user.html')

'''def download_pdf(request):
    # Get the department from the request
    dept = request.GET.get('department', None)  # Default to None if 'department' is not in the request

    if not dept:
        return HttpResponse("Department not specified", status=400)

    # Now you can use 'dept' in your query to filter data
    model_name = Report.__name__
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename={model_name}_{dept}.pdf'

    pdf = canvas.Canvas(response, pagesize=landscape(letter))
    pdf.setTitle(f'PDF Report for {dept}')

    # Fetch data based on the department
    queryset = Report.objects.filter(department=dept)

    headers = [field.verbose_name for field in Report._meta.fields]
    data = [headers]

    for obj in queryset:
        data_row = [str(getattr(obj, field.name)) for field in Report._meta.fields]
        data.append(data_row)

    col_widths = [1.5 * inch] * len(headers)  # Adjust column widths
    table = Table(data, colWidths=col_widths)

    table.setStyle(TableStyle(
        [
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]
    ))

    # Adjust the placement to ensure the table fits the page
    canvas_width, canvas_height = landscape(letter)
    table.wrapOn(pdf, canvas_width, canvas_height)
    table_height = table._height
    y_position = canvas_height - table_height - 250

    table.drawOn(pdf, 10, y_position)
    
    pdf.save()
    return response'''





def download_pdf(request):
    dept = request.GET.get('department', None)
    if not dept:
        return HttpResponse("Department not specified", status=400)
    
    print(f'Department: {dept}')  # Debugging line
    
    queryset = Report.objects.filter(dept=dept)
    print(f'Queryset: {queryset}') 
    # Now you can use 'dept' in your query to filter data
    model_name = Report.__name__
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename={model_name}_{dept}.pdf'

    pdf = canvas.Canvas(response, pagesize=landscape(A3))
    pdf.setTitle(f'PDF Report for {dept}')

    # Fetch data based on the department
    queryset = Report.objects.filter(dept=dept)

    headers = [field.verbose_name for field in Report._meta.fields]
    data = [headers]

    for obj in queryset:
        data_row = [str(getattr(obj, field.name)) for field in Report._meta.fields]
        data.append(data_row)

    col_widths = [1.3 * inch] * len(headers)  # Adjust column widths
    table = Table(data, colWidths=col_widths)

    table.setStyle(TableStyle(
        [
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]
    ))

    # Adjust the placement to ensure the table fits the page
    canvas_width, canvas_height = landscape(A3)
    table.wrapOn(pdf, canvas_width, canvas_height)
    table_height = table._height
    y_position = canvas_height - table_height - 250

    table.drawOn(pdf, 100, y_position)
    
    pdf.save()
    return response
