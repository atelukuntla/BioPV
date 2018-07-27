from django.shortcuts import render
import xml.etree.ElementTree as ET
# from lxml import etree
import csv, io


def ratings_search(request):
    return render(request, 'ratings/ratings_search.html')


def ratings_compare(request):
    return render(request, 'ratings/ratings_compare.html')


def ratings_reporting(request):
    return render(request, 'ratings/ratings_reporting.html')


def ratings_add_module(request):
    return render(request, 'ratings/ratings_add_module.html')


def insert_data(request):
    return render(request, 'ratings/ratings_add_module.html', {'message': 'Information saved successfully'})


def upload_xml(request):
    xmlfile = request.FILES['xml_file']
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    for child in root:
        print(child.tag, child.attrib)
    return render(request, 'ratings/ratings_add_module.html', {'message': 'XML file uploaded successfully'})


def upload_csv(request):
    csv_file = request.FILES['csv_file']
    decoded_file = csv_file.read().decode('utf-8')
    io_string = io.StringIO(decoded_file)
    for line in csv.reader(io_string, delimiter=';', quotechar='|'):
        print(line)
    return render(request, 'ratings/ratings_add_module.html', {'message': 'CSV file uploaded successfully'})
