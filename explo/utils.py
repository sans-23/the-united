import numpy as np
#import matplotlib.pyplot as plt

def pfiner(mass_retained, total_mass):
    cumulative_retained = []
    percentage_finer = []

    j=0
    for i in range(0,len(mass_retained)):
        j+=mass_retained[i]
        cumulative_retained.append(j)

    for a in cumulative_retained:
        percentage_finer.append(100 - (a/total_mass)*100.0)

    return percentage_finer

def util(a, target):
  if target>a[0]:
    return 100
  elif target<a[-1]:
    return -1
  for i in range(len(a)):
    if a[i]<=target:
      return i

def USCS_COARSE(finer4, finer200, Cu, Cc, PI, LL, clay, dc):

  if dc == True:
    silt = finer200 - clay

  if finer4 > 50:
    if finer200>=0 and finer200<=5 :
      if Cu>6 and (Cc>1 and Cc<3):
        return 'SW'
      else:
        return 'SP'
    elif finer200>5 and finer200<=12:
      #Dual Classification
      if dc == False:
        return 'DUALS'
      else:
        if clay > silt:
          if Cu>6 and (Cc>1 and Cc<3):
            return 'SW-SC'
          else:
            return 'SP-SC'
        else:
          if Cu>6 and (Cc>1 and Cc<3):
            return 'SW-SM'
          else:
            return 'SP-SM'
    elif finer200>12 and finer200<50 :
      if PI > 0.73*(LL-20):
        return 'SC'
      else:
        return 'SM'
  else:
    if finer200>=0 and finer200<=5 :
      if Cu>4 and (Cc>1 and Cc<3):
        return 'GW'
      else:
        return 'GP'
    elif finer200>5 and finer200<=12:
      #Dual Classification
      if dc == False:
        return 'DUALG'
      else:
        if clay > silt:
          if Cu>4 and (Cc>1 and Cc<3):
            return 'GW-GC'
          else:
            return 'GP-GC'
        else:
          if Cu>4 and (Cc>1 and Cc<3):
            return 'GW-GM'
          else:
            return 'GP-GM'

    elif finer200>12 and finer200<=50 :
      if PI > 0.73*(LL-20):
        return 'GC'
      else:
        return 'GM'

def USCS_FINE(PI, LL):
  if LL>50:
    if PI > 0.73*(LL-20):
      return 'CH'
    else:
      return 'MH'
  else:
    if PI > 0.73*(LL-20):
      return 'CL'
    else:
      return 'ML'

USCS_NAMES = {'SW': 'Well-graded sand',
              'SP': 'Poorly-graded sand',
              'SP-SM': 'Poorly-graded sand with silt',
              'SP-SC': 'Poorly-graded sand with clay',
              'SW-SM': 'Well-graded sand with silt',
              'SW-SC': 'Well-graded sand with clay',
              'SC': 'Clayey sand',
              'SM': 'Silty sand',
              'GW': 'Well-graded gravel',
              'GP': 'Poorly-graded gravel',
              'GP-GM': 'Poorly-graded gravel with silt',
              'GP-GC': 'Poorly-graded gravel with clay',
              'GW-GM': 'Well-graded gravel with silt',
              'GW-GC': 'Well-graded gravel with clay',
              'GC': 'Clayey gravel',
              'GM': 'Silty gravel',
              'CH': 'Fat clay',
              'MH': 'Elastic clay',
              'CL': 'Lean clay',
              'ML': 'Lean silt',
              'DUALG': 'GP-GM GP-GC GW-GM GW-GC',
              'DUALS': 'SP-SM SP-SC SW-SM SW-SC',
              'ERROR': 'Insufficient data'}

def explosans(sieve, A, LL=42, PI=18):

  for i in range(len(A)-1):
    if A[i]<A[i+1]:
        return {'USCS_ABBR': 'ERROR' , 'USCS_NAME': 'Bad Data'}

  dual_classification = True

  i4   = util(sieve, 4.75)
  i200 = util(sieve, 0.075)
  i200 = util(sieve, 0.075)
  iclay = util(sieve, 0.002)
  i60  = util(A, 60)
  i30  = util(A, 30)
  i10  = util(A, 10)

  if sieve[0] == 4.75:
    finer4 = A[0]
  else:
    finer4   = 100 if i4==100 else np.interp(4.75, np.flipud(sieve[i4-1:i4+1]), np.flipud(A[i4-1: i4+1]))
  finer200 = 100 if i200==100 else np.interp(0.075, np.flipud(sieve[i200-1:i200+1]), np.flipud(A[i200-1: i200+1]))
  clay     = -1 if iclay==-1 else np.interp(0.002, np.flipud(sieve[iclay-1:iclay+1]), np.flipud(A[iclay-1: iclay+1]))

  if clay == -1 :
    dual_classification = False

  if finer200 >= 50:
    abbr = USCS_FINE(PI, LL)
    return {'USCS_ABBR': abbr , 'USCS_NAME': USCS_NAMES[abbr]}
  else:
    retained200 = 100 - finer200 #total coarse soil
    retained4 = 100 - finer4 #total gravel

    percentage_gravel = (retained4/retained200)*100
    finer4 = percentage_gravel

    try:
      D60 = np.interp(60, np.flipud(A[i60-1:i60+1]), np.flipud(sieve[i60-1: i60+1]))
      D30 = np.interp(30, np.flipud(A[i30-1:i30+1]), np.flipud(sieve[i30-1: i30+1]))
      D10 = np.interp(10, np.flipud(A[i10-1:i10+1]), np.flipud(sieve[i10-1: i10+1]))
      Cu  = D60/D10
      Cc  = (D30*D30)/(D10*D60)
      print('Cu =', Cu)
      print('Cc =', Cc)
      abbr = USCS_COARSE(finer4, finer200, Cu, Cc, PI, LL, clay, dual_classification)
      return {'USCS_ABBR': abbr , 'USCS_NAME': USCS_NAMES[abbr], 'Cu':Cu, 'Cc':Cc}
    except:
      return {'USCS_ABBR': 'ERROR' , 'USCS_NAME': 'Insufficient data'}

