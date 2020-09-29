from unittest.mock import Mock

import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Bruno', email='brjatoba92@gmail.com'),
            Usuario(nome='Rafael', email='bruno.jatoba@icat.ufal.br')
        ],
        [
            Usuario(nome='Bruno', email='brjatoba92@gmail.com')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'brjatoba92@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantasticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


"""
class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1
"""


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Bruno', email='brjatoba92@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('bruno.jatoba@icat.ufal.br', 'Curso Python Pro', 'Confira os módulos fantasticos')
    enviador.enviar.assert_called_once_with == (
        'bruno.jatoba@icat.ufal.br',
        'brjatoba92@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantasticos'
    )
