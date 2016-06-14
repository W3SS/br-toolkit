import string
import collections
from re import compile

class Informacoes():

    def palavras(text):
        """ Método que remove a pontuação da frase
        para poder retornar um array com todas as
        palavras de forma limpa """

        regex = compile("\w+")
        saida = regex.findall(text)
        return " ".join(saida)

    def conta_palavras(text):
        """ Função que retorna a contagem de todas
        as palavras de um texto selecionado pelo
        usuário"""

        return(collections.Counter(
        Geral.palavras(text).split(" ")
        ))

class Texto:
    def __init__(self):
        # Coleção
        self.emocoes = ['agressividade', 'afetividade', 'aflição', 'alegria', 'altruísmo', 'ambivalência', 'amizade', 'amor', 'angústia', 'ansiedade', 'antipatia', 'antecipação', 'apatia', 'arrependimento', 'arrogância', 'auto', 'piedade', 'avareza', 'bondade', 'bem', 'aventurança', 'benevolência', 'carinho', 'cobiça', 'compaixão', 'confusão', 'ciúme', 'constrangimento', 'coragem', 'culpa', 'curiosidade', 'contentamento', 'criatividade', 'depressão', 'desabafo', 'deslumbramento', 'desprezo', 'dó', 'decepção', 'dúvida', 'desapontamento', 'egoísmo', 'empatia', 'esperança', 'euforia', 'entusiasmo', 'epifania', 'excitação', 'fanatismo', 'felicidade', 'frieza', 'frustração', 'gratificação', 'gratidão', 'histeria', 'hostilidade', 'humor', 'humildade', 'humilhação', 'inspiração', 'interesse', 'indecisão', 'inveja', 'ira', 'isolamento', 'intriga', 'luxúria', 'mágoa', 'mau', 'humor', 'medo', 'melancolia', 'mazela', 'nojo', 'nostalgia', 'ódio', 'orgulho', 'paixão', 'paciência', 'pânico', 'pena', 'piedade', 'possessividade', 'prazer', 'preguiça', 'preocupação', 'paz', 'raiva', 'remorso', 'repugnância', 'resignação', 'ressentimento', 'saudade', 'schadenfreude', 'simpatia', 'soberba', 'sofrimento', 'solidão', 'surpresa', 'susto', 'tranquilidade', 'tédio', 'timidez', 'tristeza', 'vaidade', 'veracidade', 'vergonha', 'vingança']
        # Coleção de Stop Words
        self.stopwords = ['de', 'de', 'de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'é', 'com', 'não', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'foi', 'ao', 'ele', 'das', 'tem', 'à', 'seu', 'sua', 'ou', 'ser', 'quando', 'muito', 'há', 'nos', 'já', 'está', 'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'era', 'depois', 'sem', 'mesmo', 'aos', 'ter', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'estão', 'você', 'tinha', 'foram', 'essa', 'num', 'nem', 'suas', 'meu', 'às', 'minha', 'têm', 'numa', 'pelos', 'elas', 'havia', 'seja', 'qual', 'será', 'nós', 'tenho', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este', 'fosse', 'dele', 'tu', 'te', 'vocês', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'está', 'estamos', 'estão', 'estive', 'esteve', 'estivemos', 'estiveram', 'estava', 'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja', 'estejamos', 'estejam', 'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei', 'há', 'havemos', 'hão', 'houve', 'houvemos', 'houveram', 'houvera', 'houvéramos', 'haja', 'hajamos', 'hajam', 'houvesse', 'houvéssemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 'houverá', 'houveremos', 'houverão', 'houveria', 'houveríamos', 'houveriam', 'sou', 'somos', 'são', 'era', 'éramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja', 'sejamos', 'sejam', 'fosse', 'fôssemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'será', 'seremos', 'serão', 'seria', 'seríamos', 'seriam', 'tenho', 'tem', 'temos', 'tém', 'tinha', 'tínhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram', 'tivera', 'tivéramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivéssemos', 'tivessem', 'tiver', 'tivermos', 'tiverem', 'terei', 'terá', 'teremos', 'terão', 'teria', 'teríamos', 'teriam']
        # Coleção de Nomes mais comuns do Brasil
        self.nomes = ['Miguel', 'Sophia', 'Davi', 'Alice', 'Arthur', 'Julia', 'Pedro', 'Isabella', 'Gabriel', 'Manuela', 'Bernardo', 'Laura', 'Lucas', 'Luiza', 'Matheus', 'Valentina', 'Rafael', 'Giovanna', 'Heitor', 'Maria', 'Eduarda', 'Enzo', 'Helena', 'Guilherme', 'Beatriz', 'Nicolas', 'Maria', 'Luiza', 'Lorenzo', 'Lara', 'Gustavo', 'Mariana', 'Felipe', 'Nicole', 'Samuel', 'Rafaela', 'João', 'Pedro', 'Heloísa', 'Daniel', 'Isadora', 'Vitor', 'Lívia', 'Leonardo', 'Maria', 'Clara', 'Henrique', 'Ana', 'Clara', 'Theo', 'Lorena', 'Murilo', 'Gabriela', 'Eduardo', 'Yasmin', 'Pedro', 'Henrique', 'Isabelly', 'Pietro', 'Sarah', 'Cauã', 'Ana', 'Julia', 'Isaac', 'Letícia', 'Caio', 'Ana', 'Luiza', 'Vinicius', 'Melissa', 'Benjamin', 'Marina', 'João', 'Clara', 'Lucca', 'Cecília', 'João', 'Miguel', 'Esther', 'Bryan', 'Emanuelly', 'Joaquim', 'Rebeca', 'João', 'Vitor', 'Ana', 'Beatriz', 'Thiago', 'Lavínia', 'Antônio', 'Vitória', 'Davi', 'Lucas', 'Bianca', 'Francisco', 'Catarina', 'Enzo', 'Gabriel', 'Larissa', 'Bruno', 'Maria', 'Fernanda', 'Emanuel', 'Fernanda', 'João', 'Gabriel', 'Amanda', 'Ian', 'Alícia', 'Davi', 'Luiz', 'Carolina', 'Rodrigo', 'Agatha', 'Otávio', 'Gabrielly']
        # Coleção de badwords
        self.palavroes = ['filho da puta', 'viado', 'bicha', 'cacete', 'cusão', 'corno', 'corna', 'corno manso', 'sapatão', 'idiota', 'zé ruela', 'rola', 'chupa rola', 'putona', 'putão', 'safada', 'vadia', 'boqueteira', 'boqueteiro', 'cagão']
