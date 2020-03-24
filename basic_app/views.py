from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView)
# from django.http import HttpResponse
from django.urls import reverse_lazy
from basic_app import models

# Create your views here.


# def index(request):
#     return render(request, 'index.html')

# class CBView(View):
#     def get(self, request):
#         return HttpResponse('CBV Level Five')

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variable'] = 'BASIC INJECTION FOR THE VARIABLE'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools' #if not mentioned default will be school_list
    model = models.School
    template_name = 'basic_app/school_list.html'

class SchoolDetailView(DetailView):
    context_object_name = 'schools'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class StudentDetailView(DetailView):
    context_object_name = 'students'
    model = models.Student
    template_name = 'basic_app/student_detail.html'

class StudentListView(ListView):
    context_object_name = 'students'
    model = models.Student
    template_name = 'basic_app/student_list.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School
    # template_name = 'basic_app/school_create.html'

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School
    # template_name = 'basic_app/school_update.html'

class SchoolDeleteView(DeleteView):
    model = models.School
    context_object_name = 'school'
    success_url = reverse_lazy("basic_app:list")
    template_name = 'basic_app/school_delete.html'

class StudentCreateView(CreateView):
    fields = ('name','age','school')
    model = models.Student
    # template_name = 'basic_app/school_create.html'

class StudentUpdateView(UpdateView):
    fields = ('name','age','school')
    model = models.Student
    # template_name = 'basic_app/school_update.html'

class StudentDeleteView(DeleteView):
    model = models.Student
    context_object_name = 'student'
    success_url = reverse_lazy("basic_app:slist")
    template_name = 'basic_app/student_delete.html'
