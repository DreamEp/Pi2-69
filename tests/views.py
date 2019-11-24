from django.shortcuts import render, get_object_or_404
from .forms import TestForm, PassTestForm, TestMcqForm, PassTestMcqForm
from .models import Test_end_session, Pass_test_end_session, Test_mcq_end_session, Pass_test_mcq_end_session


# Create your views here.
def test_create_view(request, *args, **kwargs):
	""" Show page which can then redirect toward standard and mcq creation pages """
	return render(request, 'manage_tests/test_create.html', {})


def test_standard_create_view(request):
	""" Show page to create a standard test (inputting text as answers) """
	form = TestForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = TestForm()

	context = {
		'form': form
	}
	return render(request, 'manage_tests/test_create_standard.html', context)


def test_mcq_create_view(request):
	""" Show page to create a mcq test (selecting a choice among others) """
	form = TestMcqForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = TestMcqForm()

	context = {
		'form': form
	}
	return render(request, 'manage_tests/test_create_mcq.html', context)


def test_display_view(request, input_id_test):
	""" Show page displaying a given test questions """
	# Retrieve and display the requested form
	form = get_object_or_404(Test_end_session, id_test=input_id_test)
	context = {
		'form': form
	}
	return render(request, 'manage_tests/test_display.html', context)


def test_pass_view(request, input_id_test):
	""" Show page displaying pass test with his questions """
	form_questions = get_object_or_404(Test_end_session, id_test=input_id_test)
	form_answers = PassTestForm(request.POST or None)
	form_answers.id_test = input_id_test

	#form_answers.id_student = ?

	if form_answers.is_valid():
		form_answers.save()

		# # Assess grade:
		# assessment = form_answers.assess_answer()

		# if not assessment['comment'] == 'pass':
		# 	# TODO: display indication to retry
		# 	form_answers = PassTestForm()
		# else:
		# 	# TODO: display indication that test is passed
		# 	form_answers = PassTestForm()

		form_answers = PassTestForm()

	context = {
		'form_answers': form_answers,
		'form_questions': form_questions
	}
	return render(request, 'pass_tests/test_pass.html', context)

	


def test_mcq_pass_view(request, input_id_test):
	form_questions = get_object_or_404(Test_mcq_end_session, id_test=input_id_test)
	form_answers = PassTestMcqForm(request.POST or None)
	#form_answers.id_student = ?

	if form_answers.is_valid():
		form_answers.save()

		# # Assess grade:
		# assessment = form_answers.assess_answer()

		# if not assessment['comment'] == 'pass':
		# 	# TODO: display indication to retry
		# 	form_answers = PassTestMcqForm()
		# else:
		# 	# TODO: display indication that test is passed
		# 	form_answers = PassTestMcqForm()

		form_answers = PassTestMcqForm()

	context = {
		'form_answers': form_answers,
		'form_questions': form_questions
	}
	return render(request, 'pass_tests/test_mcq_pass.html', context)



def tests_list_teacher_view(request):
	# List all the tests of the db
	tests_list_normal_questions = Test_end_session.objects.all()
	testlist_mcq = Test_mcq_end_session.objects.all()
	context = {
		'tests_list': tests_list_normal_questions,
		'tests_mcq_list': testlist_mcq
	}
	return render(request, 'manage_tests/tests_list_teacher.html', context)

def tests_list_student_view(request):
	# List all the tests of the db
	tests_list_normal_questions = Test_end_session.objects.all()
	testlist_mcq = Test_mcq_end_session.objects.all()
	context = {
		'tests_list': tests_list_normal_questions,
		'tests_mcq_list': testlist_mcq
	}
	return render(request, 'pass_tests/tests_list_student.html', context)


def tests_history_view(request):
	# Show the history of results
	queryset = Pass_test_end_session.objects.all() #TODO: transform query to get id_student only
	context = {
		'tests_list': queryset
	}
	return render(request, 'pass_tests/tests_history.html', context)

def tests_analysis_view(request):
	# Analysis of the students' results
	normal_test = Test_end_session.objects.all()
	#normal_test = Pass_test_end_session.objects.all().values('id_test').distinct()
	mcq_test = Pass_test_mcq_end_session.objects.all()
	context = {
		'tests_list_normal': normal_test,
		'tests_list_mcq': mcq_test
	}
	return render(request, 'manage_tests/tests_analysis.html', context)

def real_tests_analysis_view(request, input_id_test):
	# Analysis of the students' results
	test_list = Pass_test_end_session.objects.filter(id_test = input_id_test)
	context = {
		'test_list': test_list
	}
	return render(request, 'manage_tests/real_tests_analysis.html', context)


def test_mcq_display_view(request, input_id_pass_test):
	# Retrieve and display the requested mcq form
	form = get_object_or_404(Test_mcq_end_session, id_pass_test=input_id_pass_test)
	context = {
		'form': form
	}
	return render(request, 'manage_tests/test_mcq_display.html', context)

