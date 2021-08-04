from model.db import DB

class UtilisateurModel():
    def __init__(self) -> None:
        self.conn=DB.connect()
    
    def fetch_all_utilisateur(self):
        self.conn.execute(
            """ SELECT id, nom, prenom FROM utilisateur """)
        rows=self.conn.fetchall()
        return rows
    
    def deleteById(self, id):
        # requête permettant la suppression d'un utilisateur
        self.conn.execute(
            f""" DELETE FROM utilisateur WHERE id = {int(id)} """
        )
    
    def addUser(self, data):
        # requête permettant l'ajout d'un utilisateur
        self.conn.execute(
            f"""INSERT INTO utilisateur(id, nom, prenom) VALUES('{int(data.get('id'))}', '{data.get('nom')}', '{data.get('prenom')}')"""
        )
    
    def update(self, data):
        # méthode permettant la mise à jour d'un continent
        self.conn.execute(
            f""" UPDATE utilisateur SET nom = '{data.get('nom')}', prenom = '{data.get('prenom')}' WHERE id = '{int(data.get('id'))}' """
        )