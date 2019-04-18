from django.shortcuts import render
from django.views.generic import (
	View, TemplateView, ListView, DetailView,
	CreateView, UpdateView, DeleteView,
)
from django.urls import reverse_lazy
from CVB.models import School, Student
# Create your views here.
class IndexView(View):
	def get(self, request):
		return render(request, 'CVB/index.html', {
			'index_injection': 'HOME PAGE'
		})

class AboutView(TemplateView):
	template_name = 'CVB/about.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['about_injection']='ABOUT US'
		return context

class SchoolListView(ListView):
	context_object_name = 'schools'
	model = School

class SchoolDetailView(DetailView):
	context_object_name = 'school_detail'
	model = School
	template_name = 'CVB/school_details.html'

class SchoolCreateView(CreateView):
	fields=('name', 'principal', 'location')
	model = School

class SchoolUpdateView(UpdateView):
	fields=('name', 'principal')
	model = School

class SchoolDeleteView(DeleteView):
	model = School
	# this code will execute after action from the delete button
	success_url = reverse_lazy('CVB:school_list')

class StudentCreateView(CreateView):
	fields = ['name', 'age']
	model = Student

	def form_valid(self, form):
		form.instance.school = School.objects.get(id=self.kwargs.get('pk'))
		return super(StudentCreateView, self).form_valid(form)

class StudentUpdateView(UpdateView):
	fields = ['school', 'name', 'age']
	model = Student

	def form_valid(self, form):
		form.instance.student = Student.objects.get(id=self.kwargs.get('pk'))
		return super(StudentUpdateView, self).form_valid(form)

class StudentDeleteView(DeleteView):
	model = Student

	def get_success_url(self):
		pk = self.kwargs['pk']
		obj = Student.objects.get(pk=pk)
		return reverse_lazy('CVB:detail', kwargs={'pk':obj.school.pk})