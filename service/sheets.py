from octopus.lib import clcsv

class ScoreSheet(clcsv.SheetWrapper):

    HEADERS = {
        "Journal Name" : "journal_name",
        "Journal URL" : "journal_url",
        "Reader Rights Score" : "reader_rights_score",
        "Reader Rights URL" : "reader_rights_url",
        "Reader Rights Relevant Text" : "reader_rights_relevant_text",
        "Reuse Rights Score" : "reuse_rights_score",
        "Reuse Rights URL" : "reuse_rights_url",
        "Reuse Rights Relevant Text" : "reuse_rights_relevant_text",
        "Copyrights Score" : "copyrights_score",
        "Copyrights URL" : "copyrights_url",
        "Copyrights Relevant Text" : "copyrights_relevant_text",
        "Author Posting Rights Score" : "author_posting_rights_score",
        "Author Posting Rights URL" : "author_posting_rights_url",
        "Author Posting Rights Relevant Text" : "author_posting_rights_relevant_text",
        "Automatic Posting Rights Score" : "automatic_posting_rights_score",
        "Automatic Posting Rights URL" : "automatic_posting_rights_url",
        "Automatic Posting Rights Relevant Text" : "automatic_posting_rights_relevant_text",
        "Machine Readability Score" : "machine_readability_score",
        "Machine Readability URL" : "machine_readability_url",
        "Machine Readability Relevant Text"  : "machine_readability_relevant_text",
        "APC Price" : "apc_price",
        "Funder Policy URL" : "funder_policy_url",
        "SHERPA/RoMEO URL" : "romeo_url",
        "ISSN" : "issn",
        "E-ISSN" : "eissn",
        "Total Score" : "total",
        "Publisher" : "publisher",
        "Publisher Contact Date" : "publisher_contact_date",
        "Score Locked Date" : "score_locked_date"
    }

    EMPTY_STRING_AS_NONE = True

    OUTPUT_ORDER = [
        "issn",
        "eissn",
        "journal_name",
        "journal_url",
        "reader_rights_score",
        "reader_rights_url",
        "reader_rights_relevant_text",
        "reuse_rights_score",
        "reuse_rights_url",
        "reuse_rights_relevant_text",
        "copyrights_score",
        "copyrights_url",
        "copyrights_relevant_text",
        "author_posting_rights_score",
        "author_posting_rights_url",
        "author_posting_rights_relevant_text",
        "automatic_posting_rights_score",
        "automatic_posting_rights_url",
        "automatic_posting_rights_relevant_text",
        "machine_readability_score",
        "machine_readability_url",
        "machine_readability_relevant_text",
        "apc_price",
        "funder_policy_url",
        "romeo_url",
        "issn",
        "eissn",
        "total",
        "publisher",
        "publisher_contact_date",
        "score_locked_date"
    ]

    REQUIRED = OUTPUT_ORDER