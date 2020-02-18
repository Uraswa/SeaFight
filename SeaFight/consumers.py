from channels.generic.websocket import AsyncJsonWebsocketConsumer


class GameConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        game_id = self.scope['url_route']['kwargs']['id']
        is_host = self.scope['url_route']['kwargs']['is_host'] == "false"
        await self.channel_layer.group_add(game_id, self.channel_name)
        if is_host:
            await self.channel_layer.group_send(game_id, {"type": "game_connect"})

    async def receive_json(self, content, **kwargs):
        pass

    async def game_connect(self, event):
        await self.send_json({"type": "game_connect"})

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.scope['url_route']['kwargs']['id'], self.channel_name)


