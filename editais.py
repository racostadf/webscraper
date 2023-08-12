class BidBr:
    def __init__(
        self, OrgaoNome, EditalNum, UasgNum, ObjetoTxt, DataAbertura, Objeto, WebSite
    ):
        self.OrgaoNome = OrgaoNome
        self.EditalNum = EditalNum
        self.UasgNum = UasgNum
        self.ObjetoTxt = ObjetoTxt
        self.DataAbertura = DataAbertura
        self.Objeto = Objeto
        self.WebSite = WebSite

    @property
    def orgao_nome(self):
        return self.OrgaoNome

    @orgao_nome.setter
    def orgao_nome(self, v_orgao):
        self.OrgaoNome = v_orgao

    @property
    def edital_num(self):
        return self.EditalNum

    @edital_num.setter
    def edital_num(self, v_edital_num):
        self.EditalNum = v_edital_num

    @property
    def uasg_num(self):
        return self.UasgNum

    @uasg_num.setter
    def uasg_num(self, v_uasg_num):
        self.UasgNum = v_uasg_num

    @property
    def objeto_txt(self):
        return self.ObjetoTxt

    @objeto_txt.setter
    def objeto_txt(self, v_objeto_txt):
        self.ObjetoTxt = v_objeto_txt

    @property
    def data_abertura(self):
        return self.DataAbertura

    @data_abertura.setter
    def data_abertura(self, v_data_abertura):
        self.DataAbertura = v_data_abertura

    @property
    def objeto(self):
        return self.Objeto

    @objeto.setter
    def objeto(self, v_objeto):
        self.Objeto = v_objeto

    @property
    def website(self):
        return self.WebSite

    @website.setter
    def website(self, v_website):
        self.WebSite = v_website

    def get_value(self):
        return (
            "\n".join(
                [
                    self.OrgaoNome,
                    self.EditalNum,
                    self.UasgNum,
                    self.ObjetoTxt,
                    self.DataAbertura,
                    self.Objeto,
                    self.WebSite,
                ]
            )
            + "\n"
        )
