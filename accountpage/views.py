from django.shortcuts import render

from django.shortcuts import redirect #much better than return index(request) since No paramter collision
from .forms import forms, PatientForm, DoctorForm, UserForm
from .models import  Doctor, Patient
from django.contrib.auth.models import User
# Create your views here.



def getUser(request): #Get user page with info to edit
	'''
	print("Getting user maybe")
	print(request.session['id'])
	print(request.session['user_type'])
	'''
	try: #avoid invalid id error
		if (request.session['user_type']=='1'):
			p = User.objects.get(id=request.session['id'])
			user = Doctor.objects.get(user=p)
			form = DoctorForm(instance=user)
			# form= UserForm(instance=p)
			# print("doctor: ", user)
		elif (request.session['user_type']=='0'):
			p = User.objects.get(id=request.session['id'])
			user = Patient.objects.get(user=p)
			form = PatientForm(instance=user)

		else:
			return redirect('/')
		# global doctorselected
		# doctorselected=False
		form.fields['status'].widget = forms.HiddenInput()

		if request.method == 'POST': #Edit User (editUser)
			if request.session['user_type']=='1':
				form = DoctorForm(request.POST, instance=user)
			elif request.session['user_type']=='0':
				form = PatientForm(request.POST, instance=user)
			# else:
			# 	return redirect('/')
			# user.save()
			# p.save()
			if form.is_valid():
				form.save()
				form.fields['status'].widget = forms.HiddenInput()
				return render(request, 'account.html', {'form': form, 'id':request.session['id'], 'isdoctor':request.session['user_type'] } ) #NOTE: VARIABLES IN HTML CANNOT START WITH '_' SO NO "_id"
			else:
				print('form is not valid',form.errors, form.cleaned_data)
				return render(request, 'account.html', {'form': form, 'id':request.session['id'], 'isdoctor':request.session['user_type'] } )

		else: # See User data. Logically renders first since first accessed thorugh GET
			return render(request, 'account.html', {'form': form, 'id':request.session['id'], 'isdoctor':request.session['user_type'] } )
	except:
		print("Exception occurring")
		return redirect('/')

def deleteUser(request): #API that renders back index
	try: #avoid invalid id error
		if request.session['user_type']=='1':
			p = User.objects.get(id=request.session['id'])
			user = Doctor.objects.get(user=p)
		elif request.session['user_type']=='0':
			p = User.objects.get(id=request.session['id'])
			user = Patient.objects.get(user=p)
		else:
			return redirect('/')	

		print("Deleting user")
		user.delete()
		p.delete()
		request.session['id'] = None #sets isLoggedin=False in homepage
	except:
		print("Error happening deleting user")
		pass

	return redirect('/') #also returns updated request session params so good
