class Teacher_CRUD():
    def __init__(self,database):
        self.db = database
    
    def create_teacher(self,name,ano_nasc,cpf):
        query = "CREATE(t:Teacher{name:$name,ano_nasc:$ano_nasc,cpf:$cpf})"
        parameters = {"name":name, "ano_nasc": ano_nasc, "cpf":cpf}
        self.db.execute_query(query,parameters)

    def read_teacher(self,name):
        query = "MATCH(t:Teacher{name:$name}) RETURN t.name AS name" 
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def update_teacher(self,name, newCpf):
        query = "MATCH(t:Teacher{name:$name}) SET t.cpf = $newCpf"
        parameters={"name": name, "cpf": newCpf}
        self.db.execute_query(query,parameters)
    
    def delete_teacher(self,name):
        query = "MATCH(t:Teacher{name:$name}) DETACH DELETE t"
        parameters = {"name":name}
        self.db.execute_query(query,parameters)


teacher = Teacher_CRUD()
teacher.create_teacher("Chris Lima", 1956, '189.052.396-66')
teacher.read_teacher('Chris Lima')
teacher.update_teacher('Chris Lima','162.052.777-77')
