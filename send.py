import smtplib
import generate
import config
import gapps

def main():
    gc = gapps.get_client()
    sheet = gc.open(config.GDOCS_NAME)
    worksheet = sheet.worksheet(config.GDOCS_WORKSHEET)

    email_col = generate.spr_keys.index('email')+1
    body_col = generate.spr_keys.index('body')+1
    subject_col = generate.spr_keys.index('subject')+1
    status_col = generate.spr_keys.index('status')+1       

    for row in xrange(2, 101):
        status = worksheet.cell(row, status_col).value
        email = worksheet.cell(row, email_col).value
        body = worksheet.cell(row, body_col).value
        subject = worksheet.cell(row, subject_col).value        

        if email and body and subject and not status:
            send_email(email, '%s <%s>' % (config.EMAIL_FROM_NAME, config.EMAIL_FROM_ADDRESS), body.strip(), subject, config.EMAIL_TO_SALESFORCE)
            worksheet.update_cell(row, status_col, 'Sent')
            break
def send_email(to, sender, msg, subject, bcc=None):
    server = smtplib.SMTP(config.EMAIL_HOST, config.EMAIL_PORT)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(config.EMAIL_HOST_USER, config.EMAIL_HOST_PASSWORD)

    subject = subject.replace('\n', '')
    header = 'To:' + to + '\n' + 'From: ' + sender + '\n' + 'Subject:' + subject + '\n'
    print header
    msg = header + '\n' + msg + '\n\n'
    server.sendmail(sender, [to, bcc], msg)
    print 'done!'
    server.close()
    
    print 1

if __name__ == "__main__":
    main()
