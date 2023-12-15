# Данила Образцов, 11 когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

def test_created_order():
    response = sender_stand_request.creation_order(data.body)
    assert response.status_code == 201, 'Order not creation'

def test_order_by_track():
    track = sender_stand_request.order_track()
    response = sender_stand_request.get_order_on_track(track)
    assert response.status_code == 200, 'Order not exist'


