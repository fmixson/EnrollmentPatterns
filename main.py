import pandas as pd
import openpyxl
import matplotlib as mpl
import matplotlib.pyplot as plt

enrollmentPattern_df = pd.read_csv('D:\Work\Data\LA_Division\WeeklyEnrollmentSheets\Liberal Arts.csv')
enrollmentPattern_df['Enrollment Add Date'] = pd.to_datetime(enrollmentPattern_df['Enrollment Add Date'])
# print(enrollmentPattern_df)
enrollmentSubset = enrollmentPattern_df[['Enrollment Add Date', 'Session Code']]
print(enrollmentSubset)
regularSession = enrollmentSubset[enrollmentSubset['Session Code'] == '1']
session15B = enrollmentSubset[enrollmentSubset['Session Code'] == '15B']
print(regularSession)
print(session15B)
regularSession = regularSession.groupby('Enrollment Add Date').count()
session15B = session15B.groupby('Enrollment Add Date').count()
regularSessionFlat = regularSession.reset_index()
session15BFlat = session15B.reset_index()
regularSessionFlat.loc[0, 'cumEnrollment'] = 0
session15BFlat.loc[0, '15BcumEnrollment'] = 0
regularSessionFlat.loc[1, 'cumEnrollment'] = regularSessionFlat.loc[0, 'Session Code'] + regularSessionFlat.loc[1, 'Session Code']
session15BFlat.loc[1, '15BcumEnrollment'] = session15BFlat.loc[0, 'Session Code'] + session15BFlat.loc[1, 'Session Code']
for i in range(1, len(regularSessionFlat)-1):
     regularSessionFlat.loc[i+1, 'cumEnrollment'] = regularSessionFlat.loc[i, 'cumEnrollment'] + regularSessionFlat.loc[i+1, 'Session Code']
for i in range(1, len(session15BFlat)-1):
     session15BFlat.loc[i+1, '15BcumEnrollment'] = session15BFlat.loc[i, '15BcumEnrollment'] + session15BFlat.loc[i+1, 'Session Code']

cum15Benrollment = session15BFlat['15BcumEnrollment']
regularSessionFlat = regularSessionFlat.join(cum15Benrollment)
regularSessionFlat.loc[0, 'Available Seats'] = 5000
regularSessionFlat['Available Seats'] = 6000 - regularSessionFlat.cumEnrollment
# regularSessionFlat.set_index('Enrollment Add Date')
print(regularSessionFlat)
# print(session15BFlat)
# regularSessionFlat.plot([['cumEnrollment', '15BcumEnrollment']], kind='line')
plt.plot(regularSessionFlat['cumEnrollment'])
plt.plot(regularSessionFlat['15BcumEnrollment'])
plt.plot(regularSessionFlat['Available Seats'])
plt.plot()



plt.show()


# print(regularSession)
# sorted_df = enrollmentPattern_df.sort_values('Enrollment Add Date')


# regularSession_df = regularSession[['Enrollment Add Date, Term']]

regularSession.to_excel('RegularSessionEnrollment.xlsx')
# major_df = enrollmentPattern_df(['Enrollment Add Date']), ['Session Code'].count()
# major_df['Enrollment Add Date'] = pd.to_datetime(major_df['Enrollment Add Date'])
# print(major_df)
# groupedAddDate_df = major_df.groupby(['Enrollment Add Date'])['Session Code'].count()
# print(groupedAddDate_df)