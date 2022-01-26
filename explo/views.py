from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import utils
import numpy as np
import math

@login_required(login_url='/')
def sans(request):
    sieve1 = [63.0, 4.75, 2.00, 1.40, 1.00, 0.50, 0.25, 0.125, 0.075, 0.063, 0.020, 0.004, 0.002, 0.001]
    sieve2 =  [63.0, 20.0, 6.3, 2.0, 0.6, 0.212, 0.063, 0.020, 0.006, 0.002]
    return render(request, 'explo/form.html',{'sieve1':sieve1, 'sieve2':sieve2 })

@login_required(login_url='/')
def classifysoil(request):
    if request.method == 'POST':
        sieve1 = [63.0, 4.75, 2.00, 1.40, 1.00, 0.50, 0.25, 0.125, 0.075, 0.063, 0.020, 0.004, 0.002, 0.001]
        sieve2 =  [63.0, 20.0, 6.3, 2.0, 0.6, 0.212, 0.063, 0.020, 0.006, 0.002]
        percentage_finer = []
        sieve = []
        userinput = []
        additional = {}

        if request.POST.get('set') == 'a':
            for i in range(13):
                id = str(i)
                if request.POST.get(id) != '':
                    sieve.append(sieve1[i])
                    userinput.append(float(request.POST.get(id)))
        else :
            for i in range(10):
                id = str(i)
                if request.POST.get(id) != '':
                    sieve.append(sieve2[i])
                    userinput.append(float(request.POST.get(id)))

        if request.POST.get('total_mass') != '':
            total_mass  = float(request.POST.get('total_mass'))
        else:
            if request.POST.get('option1') == '2' or request.POST.get('option2') == '2':
                total_mass = sum(userinput)

        if request.POST.get('option1') == '1' or request.POST.get('option2') == '1':
            percentage_finer = userinput
        else :
            percentage_finer = utils.pfiner(userinput, total_mass)

##########################################################################################################################################################

        if sieve[0] < 4.75 :
            additional['gravel']= 'Can not be determined'
        else:
            i = utils.util(sieve, 4.75)
            k   = np.interp(4.75, np.flipud(sieve[i-1:i+1]), np.flipud(percentage_finer[i-1: i+1]))
            additional['gravel'] = 100 - k

###########################################################################################################################################################

        if sieve[0] < 2.00 :
            additional['coarsesand']= 'Can not be determined'
        else:
            i = utils.util(sieve, 2.00)
            k   = np.interp(2.00, np.flipud(sieve[i-1:i+1]), np.flipud(percentage_finer[i-1: i+1]))
            if additional['gravel'] == 'Can not be determined':
                additional['coarsesand']= 100 - k
            else:
                additional['coarsesand']= (100 - k) - additional['gravel']

############################################################################################################################################################

        if sieve[0] < 0.425:
            additional['mediumsand']= 'Can not be determined'
        else:
            i = utils.util(sieve, 0.425)
            k   = np.interp(0.425, np.flipud(sieve[i-1:i+1]), np.flipud(percentage_finer[i-1: i+1]))
            if additional['coarsesand']== 'Can not be determined':
                additional['mediumsand'] = 100 - k
            else:
                additional['mediumsand'] = (100 - k) -  additional['coarsesand']

############################################################################################################################################################

        if sieve[0] < 0.075:
            additional['finesand'] = 'Can not be determined'
            additional['silt'] = percentage_finer[0]
        else:
            i = utils.util(sieve, 0.075)
            k   = np.interp(0.075, np.flipud(sieve[i-1:i+1]), np.flipud(percentage_finer[i-1: i+1]))
            if additional['mediumsand']== 'Can not be determined':
                additional['finesand'] = 100 - k
                additional['silt'] = k
            else:
                additional['finesand'] = (100 - k) - additional['mediumsand']
                additional['silt'] = k


        S = []
        for i in sieve:
            S.append(math.log(i))

        data = utils.explosans(sieve, percentage_finer)
        zipper = zip(sieve, percentage_finer)

        return render(request, 'explo/sans.html', {'data':data, 'sieve':S, 'A': percentage_finer, 'zipper': zipper, 'add': additional})
    else:
        return redirect('sans:sans')