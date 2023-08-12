import re


def extract_url(text):
    # Usar uma expressão regular para encontrar uma URL na string
    # A expressão regular busca por "http" ou "https" seguido por caracteres válidos em uma URL
    match = re.search(r"https?://\S+", text)

    if match:
        return match.group()
    else:
        return None


def extract_pregao_number(text):
    # Usar uma expressão regular para encontrar um valor após "Pregão Eletrônico Nº"
    match = re.search(r"Pregão Eletrônico Nº\s*([\w\d\/\\-]+)", text)

    if match:
        pregao_value = match.group(1)
        return pregao_value
    else:
        return None


def extract_first_three_lines(text):
    # Usar uma expressão regular para encontrar as três primeiras linhas
    match = re.search(r"(.*?\n.*?\n.*?\n)", text, re.DOTALL)

    if match:
        return match.group(1)
    else:
        return None


def extract_number(text):
    # Usar uma expressão regular para encontrar um número na string
    # \d+ corresponde a um ou mais dígitos (0-9)
    match = re.search(r"\d+", text)

    if match:
        return int(match.group())  # Converter o resultado em um número inteiro
    else:
        return None


def roda03():
    string = """Primeira linha
    Segunda linha
    Terceira linha
    Quarta linha
        """
    print(extract_first_three_lines(string.strip()))


def roda02():
    string = "Este é o Pregão Eletrônico Nº 123/2023 para aquisição de produtos."
    pregao_number = extract_pregao_number(string)

    if pregao_number is not None:
        print("Número do Pregão:", pregao_number)
    else:
        print("Nenhum número de Pregão encontrado na string.")


def roda01():
    string = "A string contém o número 12345 e outras informações."
    numero = extract_number(string)

    if numero is not None:
        print("Número extraído:", numero)
    else:
        print("Nenhum número encontrado na string.")


def roda():
    # string = "Aqui está uma URL: https://www.exemplo.com/pagina"
    string = """A Secretaria da Casa Civil https://www.exemplo.com/pagina torna público a REMARCAÇÃO do Pregão Eletrônico Nº 20221627, de interesse da Secretaria da Saúde - SESA, cujo OBJETO é: Serviço de administração, gerenciamento e controle de frota para manutenção preventiva e corretiva, com fornecimento total de peças, acessórios, reboque e componentes recomendados pelo fabricante de acordo com as características de cada veículo, maquinário, equipamento e implementos que compõe a frota da Secretaria de Saúde do Estado do Ceará, com implantação e operação de sistema informatizado, via internet, com tecnologia de pagamento on-line e real time por meio de cartão virtual ou sistema on-line, nas redes de estabelecimentos credenciados por todo o país, destinado à cobertura da SESA. MOTIVO: Alterações no Edital. RECEBIMENTO DAS PROPOSTAS VIRTUAIS: No endereço www.comprasnet.gov.br, através do Nº 16272022, até o dia 23/08/2023, às 9h (Horário de Brasília-DF). OBTENÇÃO DO EDITAL: No endereço eletrônico acima ou no site https://www.seplag.ce.gov.br
Fortaleza, 1º de Agosto de 2023"""
    url = extract_url(string)

    if url is not None:
        print("URL extraída:", url)
    else:
        print("Nenhuma URL encontrada na string.")


# roda()
# roda01()
# roda02()
roda03()
