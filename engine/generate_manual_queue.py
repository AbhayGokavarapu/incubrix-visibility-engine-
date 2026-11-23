import csv

def generate_manual_queue():
    with open('FULL_QUESTION_PROVIDER_DAY_MATRIX.csv', 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    pending_items = []
    for r in rows:
        qid = r['Question_ID']
        qtext = r['Question_Text']
        mkt = r['Market']
        
        for prov in ['chatgpt', 'claude', 'perplexity']:
            col_name = f"{prov.capitalize()}_Web_Status" if prov != 'chatgpt' else "ChatGPT_Web_Status"
            st = r.get(col_name, "")
            if 'PENDING' in st:
                pending_items.append({
                    "priority": int(qid[1:]),
                    "question_id": qid,
                    "market": mkt,
                    "provider": prov,
                    "question_text": qtext,
                    "cli_command": f'python -m engine.manual_importer --question-id {qid} --provider {prov} --market {mkt} --text "<PASTE_ANSWER>" --citations "<URL1>" "<URL2>"'
                })

    with open('MANUAL_ASSISTANT_COLLECTION_QUEUE.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Priority_Order', 'Question_ID', 'Market', 'Target_Assistant', 'Question_Text', 'CLI_Import_Template'])
        for item in pending_items:
            writer.writerow([item['priority'], item['question_id'], item['market'], item['provider'], item['question_text'], item['cli_command']])

    print(f"Manual collection queue generated: MANUAL_ASSISTANT_COLLECTION_QUEUE.csv ({len(pending_items)} pending items)")

if __name__ == "__main__":
    generate_manual_queue()
