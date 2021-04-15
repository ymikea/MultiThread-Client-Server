# SERVER/CLIENT

## Files
- server_part1.py
- server_part2.py
- client.py
- index.html
- README.md


## Run Instructions
python3 server_part1.py
python3 server_part2.py
python3 client.py


## Author
### 👤 Yekaalo Habtemichael
* Github: [@ymikea](https://github.com/ymikea)


## Implementation
Part 1.
The program connects server and client. The server runs on a fixed port which listens for any request from clients. Once client requets connection to server, then accept establishes and server send the contents to client. The client displays the content on the browser.

Part 2.
The program works the same as part one. However, part 2 accepts multiple clients requets by utilizing multi threads. After the connection is prepared and server is ready to accept, the thread will starts to serve multiple requests at a given time.

Client program is provided for testing purposes. Since part 2 accepts multiple requests, running the client program in multiple terminals will allow as to test past 2 program.

Index.html file will be the contents that will be served to the client.


## License
[MIT](https://choosealicense.com/licenses/mit/) &copy; 2020 Yekaalo Habtemichael 
