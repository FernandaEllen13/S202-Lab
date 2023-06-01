
class Query:
    def get_teacher_renzo(self):
        query = "MATCH(t:Teacher) WHERE t.name = 'Renzo' RETURN t.ano_nasc,t.cpf AS ano_nasc,cpf"
        results = self.db.execute_query(query)
        return[(result["ano_nasc"],result["cpf"]) for result in results]
    
    def get_teacher_m(self):
        query = "MATCH(t:Teacher) WHERE t.name =~ 'M.*' RETURN t.name,t.cpf"
        results = self.db.execute_query(query)
        return[(result["name"],result["cpf"]) for result in results]
    
    def get_city(self):
        query = "MATCH(c:City) RETURN c.name"
        results = self.db.execute_query(query)
        return[result["name"] for result in results]
    
    def get_school(self):
        query = "MATCH(s:School) WHERE s.number >= 150 RETURN s.name, s.address, s.number"
        results = self.db.execute_query(query)
        return[result["name","address","number"] for result in results]
    
    def get_newer_older(self):
        query = "MATCH(t:Teacher) RETURN MAX(t.ano_nasc) AND MIN(t.ano_nasc)"
        results = self.db.execute_query(query)
        return[result["name","address","number"] for result in results]
    
    def get_population(self):
        query = "MATCH(c:City) RETURN AVG(c.population)"
        results = self.db.execute_query(query)
        return[result["name","address","number"] for result in results]

    def get_replace(self):
        query = "MATCH(c:City) WHERE c.cep = '37540-000' RETURN REPLACE(c.name,'a','A')"
        results = self.db.execute_query(query)
        return[result["name","address","number"] for result in results]
    
    def get_char(self):
        query = "MATCH(t:Teacher) RETURN substring(t.name,3,1)"
        results = self.db.execute_query(query)
        return[result["name","address","number"] for result in results]

    





