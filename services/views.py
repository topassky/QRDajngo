from django.shortcuts import render, get_object_or_404
from .models import Service
import psycopg2
from django.http import HttpResponse
# Create your views here.

def services(request):
    #services = Service.objects.all()
    #services = Category.objects.filter(name="12")
    try:
        
        PSQL_HOST = "ec2-34-193-42-173.compute-1.amazonaws.com"
        PSQL_PORT = "5432"
        PSQL_USER = "qlbdgwbnelasno"
        PSQL_PASS = "495257845f432fb50131165b34a93e99eff5292fbae1b76ce08e59b924b2a903"
        PSQL_DB   = "de8ie3tk2nmcs4"
        connstr = "host=%s port=%s user=%s password=%s dbname=%s" % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)
        conn = psycopg2.connect(connstr)
        cur = conn.cursor()
        sqlquery2 = "select * from informacionqr2 ORDER BY id DESC;"
        cur.execute(sqlquery2)
        row = cur.fetchone()
        username = row
        print(username)
        services = Service.objects.filter(title=1234)
    except:
        services = get_object_or_404(Service, id=23)
    return render(request, "services/services.html", {'services':services})