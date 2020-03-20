import pandas as pd 
import numpy as np 


def read_dataframe(filepath):
    df = pd.read_csv(filepath)
return df 


def binary_output(df):
	df['readmitted'].replace('NO','otherwise', inplace = True)
	df['readmitted'].replace('>30','otherwise', inplace = True)
	df['readmitted'].replace('<30','readmitted', inplace = True)
return df
	
def easy_dummies(df):
	# dummify diabetes medication indicator
	df['diabetesMed'].replace('Yes',1, inplace = True)
	df['diabetesMed'].replace('No',0, inplace = True)

	# dummify change in diabetes medication indicator 
	df['change'].replace('Ch',1, inplace = True)
	df['change'].replace('No', 0, inplace = True)

	# dummify patient gender
	df['gender'].replace('Male',1,inplace = True)
	df['gender'].replace('Female',0, inplace = True)


def dummify_features(df):
	# bucket variables
	df['race'] = [x if x in ['Caucasian', 'AfricanAmerican'] else 'Other' for x in df['race']]
	df['age'] = ['[60, 100)' if x in ['[70-80)','[60-70)','[80-90)','[90-100)'] else 
	'[30, 60)' if x in ['[50-60)','[40-50)','[30-40)'] else 
	'<30' for x in df['age']]
	df['admission_source_id'] = ['Referral' if x in [1,2,3] else 'Emergency' if x == 7 else 'Other' for x in df['admission_source_id']]
	df['discharge_disposition_id'] = ['Home' if x in [1,6,8,13] else 'Expired' if x in [11,19,20,21] else "Other" for x in df['discharge_disposition_id']]
	# initiate buckets
	cardiology = ['Cardiology','Cardiology-Pediatric']
	generalpractice = ['Family/GeneralPractice']
	internalmedicine = ['InternalMedicine']
	surgery = ['Surgeon','Surgery-Cardiovascular','Surgery-Cardiovascular/Thoracic',
	'Surgery-Colon&Rectal','Surgery-General','Surgery-Maxillofacial','Surgery-Neuro',
	'Surgery-Pediatric','Surgery-Plastic','Surgery-PlasticwithinHeadandNeck','Surgery-Thoracic', 
	'Surgery-Vascular','SurgicalSpecialty']
	df['medical_specialty'] = ['Cardiology' if x in cardiology else
	'General Practice' if x in generalpractice else
	'Internal Medicine' if x in internalmedicine else
	'Surgery' if x in surgery else 
	'Missing' if x == '?' else 
	'Other' for x in df['medical_specialty']]
	#HA1C
	#diagnosis 




	race_dummy = pd.get_dummies(df['race'], prefix = 'race', drop_first = True)
	age_dummy = pd.get_dummies(df['age'], prefix = 'age', drop_first = True)
	admissions_dummy = pd.get_dummies(df['admission_source_id'], prefix = 'admissions', drop_first = True)
	discharge_dummy = pd.get_dummies(df['discharge_disposition_id'], prefix = 'discharge', drop_first = True)
	specialty_dummy = pd.get_dummies(df['medical_specialty'], prefix = 'specialty', drop_first = True)

medications = ['metformin', 'repaglinide', 'nateglinide', 'chlorpropamide',
       'glimepiride', 'acetohexamide', 'glipizide', 'glyburide', 'tolbutamide',
       'pioglitazone', 'rosiglitazone', 'acarbose', 'miglitol', 'troglitazone',
       'tolazamide', 'insulin',
       'glyburide-metformin', 'glipizide-metformin',
       'glimepiride-pioglitazone', 'metformin-rosiglitazone',
       'metformin-pioglitazone']

def med_eda(df):
	med_eda = df[medications]
	med_dummy = pd.get_dummies(med_eda, columns = medications, drop_first = True)





def drop_columns(): 
	# drop rows
	df = df[df['gender'] != 'Unknown/Invalid'] # drop unknown gender values
	df = df[df['discharge_disposition_id'] != 'Expired'] # drop 'Expired' (death)

	# drop columns
	df.drop(columns = ['admission_type_id', 'weight', 'payer_code','examide', 'citoglipton'], inplace = True)






