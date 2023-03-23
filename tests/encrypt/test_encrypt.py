from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    #  retorna a mensagem corretamente com chaves pares
    assert encrypt_message('thais', 2) == 'sia_ht'
    # retorna a mensagem corretamente com chaves ímpares
    assert encrypt_message('thais', 3) == 'aht_si'
    assert encrypt_message('thais', 5) == 'siaht'
    with pytest.raises(TypeError):
        encrypt_message('thais', '1')
    with pytest.raises(TypeError):
        encrypt_message(2, 4)
