import config
import gdata
import gdata.spreadsheet.service

spr_keys = ['name', 'email', 'body', 'subject', 'status']

def get_spreadsheet_client():
    spr_client = gdata.spreadsheet.service.SpreadsheetsService()
    spr_client.email = config.GDOCS_USERNAME
    spr_client.password = raw_input('GDocs Password:')
    spr_client.source = 'SaaS Metrics Python Program'
    spr_client.ProgrammaticLogin()
    return spr_client

def get_worksheet_id_by_title(spr_client, spreadsheet_key, title):
    for worksheet in spr_client.GetWorksheetsFeed(key=spreadsheet_key).entry:
        if worksheet.title.text == title:
            return worksheet.id.text.rsplit('/', 1)[1]   

def fill_subject(name):
    if '%s' in config.SUBJECT:
        return config.SUBJECT % name.split()[0]
    return config.SUBJECT

def fill_body(name):
    return (config.BODY % name.split()[0]).strip()

def add_row(spr, row, article, wid):
    for col, key in enumerate(spr_keys):
        spr.UpdateCell(row, col+1, article.get(key, ''), config.GDOCS_SPREADSHEET_KEY, wid)

    print article

def main():
    spr = get_spreadsheet_client()
    wid = get_worksheet_id_by_title(spr, config.GDOCS_SPREADSHEET_KEY, config.GDOCS_WORKSHEET)

    name_col = spr_keys.index('name')+1
    body_col = spr_keys.index('body')+1
    subject_col = spr_keys.index('subject')+1

    for row in xrange(2, config.GDOCS_MAX_ROWS):
        name = spr.GetCellsFeed(config.GDOCS_SPREADSHEET_KEY, wid, "R"+str(row)+"C"+str(name_col)).content.text

        if not name:
            continue
        
        spr.UpdateCell(row, subject_col, fill_subject(name), config.GDOCS_SPREADSHEET_KEY, wid)
        spr.UpdateCell(row, body_col, fill_body(name), config.GDOCS_SPREADSHEET_KEY, wid)        
    
if __name__ == "__main__":
    main()
