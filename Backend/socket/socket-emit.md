# Socket.io - io.emit(io.sockets.emit)과 socket.broadcast.emit의 차이

`io.emit`은 모든 연결된 클라이언트를 대상으로 한다.
값을 보낸 socket에 해당하는 클라이언트에게도 전달된다.

```js
io.on("connection", (socket) => {
  io.emit("hello", "world");
});
```

`io.broadcast.emit`은 값을 보낸 socket에 해당하는 클라이언트가 아닌 다른 클라이언트들을 대상으로 한다.

```js
io.on("connection", (socket) => {
  socket.broadcast.emit("hello", "world");
});
```

결론 : 차이는 sender의 socket에 해당하는 클라이언트에게 전달 유무이다.
