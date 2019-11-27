from django.db import models
from django.urls import reverse

# Create your models here.

## Standard tests ##

class Test_end_session(models.Model):
	"""
	Model for the tests:
	TODO: how to make a dynamic number of questions
	"""
	id_test = models.CharField(max_length=10, null=False, primary_key=True)
	title = models.CharField(max_length=50)
	q1 = models.TextField()
	a1 = models.TextField()
	q2 = models.TextField()
	a2 = models.TextField()
	q3 = models.TextField()
	a3 = models.TextField()
	q4 = models.TextField()
	a4 = models.TextField()
	q5 = models.TextField()
	a5 = models.TextField()
	q6 = models.TextField()
	a6 = models.TextField()
	q7 = models.TextField()
	a7 = models.TextField()
	q8 = models.TextField()
	a8 = models.TextField()
	q9 = models.TextField()
	a9 = models.TextField()
	q10 = models.TextField()
	a10 = models.TextField()


	def get_absolute_url(self):
		# dynamic (if 'my_app' is renamed in the url, it will adapt)
		return reverse('tests:Display test', kwargs={'input_id_test': self.id_test})


class Pass_test_end_session(models.Model):
	"""
	Model for the students records of passing the test
	"""
	id_pass_test = models.CharField(max_length=10, primary_key=True)
	id_test = models.ForeignKey(Test_end_session, on_delete=models.CASCADE)
	id_student = models.CharField(max_length=10, null=False)
	#question = models.TextField()
	q1 = models.TextField()
	q2 = models.TextField()
	q3 = models.TextField()
	q4 = models.TextField()
	q5 = models.TextField()
	q6 = models.TextField()
	q7 = models.TextField()
	q8 = models.TextField()
	q9 = models.TextField()
	q10 = models.TextField()

	def get_absolute_url(self):
		return reverse('tests:Display test', kwargs={'input_id_pass_test': self.id_pass_test})

	class Meta:
		unique_together = ('id_pass_test', 'id_student')

	def test_dumb_id_student_not_admin(self):
		if not self.id_student == 'admin':
			return True
		else:
			return False



## Multiple tests ##

class Test_mcq_end_session(models.Model):
	"""
	Model for the tests_mcq_end_session:
	TODO: how to make a dynamic number of questions
	"""
	id_test = models.CharField(max_length=10, primary_key=True)
	title = models.CharField(max_length=50)
	id_q = models.IntegerField(null=False)
	question = models.CharField(max_length=50, null=False)
	Choice_num = models.IntegerField(null=False)
	Choice_num_exp = models.IntegerField(null=False)
	Choice_text_correspnd = models.TextField()

	def get_absolute_url(self):
		return reverse('tests:Display mcq test', kwargs={'input_id_test': self.id_test})

	def __str__(self):
		# dic_table = {
		# 	'id_test': self.id_test,
		# 	'id_q': self.id_q,
		# 	'title': self.title,
		# 	'question': self.question,
		# 	'Choice_num': self.Choice_num,
		# 	'Choice_num_exp': self.Choice_num_exp,
		# 	'Choice_text_correspnd': self.Choice_text_correspnd
		# }

		str_table = """
		id_test: {0};\n
		id_q: {1};\n
		title: {2};\n
		question: {3};\n
		""".format(
			self.id_test,
			self.id_q,
			self.title,
			self.question,
			)

		return str_table

	class Meta:
		unique_together = ('id_test', 'id_q')



class Pass_test_mcq_end_session(models.Model):
	"""
	Model for the students records of passing the test
	"""
	id_pass_test = models.CharField(max_length=10, primary_key=True)
	id_test = models.ForeignKey(Test_mcq_end_session, on_delete=models.CASCADE)
	id_student = models.CharField(max_length=10, null=False)
	id_q = models.IntegerField(null=False)
	input_Choice_num = models.IntegerField(null=False)

	def get_absolute_url(self):
		return reverse('tests:Display mcq test', kwargs={'input_id_pass_test': self.id_pass_test})

	class Meta:
		unique_together = ('id_pass_test', 'id_student', 'id_q')


class Mark:
    counter = 0

    def increment(self):
        self.counter += 1
        return ''

    def decrement(self):
        self.counter -= 1
        return ''

    def double(self):
        self.counter *= 2
        return ''
		
    def init(self):
	    self.counter = 0
	    return ''

# Normalized implementation

"""class Test(models.Model):
	id_test = models.CharField(max_length=12, primary_key=True)
	name = models.CharField(max_length=20)
	description = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.id_test"""

class Test(models.Model):
	title = models.CharField(max_length=64)
	def __str__(self):
		return self.title

class PassTest(models.Model):
	id_student = models.CharField(max_length=10, null=False)
	id_test = models.ForeignKey(Test, on_delete=models.CASCADE)
	def __str__(self):
		return self.id_student


"""class Question(models.Model):
	id_test = models.ForeignKey(Test, on_delete=models.CASCADE)
	id_question = models.CharField(max_length=12, primary_key=True)
	question_text = models.CharField(max_length=200)

	def __str__(self):
		output = "{}, {}".format(self.id_test, self.id_question)
		return output"""

class Question(models.Model):
	id_test = models.ForeignKey(Test, on_delete=models.CASCADE)
	question_text = models.CharField(max_length=200)
	def __str__(self):
		return self.question_text


"""class Choice(models.Model):
	id_test = models.ForeignKey(Test, on_delete=models.CASCADE)
	id_question = models.ForeignKey(Question, on_delete=models.CASCADE)
	id_choice = models.CharField(max_length=12, primary_key=True)
	choice_text = models.CharField(max_length=200)
	is_correct = models.BooleanField(default=False)

	def __str__(self):
		output = "{}, {}, {}".format(self.id_test, self.id_question, self.id_Choice)
		return output"""

class Choice(models.Model):
	id_question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	check_button = models.BooleanField(blank = True, default=False)
	def __str__(self):
		return self.choice_text		

"""
class Score(models.Model):
	score = models.IntegerField(default=0)
	id_user = models.ForeignKey(User, on_delete=models.CASCADE)
	id_test = models.ForeignKey(Test, on_delete=models.CASCADE)
	start_time = models.CharField(max_length=64)
	end_time = models.CharField(max_length=64)
	def __str__(self):
		return self.test.title"""
