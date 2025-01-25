from src.find.company_profile import CompanyProfile


class ESGReports:

    def __init__(self, company: CompanyProfile):
        self.company = company
        self.urls = {}
