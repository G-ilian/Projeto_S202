import pymongo

class Database:
    def __init__(self, database, collection, dataset=None):
        connectionString = "mongodb+srv://admin:admin@projetos202.cevdl.mongodb.net/?retryWrites=true&w=majority"
        self.clusterConnection = pymongo.MongoClient(
            connectionString,
            # CASO OCORRA O ERRO [SSL_INVALID_CERTIFICATE]
            tlsAllowInvalidCertificates=True
        )
        self.db = self.clusterConnection[database]
        self.collection = self.db[collection]
        if dataset:
            self.dataset = dataset

    def resetDatabase(self):
        self.db.drop_collection(self.collection)


    # Criando produtos no banco de dados
    def create_product_shovel(self, nome, quantidade,idProduto,marca,material_fabri,valor):
        return self.collection.insert_one({"idProduto": idProduto,"nome": nome, "quantidade": quantidade,"marca":marca,"material":material_fabri,"valor":valor})

    def create_product_pliers(self,nome,quantidade,idProduto,marca,cor,valor):
        return self.collection.insert_one({"idProduto": idProduto, "nome": nome, "quantidade": quantidade, "marca": marca,"cor":cor,"valor":valor})

    def create_product_hammer(self,nome,quantidade,idProduto,marca,cor,peso,valor):
        return self.collection.insert_one({"idProduto": idProduto,
                                           "nome": nome, "quantidade": quantidade, "marca": marca, "cor": cor,"peso":peso,"valor":valor})


    def read_product(self):
        response = self.collection.find({},{"idProduto":1,"nome": 1,"quantidade":1,"valor":1,"_id":0,"marca":1,"cor":1,"material":1})
        produtos = []
        for produto in response:
            produtos.append(produto)
        return produtos

    def update_product(self, id,quantidade):
        return self.collection.update_one(
            {"idProduto": id},
            {
                "$set":{"quantidade": quantidade},
                "$currentDate": {"lastModified": True}
            }
        )

    def delete_product(self, id):
        return self.collection.delete_one({"idProduto": id})