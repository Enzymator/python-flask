from model.bd import DB

class utilisateurModel():
    def __init__(self) -> None:
        self.conn=DB.connect()
    
    def fetch_all_continent(self):
        self.conn.execute(
            """ SELECT id_continent, nom_continent FROM continent """)
        rows=self.conn.fetchall()
        return rows
    
    def deleteById(self, id):
        # requête permettant la suppression d'un continent
        self.conn.execute(
            f""" DELETE FROM continent WHERE id_continent = {int(id)} """
        )
    
    def addContinent(self, data):
        # requête permettant l'ajout d'un continent
        self.conn.execute(
            f"""INSERT INTO continent(id_continent, nom_continent) VALUES('{int(data.get('id'))}', '{data.get('nom')}')"""
        )
    
    def update(self, data):
        # méthode permettant la mise à jour d'un continent
        self.conn.execute(
            f""" UPDATE continent SET nom_continent = '{data.get('nom')}' WHERE id_continent = '{int(data.get('id'))}' """
        )