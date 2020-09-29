import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('destinatario', ['brjatoba92@gmail.com', 'foo@bar.com.br'])
def test_remetente(destinatario):
    enviador = Enviador()

    resultado = enviador.enviar(destinatario, 'bruno.jatoba@icat.ufal.br', 'Cursos Python Pro',
                                'Este é um teste de envio de email usando o Python.', )

    assert destinatario in resultado


@pytest.mark.parametrize('remetente', ['', 'foo'])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente, 'bruno.jatoba@icat.ufal.br', 'Cursos Python Pro',
            'Este é um teste de envio de email usando o Python.',
        )
