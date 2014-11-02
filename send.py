import smtplib
import generate
import config

def main():

    spr = generate.get_spreadsheet_client()
    wid = generate.get_worksheet_id_by_title(spr, config.GDOCS_SPREADSHEET_KEY, config.GDOCS_WORKSHEET)

    email_col = generate.spr_keys.index('email')+1
    body_col = generate.spr_keys.index('body')+1
    subject_col = generate.spr_keys.index('subject')+1
    status_col = generate.spr_keys.index('status')+1       

    for row in xrange(2, 101):
        status = spr.GetCellsFeed(config.GDOCS_SPREADSHEET_KEY, wid, "R"+str(row)+"C"+str(status_col)).content.text
        email = spr.GetCellsFeed(config.GDOCS_SPREADSHEET_KEY, wid, "R"+str(row)+"C"+str(email_col)).content.text
        body = spr.GetCellsFeed(config.GDOCS_SPREADSHEET_KEY, wid, "R"+str(row)+"C"+str(body_col)).content.text
        subject = spr.GetCellsFeed(config.GDOCS_SPREADSHEET_KEY, wid, "R"+str(row)+"C"+str(subject_col)).content.text

        if email and body and subject and not status:
            send_email(email, '%s <%s>' % (config.EMAIL_FROM_NAME, config.EMAIL_FROM_ADDRESS), body.strip(), subject, config.EMAIL_TO_SALESFORCE)
            spr.UpdateCell(row, status_col, 'Sent', config.GDOCS_SPREADSHEET_KEY, wid)
            
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
