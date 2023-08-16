import smtplib

conn = smtplib.SMTP('smtp.gmail.com',587)
type(conn)
conn.ehlo()
conn.starttls()
conn.login('Email ID','password')
#conn.sendmail(sender, receivers, 'Subject: This is an e-mail subject.\n\n This is some content. ' + str(num))
conn.sendmail('from','CcBcc','Subject:')
conn.quit()
