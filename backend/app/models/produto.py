from app import db


class Produto(db.Model):
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    quantidade_estoque = db.Column(db.Integer, nullable=False, default=0)
    categoria = db.Column(db.String(80), nullable=True)
    
    def __repr__(self):
        return f'<Produto {self.id}: {self.nome}>'