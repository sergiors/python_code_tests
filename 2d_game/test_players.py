from players import Player


def test_payer_position():
    player = Player()
    player.pos = player.move_right()
    player.pos = player.move_right()

    assert 12 == player.pos.x
