import config
import gapps

spr_keys = ['name', 'email', 'body', 'subject', 'status']

def get_worksheet_id_by_title(spr_client, spreadsheet_key, title):
    for worksheet in spr_client.GetWorksheetsFeed(key=spreadsheet_key).entry:
        if worksheet.title.text == title:
            return worksheet.id.text.rsplit('/', 1)[1]   

def fill_subject(name):
    if '%s' in config.SUBJECT:
        return config.SUBJECT % name.split()[0]
    return config.SUBJECT

def fill_body(name):
    if config.USE_FULL_NAME:
        fill_name = name
    else:
        fill_name = name.split()[0]
    return (config.BODY % fill_name).strip()

def add_row(spr, row, article, wid):
    for col, key in enumerate(spr_keys):
        spr.UpdateCell(row, col+1, article.get(key, ''), config.GDOCS_SPREADSHEET_KEY, wid)

    print article

def main():
    gc = gapps.get_client()
    sheet = gc.open(config.GDOCS_NAME)
    worksheet = sheet.worksheet(config.GDOCS_WORKSHEET)
    
    name_col = spr_keys.index('name')+1
    body_col = spr_keys.index('body')+1
    subject_col = spr_keys.index('subject')+1

    for row in xrange(2, config.GDOCS_MAX_ROWS):
        name = worksheet.cell(row, name_col).value
        print name

        if not name:
            continue
        
        worksheet.update_cell(row, subject_col, fill_subject(name))
        worksheet.update_cell(row, body_col, fill_body(name))
    
if __name__ == "__main__":
    main()

