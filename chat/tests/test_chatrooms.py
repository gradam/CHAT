import pytest
from channels.testing import WebsocketCommunicator

from channels_pro.routing import application


@pytest.mark.asyncio
async def test_consumer(fake):
    message = fake.text()
    communicator = WebsocketCommunicator(application, "ws/chat/test/")
    connected = await communicator.connect()
    assert connected
    await communicator.send_json_to({"message": message})
    response = await communicator.receive_json_from()
    assert response == {"message": message}
    await communicator.disconnect()
