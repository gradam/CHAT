import pytest
from channels.testing import WebsocketCommunicator

from channels_pro.routing import application


@pytest.mark.asyncio
async def test_consumer(fake):
    room = fake.word()
    wrong_room = fake.word()

    message = fake.text()

    communicator = WebsocketCommunicator(application, f"ws/chat/{room}/")
    wrong_communicator = WebsocketCommunicator(application, f"ws/chat/{wrong_room}/")

    wrong_connected = await wrong_communicator.connect()
    connected = await communicator.connect()

    assert connected
    assert wrong_connected

    await communicator.send_json_to({"message": message})

    response = await communicator.receive_json_from()

    try:
        wrong_response = await wrong_communicator.receive_json_from()
    except:
        wrong_response = None

    assert response == {"message": message}
    assert not wrong_response

    await communicator.disconnect()
    await wrong_communicator.disconnect()
